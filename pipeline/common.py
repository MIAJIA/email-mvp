"""Shared helpers for the offline extraction pipeline.

The pipeline never reads data/ground_truth/ or any planted_* field; only evaluate.py touches ground truth.
"""
from __future__ import annotations

import json
import os
import re
import subprocess
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
OUT = Path(__file__).resolve().parent / "out"
RAW = OUT / "raw"

# Fields the pipeline is allowed to see. Anything else (planted_*, ...) is dropped on load.
EMAIL_FIELDS = ("thread_id", "message_id", "date", "to", "to_name", "subject", "body",
                "prev", "prev_sender", "category", "source")


def load_emails() -> list[dict]:
    emails = []
    for path in sorted((DATA / "emails").glob("*.jsonl")):
        for line in path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            row = json.loads(line)
            emails.append({k: row.get(k) for k in EMAIL_FIELDS})
    return emails


def load_external() -> dict[str, list[dict]]:
    path = DATA / "external.json"
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def norm_email(addr: str | None) -> str:
    return (addr or "").strip().lower()


def group_by_recipient(emails: list[dict]) -> dict[str, list[dict]]:
    groups: dict[str, list[dict]] = defaultdict(list)
    for e in emails:
        if e.get("to"):
            groups[norm_email(e["to"])].append(e)
    for msgs in groups.values():
        msgs.sort(key=lambda e: e.get("date") or "")
    return dict(groups)


def group_by_scenario(emails: list[dict]) -> dict[str, list[dict]]:
    groups: dict[str, list[dict]] = defaultdict(list)
    for e in emails:
        groups[e.get("category") or "uncategorized"].append(e)
    return dict(groups)


def call_claude(prompt: str, timeout: int = 300) -> str:
    """One `claude -p` call on the user's subscription (ANTHROPIC_API_KEY removed, so no API billing)."""
    env = {k: v for k, v in os.environ.items() if k != "ANTHROPIC_API_KEY"}
    proc = subprocess.run(
        ["claude", "-p", "--no-session-persistence", "--output-format", "text"],
        input=prompt, capture_output=True, text=True, env=env, timeout=timeout,
        cwd=str(RAW),  # neutral cwd: keeps project hooks and CLAUDE.md out of the extraction call
    )
    if proc.returncode != 0:
        raise RuntimeError(f"claude -p failed ({proc.returncode}): {proc.stderr[:500]}")
    return proc.stdout


def parse_json_block(text: str) -> dict:
    """Take the outermost JSON object from a model reply (tolerates ```json fences)."""
    fenced = re.search(r"```(?:json)?\s*(\{.*\})\s*```", text, re.S)
    candidate = fenced.group(1) if fenced else text[text.find("{"): text.rfind("}") + 1]
    return json.loads(candidate)


def safe_name(s: str) -> str:
    return re.sub(r"[^A-Za-z0-9@._+-]", "_", s)
