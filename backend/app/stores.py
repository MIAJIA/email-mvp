"""Seams later lines code against: EmailStore, ContactStore, StyleStore, ExternalContextProvider."""
from __future__ import annotations

import json
import os
from collections import Counter
from pathlib import Path
from typing import Optional, Protocol

import yaml

from .schema import ContactNote, ContactSummary, Email, ExternalItem, ScenarioStyle

REPO = Path(__file__).resolve().parents[2]
# Real data from the main line, overridable for tests or another checkout. Nothing is copied.
EMAILS_DIR = Path(os.environ.get("EMAILS_DIR", REPO / "data/emails"))
CONTACTS_DIR = Path(os.environ.get("CONTACTS_DIR", REPO / "pipeline/out/contacts"))
STYLE_DIR = Path(os.environ.get("STYLES_DIR", REPO / "pipeline/out/styles"))
EXTERNAL_FILE = Path(os.environ.get("EXTERNAL_FILE", REPO / "data/external.json"))
# Accept/reject results live here, so the extraction line's output files are never rewritten.
STATUS_FILE = Path(os.environ.get("STATUS_FILE", REPO / "backend/state/status.json"))


class EmailStore:
    def __init__(self, dir: Path = EMAILS_DIR):
        self.by_id: dict[str, Email] = {}
        for src in sorted(dir.glob("*.jsonl")):
            for line in src.read_text().splitlines():
                if line.strip():
                    e = Email(**json.loads(line))
                    self.by_id[e.message_id] = e

    def get(self, message_id: str) -> Optional[Email]:
        return self.by_id.get(message_id)

    def to(self, address: str) -> list[Email]:
        return [e for e in self.by_id.values() if e.to == address]

    def scenario_for(self, address: str) -> Optional[str]:
        """Most common category of the emails you sent this person."""
        cats = Counter(e.category for e in self.to(address) if e.category)
        return cats.most_common(1)[0][0] if cats else None


class ContactStore(Protocol):
    def list(self) -> list[ContactSummary]: ...
    def get(self, email: str) -> Optional[ContactNote]: ...
    def set_status(self, email: str, key: str, status: str) -> None: ...


def parse_note(text: str) -> ContactNote:
    _, front, body = text.split("---\n", 2)
    data = yaml.safe_load(front)  # YAML is a superset of JSON, so both frontmatter styles parse
    return ContactNote(**data, body=body.strip())


class MarkdownContactStore:
    """One `<email>.md` per contact: frontmatter (YAML or JSON) + free Markdown body.

    Notes are read-only here; entry statuses from /feedback are kept in a separate overlay file.
    """

    def __init__(self, dir: Path = CONTACTS_DIR, status_file: Path = STATUS_FILE):
        self.dir = dir
        self.status_file = status_file

    def _overlay(self) -> dict:
        return json.loads(self.status_file.read_text()) if self.status_file.exists() else {}

    def list(self) -> list[ContactSummary]:
        out = []
        for p in sorted(self.dir.glob("*.md")):
            n = parse_note(p.read_text())
            out.append(ContactSummary(email=n.email, display_name=n.display_name, relationship=n.relationship))
        return out

    def get(self, email: str) -> Optional[ContactNote]:
        p = self.dir / f"{email}.md"
        if not p.exists():
            return None
        note = parse_note(p.read_text())
        for key, status in self._overlay().get(email, {}).items():
            set_status(note, key, status)
        return note

    def set_status(self, email: str, key: str, status: str) -> None:
        data = self._overlay()
        data.setdefault(email, {})[key] = status
        self.status_file.parent.mkdir(parents=True, exist_ok=True)
        self.status_file.write_text(json.dumps(data, ensure_ascii=False, indent=2))


def set_status(note: ContactNote, key: str, status: str) -> None:
    """key is `<kind>:<id>` as in Ref: address_as:address_as, address_as:formal, fact:f1, honorific:honorific ..."""
    kind, _, id = key.partition(":")
    if kind == "fact":
        for f in note.facts:
            if f.id == id:
                f.status = status
    elif kind == "address_as" and id != "address_as":
        for a in note.address_as_by_context:
            if a.context == id:
                a.status = status
    elif kind in ("address_as", "honorific", "sign_off", "language"):
        getattr(note, kind).status = status


class StyleStore:
    def __init__(self, dir: Path = STYLE_DIR):
        self.dir = dir

    def get(self, scenario: str) -> Optional[ScenarioStyle]:
        p = self.dir / f"{scenario}.json"
        return ScenarioStyle(**json.loads(p.read_text())) if p.exists() else None


class ExternalContextProvider(Protocol):
    def get(self, email: str) -> list[ExternalItem]: ...


class MockExternalContextProvider:
    """Mock data only; no real fetching (DECISIONS 13:58)."""

    def __init__(self, path: Path = EXTERNAL_FILE):
        self.data = json.loads(path.read_text()) if path.exists() else {}

    def get(self, email: str) -> list[ExternalItem]:
        items = self.data.get(email, [])
        return [ExternalItem(**x) for x in items] if isinstance(items, list) else []
