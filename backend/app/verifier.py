"""Every quote must be a verbatim substring of its source; anything else is dropped before it is stored."""
from __future__ import annotations

from .schema import ContactNote, Evidence, ExternalItem
from .stores import EmailStore


class Verifier:
    def __init__(self, emails: EmailStore, external: list[ExternalItem] | None = None):
        self.emails = emails
        self.external = {x.id: x for x in (external or [])}

    def check(self, ev: Evidence) -> bool:
        if not ev.quote.strip():
            return False
        if ev.message_id:
            e = self.emails.get(ev.message_id)
            return e is not None and ev.quote in e.body
        if ev.external_id:
            x = self.external.get(ev.external_id)
            return x is not None and ev.quote in x.text
        return False

    def filter(self, evs: list[Evidence]) -> list[Evidence]:
        return [ev for ev in evs if self.check(ev)]

    def failures(self, note: ContactNote) -> list[str]:
        """List every evidence entry in a note that does not verify (used by tests and check.sh)."""
        bad = []
        for name in ("address_as", "honorific", "sign_off", "language"):
            for ev in getattr(note, name).evidence:
                if not self.check(ev):
                    bad.append(f"{note.email} {name}: {ev.message_id} {ev.quote!r}")
        for f in note.facts:
            for ev in f.evidence:
                if not self.check(ev):
                    bad.append(f"{note.email} fact {f.id}: {ev.message_id} {ev.quote!r}")
        return bad
