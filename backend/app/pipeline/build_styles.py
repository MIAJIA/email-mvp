"""Scenario style by rule, no model: each habit is a regex counted over all sent emails of a scenario.
Evidence is the matching line, so it is a verbatim substring by construction.

Usage: .venv/bin/python -m app.pipeline.build_styles
"""
from __future__ import annotations

import json
import re

from ..schema import Evidence, Habit, ScenarioStyle
from ..stores import REPO, STYLE_DIR, EmailStore

HABITS = {
    "friend_scheduling": [
        ("open_hey", "Opens with \"Hey\"", r"^\s*Hey\b"),
        ("open_hi_name", "Opens with \"Hi <name>,\"", r"^\s*Hi \w+,"),
        ("prefer_offline", "Suggests meeting in person", r"in person|offline|Red Rock"),
        ("sign_bare_mia", "Signs off with just \"Mia\"", r"\n\s*Mia\s*$"),
    ],
    "vendor_service": [
        ("open_dear", "Opens with \"Dear <name>,\"", r"^\s*Dear \w+"),
        ("thank_first", "Thanks them in the first line", r"^\s*Dear[^\n]*[\n,]\s*(\n\s*)?Thank"),
        ("numbered_followups", "Lists requests as a numbered list", r"\n\s*1\.\s"),
        ("sign_best", "Signs off with \"Best,\"", r"\nBest,\s*\n"),
    ],
}


def line_at(body: str, start: int) -> str:
    s = body.rfind("\n", 0, start) + 1
    e = body.find("\n", start)
    return body[s:e if e != -1 else len(body)].strip() or body[start:start + 60].strip()


def build(emails: EmailStore) -> list[ScenarioStyle]:
    out = []
    for scenario, habits in HABITS.items():
        mails = [e for e in emails.by_id.values() if e.category == scenario]
        hs = []
        for hid, desc, pattern in habits:
            rx = re.compile(pattern)
            hits = [(e, m) for e in mails if (m := rx.search(e.body))]
            evidence = [Evidence(message_id=e.message_id, quote=line_at(e.body, m.start())) for e, m in hits[:3]]
            hs.append(Habit(id=hid, description=desc, count=len(hits), total=len(mails), evidence=evidence))
        out.append(ScenarioStyle(scenario=scenario, habits=hs))
    return out


if __name__ == "__main__":
    STYLE_DIR.mkdir(parents=True, exist_ok=True)
    for s in build(EmailStore()):
        (STYLE_DIR / f"{s.scenario}.json").write_text(json.dumps(s.model_dump(exclude_none=True), ensure_ascii=False, indent=2))
        print(s.scenario, [(h.id, h.count, h.total) for h in s.habits])
