"""Offline workflow: one contact's sent emails -> model proposes entries with quotes -> Verifier drops
unverifiable quotes -> code counts support -> backend/notes/contacts/<email>.md.

Usage: .venv/bin/python -m app.pipeline.extract <email> [<email> ...]
"""
from __future__ import annotations

import json
import re
import sys

from .. import llm
from ..schema import ContactNote, Edge, Evidence, Fact, NoteField
from ..stores import REPO, EmailStore, MarkdownContactStore, MockExternalContextProvider
from ..verifier import Verifier

OUT_DIR = REPO / "backend/notes/contacts"
CJK = re.compile(r"[一-鿿]")

PROMPT = """You read emails that Mia SENT to one person and extract what she knows about her relationship with them.
Return ONLY a JSON object, no prose, with this shape:
{{"display_name": str, "relationship": str, "scenario": one of ["friend_scheduling","old_friend_catchup","zh_en_casual","vendor_service","refund_complaint","zh_formal"],
 "address_as": {{"value": str|null, "evidence": [{{"message_id": str, "quote": str}}]}},
 "honorific": {{"value": str|null, "evidence": [...]}},
 "sign_off": {{"value": str|null, "evidence": [...]}},
 "language": {{"value": "English"|"Chinese"|"Mixed", "evidence": [...]}},
 "facts": [{{"id": "short_snake_id", "text": str, "evidence": [...]}}],
 "edges": [{{"to": str, "type": str, "evidence": [...]}}]}}
Rules:
- address_as: the exact greeting phrase she uses for them (e.g. "Hi Ethan", "王老师您好", "Dear Kenji"); null if none.
- honorific: the polite second-person form if she uses one (e.g. "您"); null otherwise.
- sign_off: the exact closing line before her name (e.g. "Best,", "祝好，"); null if none.
- facts: at most 5 concrete, reusable facts about this person or what is between them.
- Every quote MUST be copied character-for-character from the body of the cited message. Keep quotes short (under 80 characters).

Emails to {name} <{email}>:
{emails}
"""


def parse_json(text: str) -> dict:
    m = re.search(r"\{.*\}", text, re.S)
    if not m:
        raise ValueError("model returned no JSON")
    return json.loads(m.group(0))


def count_support(value: str, kind: str, bodies: list[str]) -> int:
    if kind == "language":
        if value == "Chinese":
            return sum(1 for b in bodies if CJK.search(b))
        if value == "English":
            return sum(1 for b in bodies if not CJK.search(b))
        return len(bodies)
    return sum(1 for b in bodies if value in b)


def extract(address: str, emails: EmailStore, verifier: Verifier) -> tuple[ContactNote, list[str]]:
    mine = sorted(emails.to(address), key=lambda e: e.date)
    if not mine:
        raise SystemExit(f"no emails to {address}")
    name = mine[0].to_name or address
    listing = "\n\n".join(f"[message_id: {e.message_id}] date {e.date[:10]} subject {e.subject!r}\n{e.body}" for e in mine)
    raw = parse_json(llm.complete(PROMPT.format(name=name, email=address, emails=listing)))
    dropped: list[str] = []
    bodies = [e.body for e in mine]

    def keep(evs) -> list[Evidence]:
        out = []
        for ev in evs or []:
            e = Evidence(message_id=ev.get("message_id"), quote=ev.get("quote", ""))
            (out if verifier.check(e) else dropped).append(e if verifier.check(e) else f"{e.message_id}: {e.quote!r}")
        return out

    fields = {}
    for k in ("address_as", "honorific", "sign_off", "language"):
        f = raw.get(k) or {}
        evs = keep(f.get("evidence"))
        value = f.get("value") if evs else None  # no verified evidence -> fall back to scenario style
        fields[k] = NoteField(value=value, evidence=evs,
                              count=count_support(value, k, bodies) if value else 0, total=len(bodies))
    facts = []
    for f in raw.get("facts", []):
        evs = keep(f.get("evidence"))
        if evs:
            facts.append(Fact(id=f["id"], text=f["text"], evidence=evs))
    edges = [Edge(to=e["to"], type=e["type"], evidence=ev) for e in raw.get("edges", []) if (ev := keep(e.get("evidence")))]
    note = ContactNote(email=address, display_name=raw.get("display_name") or name, relationship=raw.get("relationship"),
                       scenario=raw.get("scenario"), facts=facts, edges=edges, **fields,
                       body=f"Extracted from {len(mine)} sent emails by app.pipeline.extract. Dropped quotes: {len(dropped)}.")
    return note, dropped


def main(addresses: list[str]) -> None:
    emails = EmailStore()
    store = MarkdownContactStore([OUT_DIR])
    for a in addresses:
        note, dropped = extract(a, emails, Verifier(emails, MockExternalContextProvider().get(a)))
        note.external = MockExternalContextProvider().get(a)
        store.save(note)
        print(f"{a}: {len(note.facts)} facts, address_as={note.address_as.value!r}, honorific={note.honorific.value!r}, "
              f"sign_off={note.sign_off.value!r}, language={note.language.value!r}; dropped {len(dropped)} quotes")
        for d in dropped:
            print("  dropped", d)


if __name__ == "__main__":
    main(sys.argv[1:])
