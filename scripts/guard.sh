#!/usr/bin/env bash
# scripts/guard.sh — PreToolUse hook for Bash. A tripwire, not a wall.
#
# It reads the hook's JSON from stdin, looks at tool_input.command and cwd, and prints a permissionDecision.
# It catches the spellings Claude usually writes. It does not catch /usr/bin/pkill, bash -c '...', git -C . push,
# or kill <pid> of someone else's process by number, and the settings file that registers it reloads when
# edited. The rules in COORDINATION.md, the Integrator's routine and the pre-commit are the wall.
#
# Decisions:
#   deny  — kill/pkill/killall; git checkout --ours|--theirs; git push --force; git reset --hard; git clean -fdx;
#           rm -rf outside the repository; git push from a linked worktree.
#   ask   — git push from the main checkout (every push is a prompt the user answers; one OK covers one push).
#   allow — everything else (no output).
#
# Register in .claude/settings.json (see templates/settings.json). Make executable: chmod +x scripts/guard.sh.
# Test: echo '{"tool_input":{"command":"pkill -f api"},"cwd":"'"$PWD"'"}' | scripts/guard.sh

set -u

input=$(cat)

# Extract fields without jq (python3 is on every macOS/Linux dev box; fall back to allow if parsing fails).
# shlex.quote makes the two assignments safe to eval whatever the command contains.
cmd=""; cwd=""
eval "$(printf '%s' "$input" | python3 -I -c '
import json, sys, shlex
try:
    o = json.load(sys.stdin)
    c = o.get("tool_input", {}).get("command", "") or ""
    d = o.get("cwd", "") or ""
except Exception:
    c, d = "", ""
print("cmd=" + shlex.quote(c.replace("\n", " ")))
print("cwd=" + shlex.quote(d))
' 2>/dev/null)"

[[ -z "$cmd" ]] && exit 0

emit() { # $1 = deny|ask, $2 = reason
  printf '{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"%s","permissionDecisionReason":%s}}\n' \
    "$1" "$(printf '%s' "$2" | python3 -I -c 'import json,sys; print(json.dumps(sys.stdin.read()))')"
  exit 0
}

# Normalise: collapse whitespace so patterns are simpler.
flat=$(printf '%s' "$cmd" | tr '\n' ' ' | tr -s ' ')

# 1. Process killing of any kind.
if printf '%s' "$flat" | grep -Eq '(^|[;&|(` ])(pkill|killall|kill)([ )]|$)|xargs +kill'; then
  emit deny "Guard: killing processes from the shell is blocked for every role. Stop only the servers you started, through the background task you started them with (TaskStop). If a port you need is busy, ask the user; never free it. Reserved ports and PIDs are in COORDINATION.md."
fi

# 2. Whole-file conflict resolution.
if printf '%s' "$flat" | grep -Eq 'git +(checkout|restore) +[^;&|]*--(ours|theirs)'; then
  emit deny "Guard: git checkout/restore --ours/--theirs takes the whole file and silently drops the other side's non-conflicting hunks. Resolve each <<<<<<< hunk by hand; if you already ran it, recreate the conflict with 'git checkout -m <file>' and redo it. See integration-gate step 2."
fi
if printf '%s' "$flat" | grep -Eq 'git +merge +[^;&|]*-X *(ours|theirs)'; then
  emit deny "Guard: git merge -X ours/theirs resolves every conflict blind. Merge without a strategy option and resolve hunks by hand."
fi

# 3. History and tree destruction.
if printf '%s' "$flat" | grep -Eq 'git +push +[^;&|]*(--force|-f( |$)|\+[A-Za-z])'; then
  emit deny "Guard: force push is blocked. main only moves fast-forward; a bad merge is undone with 'git revert -m 1 <merge-sha>'."
fi
if printf '%s' "$flat" | grep -Eq 'git +reset +[^;&|]*--hard'; then
  emit deny "Guard: git reset --hard is blocked. Use 'git revert' for commits, 'git stash' or 'git checkout -- <file>' for a single file, and ask the user before discarding work."
fi
if printf '%s' "$flat" | grep -Eq 'git +clean +[^;&|]*-[a-zA-Z]*[fdx]'; then
  emit deny "Guard: git clean is blocked: it deletes untracked files, including other sessions' ledgers and recordings. Delete named files on purpose instead."
fi

# 4. rm -rf outside the repository (or on the repository root itself).
if printf '%s' "$flat" | grep -Eq '(^|[;&|(` ])rm +(-[a-zA-Z]*r[a-zA-Z]*f|-[a-zA-Z]*f[a-zA-Z]*r)'; then
  repo=$(cd "$cwd" 2>/dev/null && git rev-parse --show-toplevel 2>/dev/null || true)
  targets=$(printf '%s' "$flat" | sed -E 's/.*rm +-[a-zA-Z]+ +//; s/[;&|].*$//')
  for t in $targets; do
    case "$t" in
      /*|~*|..*|'$'*) emit deny "Guard: rm -rf on a path outside the repository ($t) is blocked. Delete inside the repo only, by explicit relative path, and ask before deleting anything shared." ;;
    esac
    resolved=$(cd "$cwd" 2>/dev/null && { cd "$t" 2>/dev/null && pwd -P || echo "$(cd "$(dirname "$t")" 2>/dev/null && pwd -P)/$(basename "$t")"; })
    if [[ -n "$repo" && "$resolved" == "$repo" ]]; then
      emit deny "Guard: rm -rf on the repository root is blocked."
    fi
  done
fi

# 5. git push: ask in the main checkout, deny in a linked worktree.
if printf '%s' "$flat" | grep -Eq '(^|[;&|(` ])git +push([ )]|$)'; then
  gitdir=$(cd "$cwd" 2>/dev/null && git rev-parse --git-dir 2>/dev/null || true)
  case "$gitdir" in
    *"/.git/worktrees/"*)
      emit deny "Guard: pushing from a linked worktree is blocked. Line owners commit to their branch and write a merge request; only the Integrator pushes main, from the main checkout, after the user's OK." ;;
    *)
      emit ask "Guard: a push to the remote. One OK from the user covers this push only. Confirm it is fast-forward (git merge-base --is-ancestor origin/main HEAD) and that the user agreed in this context." ;;
  esac
fi

exit 0
