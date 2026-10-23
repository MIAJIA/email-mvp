"""Contract code layer (CONTRACT.md revision 0.2). frontend/src/types.ts mirrors this file."""
from __future__ import annotations

from typing import Literal, Optional

from pydantic import BaseModel, Field

CONTRACT_REVISION = "0.2"

EntryStatus = Literal["learned", "confirmed", "rejected"]
Layer = Literal["person", "scenario", "external", "inferred"]
RefKind = Literal["address_as", "honorific", "sign_off", "language", "fact", "habit", "external"]
Strength = Literal["strong", "weak"]


class Evidence(BaseModel):
    message_id: Optional[str] = None
    external_id: Optional[str] = None
    quote: str


class Email(BaseModel):
    thread_id: str
    message_id: str
    date: str
    to: str
    to_name: Optional[str] = None
    subject: Optional[str] = None
    body: str
    prev: Optional[str] = None
    prev_sender: Optional[str] = None
    category: Optional[str] = None
    source: Optional[str] = None


class NoteField(BaseModel):
    """address_as / honorific / sign_off / language. value=None means fall back to the scenario style."""
    value: Optional[str] = None
    count: int = 0
    total: int = 0
    status: EntryStatus = "learned"
    evidence: list[Evidence] = Field(default_factory=list)


class Fact(BaseModel):
    id: str
    text: str
    status: EntryStatus = "learned"
    evidence: list[Evidence] = Field(default_factory=list)


class Edge(BaseModel):
    to: str
    type: str
    evidence: list[Evidence] = Field(default_factory=list)


class ExternalItem(BaseModel):
    id: str
    text: str
    source_label: str
    date: str


class ContactNote(BaseModel):
    email: str
    display_name: str
    relationship: Optional[str] = None
    scenario: Optional[str] = None
    address_as: NoteField = Field(default_factory=NoteField)
    honorific: NoteField = Field(default_factory=NoteField)
    sign_off: NoteField = Field(default_factory=NoteField)
    language: NoteField = Field(default_factory=NoteField)
    facts: list[Fact] = Field(default_factory=list)
    edges: list[Edge] = Field(default_factory=list)
    external: list[ExternalItem] = Field(default_factory=list)
    body: str = ""  # free-form Markdown below the frontmatter


class Habit(BaseModel):
    id: str
    description: str
    count: int
    total: int
    status: EntryStatus = "learned"
    evidence: list[Evidence] = Field(default_factory=list)


class ScenarioStyle(BaseModel):
    scenario: str
    habits: list[Habit] = Field(default_factory=list)


class Ref(BaseModel):
    kind: RefKind
    id: str


class Highlight(BaseModel):
    id: str
    layer: Layer
    ref: Optional[Ref] = None
    strength: Strength
    label: str
    rationale: str
    count: Optional[int] = None
    total: Optional[int] = None
    evidence: list[Evidence] = Field(default_factory=list)


class Segment(BaseModel):
    text: str
    highlight_id: Optional[str] = None


class Draft(BaseModel):
    draft_id: str
    to: str
    scenario: str
    subject: str
    segments: list[Segment]
    highlights: list[Highlight]
    warnings: list[str] = Field(default_factory=list)


class ContactSummary(BaseModel):
    email: str
    display_name: str
    relationship: Optional[str] = None


class DraftRequest(BaseModel):
    mode: Literal["compose", "reply"] = "compose"
    to: str
    thread_id: Optional[str] = None
    brief: str
    # Demo-only: "unknown_ref" rewrites one model tag to a ref that does not exist, to show the fallback.
    inject: Optional[Literal["unknown_ref"]] = None


class FeedbackRequest(BaseModel):
    draft_id: str
    highlight_id: str
    action: Literal["accept", "reject"]
    correction: Optional[str] = None


class FeedbackResponse(BaseModel):
    email: str
    ref: Ref
    status: EntryStatus
