"""FastAPI app. Live mode (8041) calls the model and records /draft; REPLAY=1 (8042) serves recordings only."""
from __future__ import annotations

import hashlib
import json
import os
from datetime import datetime, timezone

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware

from . import llm
from .generator import DEFAULT_SCENARIO, generate
from .schema import (CONTRACT_REVISION, ContactNote, ContactSummary, Draft, DraftRequest, Email,
                     FeedbackRequest, FeedbackResponse)
from .stores import REPO, EmailStore, MarkdownContactStore, MockExternalContextProvider, StyleStore

REPLAY = os.environ.get("REPLAY") == "1"
RECORD = os.environ.get("RECORD", "1") == "1" and not REPLAY
RECORDINGS = REPO / "recordings"

app = FastAPI(title="email-mvp", version=CONTRACT_REVISION)
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

emails = EmailStore()
contacts = MarkdownContactStore()
styles = StyleStore()
external = MockExternalContextProvider()
DRAFTS: dict[str, Draft] = {}


def case_key(req: DraftRequest) -> str:
    canon = json.dumps({"mode": req.mode, "to": req.to, "thread_id": req.thread_id, "brief": req.brief.strip(), **({"inject": req.inject} if req.inject else {})},
                       sort_keys=True, ensure_ascii=False)
    return hashlib.sha1(canon.encode()).hexdigest()[:10]


def load_recordings() -> dict[str, dict]:
    out = {}
    for p in sorted(RECORDINGS.glob("*.json")):
        rec = json.loads(p.read_text())
        out[rec["case_key"]] = rec
        d = Draft(**rec["response"])
        DRAFTS[d.draft_id] = d
    return out


REPLAYS = load_recordings() if REPLAY else {}


@app.get("/health")
def health():
    return {"ok": True, "replay": REPLAY, "contract_revision": CONTRACT_REVISION}


@app.get("/contacts", response_model=list[ContactSummary])
def list_contacts():
    return contacts.list()


@app.get("/contacts/{email}", response_model=ContactNote)
def get_contact(email: str):
    note = contacts.get(email)
    if not note:
        raise HTTPException(404, "no contact note")
    return note


@app.get("/emails/{message_id}", response_model=Email)
def get_email(message_id: str):
    e = emails.get(message_id)
    if not e:
        raise HTTPException(404, "no such email")
    return e


@app.get("/threads")
def list_threads():
    return []  # stub: reply mode is out of the skeleton (DECISIONS 14:14)


@app.post("/draft", response_model=Draft)
async def draft(request: Request):
    raw = await request.json()
    req = DraftRequest(**raw)
    key = case_key(req)
    if REPLAY:
        rec = REPLAYS.get(key)
        if not rec:
            raise HTTPException(404, f"no recording for case {key}")
        return Draft(**rec["response"])
    note = contacts.get(req.to)
    scenario = (note.scenario if note and note.scenario else None) or emails.scenario_for(req.to) or DEFAULT_SCENARIO
    if note and not note.scenario:
        note.scenario = scenario
    style = styles.get(scenario)
    try:
        d = generate(req, note, style, external.get(req.to), llm.complete, n_emails=len(emails.to(req.to)))
    except llm.LLMError as e:
        raise HTTPException(502, f"model call failed: {e}")
    DRAFTS[d.draft_id] = d
    if RECORD:
        RECORDINGS.mkdir(exist_ok=True)
        slug = req.to.split("@")[0].replace(".", "-")
        rec = {"case_key": key, "endpoint": "POST /draft", "contract_revision": CONTRACT_REVISION,
               "recorded_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
               "request": raw, "response": d.model_dump()}
        (RECORDINGS / f"{slug}-{key}.json").write_text(json.dumps(rec, ensure_ascii=False, indent=2))
    return d


@app.post("/feedback", response_model=FeedbackResponse)
def feedback(fb: FeedbackRequest):
    d = DRAFTS.get(fb.draft_id)
    h = next((h for h in d.highlights if h.id == fb.highlight_id), None) if d else None
    if not h or not h.ref:
        raise HTTPException(404, "unknown draft or highlight")
    status = "confirmed" if fb.action == "accept" else "rejected"
    if REPLAY or h.layer != "person":
        # Replay never writes; scenario/external entries are not per-contact (not persisted).
        return FeedbackResponse(email=d.to, ref=h.ref, status=status)
    contacts.set_status(d.to, f"{h.ref.kind}:{h.ref.id}", status)
    return FeedbackResponse(email=d.to, ref=h.ref, status=status)
