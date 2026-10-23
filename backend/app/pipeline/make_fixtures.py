"""Generate fixtures/drafts/*.json from recordings/*.json (never by hand), and check them.

Usage: .venv/bin/python -m app.pipeline.make_fixtures [--check]
--check: regenerate in memory, fail if fixtures are stale, every fixture validates against Draft, the Draft
invariants hold, and every evidence quote is a verbatim substring of its source email.
"""
from __future__ import annotations

import json
import sys

from ..schema import Draft, DraftRequest
from ..stores import REPO, EmailStore, MockExternalContextProvider
from ..verifier import Verifier

REC = REPO / "recordings"
OUT = REPO / "fixtures/drafts"


def problems(d: Draft, verifier: Verifier) -> list[str]:
    out = []
    ids = {h.id for h in d.highlights}
    for s in d.segments:
        if s.highlight_id and s.highlight_id not in ids:
            out.append(f"segment points at missing highlight {s.highlight_id}")
    for h in d.highlights:
        for ev in h.evidence:
            if not verifier.check(ev):
                out.append(f"{h.id} evidence does not verify: {ev.message_id or ev.external_id} {ev.quote!r}")
    return out


def main(check: bool) -> int:
    emails = EmailStore()
    expected = {}
    bad = []
    for p in sorted(REC.glob("*.json")):
        rec = json.loads(p.read_text())
        DraftRequest(**rec["request"])  # the request the front end actually sent must still validate
        d = Draft(**rec["response"])
        bad += [f"{p.name}: {x}" for x in problems(d, Verifier(emails, MockExternalContextProvider().get(d.to)))]
        expected[p.name] = json.dumps(d.model_dump(), ensure_ascii=False, indent=2) + "\n"
    if check:
        for name, text in expected.items():
            f = OUT / name
            if not f.exists() or f.read_text() != text:
                bad.append(f"stale fixture {name}: run python -m app.pipeline.make_fixtures")
    else:
        OUT.mkdir(parents=True, exist_ok=True)
        for name, text in expected.items():
            (OUT / name).write_text(text)
    for b in bad:
        print("FAIL", b)
    print(f"{len(expected)} recordings, {len(bad)} problems")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main("--check" in sys.argv))
