"""Seams later lines code against: EmailStore, ContactStore, StyleStore, ExternalContextProvider."""
from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Optional, Protocol

import yaml

from .schema import ContactNote, ContactSummary, Email, ExternalItem, ScenarioStyle

REPO = Path(__file__).resolve().parents[2]
DEFAULT_EMAILS = Path("/Users/mia/Downloads/mia星辰大海/email-style-demo/data/emails.jsonl")
EMAIL_SOURCES = [Path(os.environ.get("EMAILS_PATH", DEFAULT_EMAILS)), REPO / "fixtures/emails/handwritten.jsonl"]
# Extracted notes win over hand-written ones for the same email address.
CONTACT_DIRS = [REPO / "fixtures/notes/contacts", REPO / "backend/notes/contacts"]
STYLE_DIR = REPO / "backend/notes/styles"
EXTERNAL_FILE = REPO / "fixtures/external/mock_external.json"


class EmailStore:
    def __init__(self, sources: list[Path] = EMAIL_SOURCES):
        self.by_id: dict[str, Email] = {}
        for src in sources:
            if not src.exists():
                continue
            for line in src.read_text().splitlines():
                if line.strip():
                    e = Email(**json.loads(line))
                    self.by_id[e.message_id] = e

    def get(self, message_id: str) -> Optional[Email]:
        return self.by_id.get(message_id)

    def to(self, address: str) -> list[Email]:
        return [e for e in self.by_id.values() if e.to == address]


class ContactStore(Protocol):
    def list(self) -> list[ContactSummary]: ...
    def get(self, email: str) -> Optional[ContactNote]: ...
    def save(self, note: ContactNote) -> None: ...


def parse_note(text: str) -> ContactNote:
    _, front, body = text.split("---\n", 2)
    data = yaml.safe_load(front)
    return ContactNote(**data, body=body.strip())


def render_note(note: ContactNote) -> str:
    data = note.model_dump(exclude={"body"}, exclude_none=True)
    front = yaml.safe_dump(data, allow_unicode=True, sort_keys=False, width=1000)
    return f"---\n{front}---\n{note.body}\n"


class MarkdownContactStore:
    """One `<email>.md` per contact: YAML frontmatter (structured entries) + free Markdown body."""

    def __init__(self, dirs: list[Path] = CONTACT_DIRS):
        self.dirs = dirs

    def _path(self, email: str) -> Optional[Path]:
        found = None
        for d in self.dirs:
            p = d / f"{email}.md"
            if p.exists():
                found = p
        return found

    def list(self) -> list[ContactSummary]:
        seen: dict[str, ContactSummary] = {}
        for d in self.dirs:
            for p in sorted(d.glob("*.md")):
                n = parse_note(p.read_text())
                seen[n.email] = ContactSummary(email=n.email, display_name=n.display_name, relationship=n.relationship)
        return list(seen.values())

    def get(self, email: str) -> Optional[ContactNote]:
        p = self._path(email)
        return parse_note(p.read_text()) if p else None

    def save(self, note: ContactNote) -> None:
        p = self._path(note.email) or (self.dirs[-1] / f"{note.email}.md")
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(render_note(note))


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
        return [ExternalItem(**x) for x in self.data.get(email, [])]
