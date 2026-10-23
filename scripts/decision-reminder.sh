#!/usr/bin/env bash
# scripts/decision-reminder.sh — UserPromptSubmit hook. A reminder, not an enforcer.
#
# Every time a prompt reaches this session (typed by the user, or a report from a background subagent, a
# message from another session, a scheduled turn), this adds one short paragraph to Claude's context: if the
# message carries a decision, append it to $MAIN/DECISIONS.md before acting; if it introduces a term, add it to
# $MAIN/GLOSSARY.md. It never blocks a prompt and never changes it.
#
# Why: decisions said in one session (or relayed in a report) were not reaching the other sessions. The
# checkpoint review by the user stays the real safety net; this only makes forgetting less likely.
#
# Register in .claude/settings.json under hooks.UserPromptSubmit (see templates/settings.json).
# Make executable: chmod +x scripts/decision-reminder.sh
# Test: echo '{"prompt":"let us not do X","cwd":"'"$PWD"'"}' | scripts/decision-reminder.sh

set -u

input=$(cat)

# Any failure below must stay silent and exit 0: a broken reminder must never block the user's prompt.
printf '%s' "$input" | python3 -I -c '
import json, os, subprocess, sys

try:
    data = json.load(sys.stdin)
except Exception:
    sys.exit(0)

cwd = data.get("cwd") or os.getcwd()

# The main checkout, found from any worktree: the common git dir is <main>/.git.
main = None
try:
    common = subprocess.run(["git", "rev-parse", "--path-format=absolute", "--git-common-dir"],
                            cwd=cwd, capture_output=True, text=True, timeout=3).stdout.strip()
    if common:
        main = os.path.dirname(common.rstrip("/"))
except Exception:
    pass
if not main:
    sys.exit(0)

decisions = os.path.join(main, "DECISIONS.md")
glossary = os.path.join(main, "GLOSSARY.md")
if not os.path.exists(decisions):
    sys.exit(0)  # not a swarm-control project yet

text = (
    "Decision check (swarm-control). If the message above contains a decision (explicit or implicit; from the "
    "user, someone they brought in, or relayed in a report), append it now to " + decisions + " in the log "
    "format, with the source quoted, before acting on it. Test: would a new session that reads only the files "
    "choose differently without knowing it? When unsure, log it as unconfirmed. If it introduces a new term, "
    "append it to " + glossary + " as proposed. If it decides nothing, ignore this note."
)

print(json.dumps({"hookSpecificOutput": {"hookEventName": "UserPromptSubmit", "additionalContext": text}}))
' 2>/dev/null

exit 0
