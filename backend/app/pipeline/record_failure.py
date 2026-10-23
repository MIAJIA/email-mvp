"""Record the failure case: a canned model output that cites a ref the note does not have.
It cannot be produced on demand from the real model, so this recording is marked synthetic.

Usage: .venv/bin/python -m app.pipeline.record_failure
"""
from __future__ import annotations

import json

from ..generator import generate
from ..main import case_key
from ..schema import CONTRACT_REVISION, DraftRequest
from ..stores import REPO, MarkdownContactStore, StyleStore

CANNED = ('Subject: Coffee Friday\n\n<hl ref="address_as">Hey Ethan,</hl>\n\n'
          'Friday works. <hl ref="fact:met_in_paris">Like that time we met in Paris</hl>, let\'s do Red Rock.\n\nMia')

if __name__ == "__main__":
    raw = {"mode": "compose", "to": "ethan.park@example.com", "brief": "[synthetic] model cites a ref that does not exist"}
    req = DraftRequest(**raw)
    note = MarkdownContactStore().get(req.to)
    d = generate(req, note, StyleStore().get(note.scenario), [], lambda _: CANNED)
    d.draft_id = "synthetic-unknown-ref"
    rec = {"case_key": case_key(req), "endpoint": "POST /draft", "contract_revision": CONTRACT_REVISION,
           "recorded_at": "synthetic", "source": "synthetic: canned model output, request not sent by the front end",
           "request": raw, "response": d.model_dump()}
    (REPO / "recordings/failure-unknown-ref.json").write_text(json.dumps(rec, ensure_ascii=False, indent=2))
    print(d.warnings, [s.highlight_id for s in d.segments])
