#!/usr/bin/env bash
# scripts/check.sh — run every check in COORDINATION.md's Checks table with real exit codes.
#
# Rules this script encodes:
#   - set -euo pipefail: the first failing check stops the run, and a pipe cannot hide a failure
#     (a commit once went in with 37 failing tests because `pytest | tail -1 && git commit` took tail's status).
#   - Each check prints its name, its command, and PASS/FAIL. Nothing is summarised away.
#   - The eval replay (only if the product calls a model) compares the FAIL/ERROR set with the last recorded
#     run instead of "it ran".
#   - The glossary check fails on any deprecated name from $MAIN/GLOSSARY.md found in tracked files.
#   - Generated files must be fresh: each generator runs in --check mode (or regenerates into a temp dir and
#     diffs), so a stale fixture or mirror fails here instead of at the next walkthrough.
#
# Fill the CHECKS array from COORDINATION.md. Keep the two in step: the table is what humans read, this is
# what runs. At CP0 the repository is empty, so the active array holds only the glossary check; anything else
# would fail the scaffold commit. The project skeleton line proposes the real list in its merge request, and the
# Lead applies it here and in COORDINATION.md after the user approves.
# Usage: scripts/check.sh [--only <name>]

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd -P)"
cd "$ROOT"

ONLY="${2:-}"
[[ "${1:-}" == "--only" ]] || ONLY=""

# name|command  — one per line. Edit these for the project.
CHECKS=(
  "glossary|scripts/check.sh __glossary"
  "data-validate|python3 -I data/validate.py"
  "backend-tests|cd backend && .venv/bin/python -m pytest -q"
  "frontend-build|cd frontend && npx tsc -b && npx vite build"
  "fixtures-and-evidence|cd backend && .venv/bin/python -m app.pipeline.make_fixtures --check"
  # Examples from a Python + Vite project, kept commented out until the user approves the skeleton line's
  # proposed list. Replace the commands with the project's own.
  # "backend-tests|.venv/bin/python -m pytest -q"
  # "frontend-tests|cd web && npx vitest run"
  # "types|cd web && npx tsc --noEmit"
  # "build|cd web && npx vite build"
  # "generated-fresh|.venv/bin/python <generator script> --check"
  # "language-sweep|scripts/check.sh __language"
  # "eval-replay|scripts/check.sh __eval_replay"      # only if the product calls a model
)

# ---- helpers used by the named checks above ------------------------------------------------------------

# The main checkout, found from any worktree: the common git dir is <main>/.git.
main_checkout() {
  local common
  common=$(git rev-parse --git-common-dir)
  (cd "$common/.." && pwd -P)
}

__glossary() {
  # Every name in the "Deprecated" column of GLOSSARY.md (backticked, comma-separated) must not appear in any
  # tracked file. The glossary lives only in the main checkout ($MAIN/GLOSSARY.md, untracked). Coordination
  # records are never committed in this project, so a fresh clone has no glossary and skips this check.
  local main glossary terms hits=""
  main=$(main_checkout)
  glossary="$main/GLOSSARY.md"
  if [[ ! -f "$glossary" ]]; then
    echo "glossary: no GLOSSARY.md in $main (fresh clone) — skipped"
    return 0
  fi
  terms=$(python3 -I - "$glossary" <<'PY'
import re, sys
col = None
for line in open(sys.argv[1], encoding="utf-8"):
    if not line.lstrip().startswith("|"):
        continue
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    if col is None:
        if "Deprecated" in cells:
            col = cells.index("Deprecated")
        continue
    if col < len(cells):
        # \x60 is a backtick; a literal one here would break bash's parsing of this $( ... ) heredoc.
        for t in re.findall("\x60([^\x60]+)\x60", cells[col]):
            print(t)
PY
)
  [[ -z "$terms" ]] && return 0
  while IFS= read -r t; do
    [[ -z "$t" ]] && continue
    local found
    found=$(git grep -n -w -F -e "$t" -- . ':!GLOSSARY.md' || true)
    [[ -n "$found" ]] && hits+="deprecated name '$t':"$'\n'"$found"$'\n'
  done <<< "$terms"
  if [[ -n "$hits" ]]; then
    printf '%s' "$hits" | head -40
    echo "glossary: deprecated names found above; use the current term from GLOSSARY.md"
    return 1
  fi
  return 0
}

__language() {
  # User-visible strings must be in the agreed language. Default here: no CJK in UI source files. Adjust the
  # paths and the character range to the decision in DECISIONS.md. Uses python, not grep -P (absent on macOS,
  # where a silent grep error would make this check always pass).
  python3 -I - web/src <<'PY'
import os, re, sys
cjk = re.compile(r"[一-鿿]")
bad = []
for root in sys.argv[1:]:
    for d, _, files in os.walk(root):
        for f in files:
            if not f.endswith((".ts", ".tsx")):
                continue
            p = os.path.join(d, f)
            for i, line in enumerate(open(p, encoding="utf-8", errors="ignore"), 1):
                s = line.strip()
                if s.startswith("//") or s.startswith("*"):
                    continue
                if cjk.search(line):
                    bad.append(f"{p}:{i}: {s[:100]}")
if bad:
    print("\n".join(bad[:20]))
    print("language-sweep: text in the wrong language found above")
    sys.exit(1)
PY
}

# Only if the product calls a model. Delete this helper otherwise.
# REPLAY_UNSET_ENV names the provider key variables (space-separated) that are unset during the replay, so a
# cassette miss fails instead of silently making a paid call. REPLAY_CMD is the project's replay command.
REPLAY_UNSET_ENV="${REPLAY_UNSET_ENV:-<YOUR_PROVIDER>_API_KEY}"
REPLAY_CMD="${REPLAY_CMD:-.venv/bin/python -m <eval runner module> --replay}"

__eval_replay() {
  # Replay the recorded eval run without network and compare the FAIL/ERROR set with the recorded report.
  # Restore any result files the replay rewrote unless regenerating them is the point.
  local run_dir="${EVAL_RUN_DIR:-<eval results dir>/latest}"
  [[ -d "$run_dir" ]] || { echo "eval-replay: no recorded run at $run_dir (set EVAL_RUN_DIR)"; return 1; }
  local before after unset_args=() v
  for v in $REPLAY_UNSET_ENV; do unset_args+=(-u "$v"); done
  before=$(grep -E 'FAIL|ERROR' "$run_dir/report.md" | sort || true)
  # shellcheck disable=SC2086  # REPLAY_CMD is a command line and is meant to be split into words.
  env ${unset_args[@]+"${unset_args[@]}"} $REPLAY_CMD "$run_dir" >/dev/null
  after=$(grep -E 'FAIL|ERROR' "$run_dir/report.md" | sort || true)
  git checkout -- "$run_dir" 2>/dev/null || true
  if [[ "$before" != "$after" ]]; then
    echo "eval-replay: FAIL/ERROR set changed against the recorded run:"
    diff <(echo "$before") <(echo "$after") || true
    return 1
  fi
  return 0
}

case "${1:-}" in
  __glossary) __glossary; exit $? ;;
  __language) __language; exit $? ;;
  __eval_replay) __eval_replay; exit $? ;;
esac

# ---- main loop ------------------------------------------------------------------------------------------

failed=0
for entry in "${CHECKS[@]}"; do
  name="${entry%%|*}"; cmd="${entry#*|}"
  [[ -n "$ONLY" && "$ONLY" != "$name" ]] && continue
  echo "== $name: $cmd"
  if (eval "$cmd"); then
    echo "== $name: PASS"
  else
    echo "== $name: FAIL (exit $?)"
    failed=1
    break
  fi
done

if [[ $failed -ne 0 ]]; then
  echo "check.sh: FAILED — do not commit on main."
  exit 1
fi
echo "check.sh: all checks passed at $(date '+%Y-%m-%d %H:%M')."
