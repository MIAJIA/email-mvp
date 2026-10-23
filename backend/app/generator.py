"""Online workflow: note + style + external -> prompt -> model text with <hl ref> tags -> segments + highlights.

The model only chooses refs. Label, rationale, strength, counts and evidence are all built here from the note.
"""
from __future__ import annotations

import re
import uuid
from dataclasses import dataclass
from typing import Callable, Optional

from .schema import ContactNote, Draft, DraftRequest, Evidence, ExternalItem, Highlight, Layer, Ref, ScenarioStyle, Segment

DEFAULT_SCENARIO = "vendor_service"
HL_RE = re.compile(r'<hl ref="([^"]*)">(.*?)</hl>', re.S)


def strength_of(count: Optional[int], total: Optional[int], status: str) -> str:
    if status == "confirmed":
        return "strong"
    if count is None:
        return "weak"
    if total:  # counted against all emails: at least 3 and more than 30%
        return "strong" if count >= 3 and count / total > 0.3 else "weak"
    return "strong" if count >= 2 else "weak"


@dataclass
class Entry:
    key: str            # what the model writes in ref="..."
    ref: Ref
    layer: Layer
    instruction: str    # what the model is told
    label: str
    rationale: str
    count: Optional[int]
    total: Optional[int]
    status: str
    evidence: list[Evidence]

    def highlight(self, hid: str) -> Highlight:
        return Highlight(
            id=hid, layer=self.layer, ref=self.ref, label=self.label, rationale=self.rationale,
            strength=strength_of(self.count, self.total, self.status),
            count=self.count, total=self.total, evidence=self.evidence[:3],
        )


def build_catalog(note: Optional[ContactNote], style: Optional[ScenarioStyle], external: list[ExternalItem]) -> dict[str, Entry]:
    cat: dict[str, Entry] = {}
    name = note.display_name if note else "this contact"
    if note:
        fields = {
            "address_as": ("Greet/address them as \"{v}\"", "Greeting: \"{v}\"", "You addressed {n} as \"{v}\" in {c} of {t} emails."),
            "honorific": ("Use the honorific form \"{v}\" (never the casual form)", "Formal \"{v}\"", "You used \"{v}\" with {n} in {c} of {t} emails."),
            "sign_off": ("Sign off with \"{v}\"", "Sign-off: \"{v}\"", "You signed off with \"{v}\" in {c} of {t} emails to {n}."),
            "language": ("Write the email in {v}", "Language: {v}", "{c} of {t} of your emails to {n} are in {v}."),
        }
        for k, (ins, lab, rat) in fields.items():
            f = getattr(note, k)
            if f.value is None or f.status == "rejected":
                continue  # falls back to the scenario style
            fmt = dict(v=f.value, n=name, c=f.count, t=f.total)
            cat[k] = Entry(k, Ref(kind=k, id=k), "person", ins.format(**fmt), lab.format(**fmt), rat.format(**fmt),
                           f.count, f.total, f.status, f.evidence)
        for a in note.address_as_by_context:
            if a.status == "rejected":
                continue
            cat[f"address_as:{a.context}"] = Entry(
                f"address_as:{a.context}", Ref(kind="address_as", id=a.context), "person",
                f"In a {a.context} setting, address them as \"{a.value}\"",
                f"Greeting ({a.context}): \"{a.value}\"",
                f"In {a.context} emails you called {name} \"{a.value}\" ({a.count} of {a.total} emails).",
                a.count, a.total, a.status, a.evidence)
        for fact in note.facts:
            if fact.status == "rejected":
                continue
            n_ev = len({e.message_id for e in fact.evidence})
            cat[f"fact:{fact.id}"] = Entry(
                f"fact:{fact.id}", Ref(kind="fact", id=fact.id), "person", f"Known fact you may use: {fact.text}",
                f"What you know: {fact.text}", f"From {n_ev} of your emails with {name}.",
                n_ev, None, fact.status, fact.evidence)
    if style:
        for h in style.habits:
            if h.status == "rejected":
                continue
            cat[f"habit:{h.id}"] = Entry(
                f"habit:{h.id}", Ref(kind="habit", id=h.id), "scenario", f"Your usual habit: {h.description}",
                h.description, f"In your {style.scenario} emails, {h.count} of {h.total} do this.",
                h.count, h.total, h.status, h.evidence)
    for x in external:
        cat[f"external:{x.id}"] = Entry(
            f"external:{x.id}", Ref(kind="external", id=x.id), "external", f"Recent context ({x.source_label}, {x.date}): {x.text}",
            f"Recent context: {x.source_label}", f"Mock {x.source_label} item from {x.date}, not from your emails.",
            None, None, "confirmed", [Evidence(external_id=x.id, quote=x.text)])
    return cat


def build_prompt(req: DraftRequest, note: Optional[ContactNote], scenario: str, cat: dict[str, Entry]) -> str:
    who = f"{note.display_name} <{note.email}>" if note else req.to
    lines = "\n".join(f'- ref="{e.key}": {e.instruction}' for e in cat.values()) or "- (no notes)"
    return f"""You write one email for Mia (the sender) to {who}. Scenario: {scenario}.
What Mia wants to say: {req.brief}

Notes about Mia's relationship with this person and her style. Person notes override scenario habits.
If several greetings are listed for different settings, pick the one that fits what Mia wants to say.
{lines}

Rules:
- Wherever your wording applies one of the notes above, wrap exactly those words in <hl ref="KEY">...</hl> using a KEY from the list. Wrap the greeting, honorific word, sign-off, and any sentence that uses a fact or recent context.
- Use only KEYs from the list. Do not invent keys. Do not nest tags.
- Plain text only: no Markdown (no **bold**, no headings).
- Output format, nothing else: first line `Subject: ...`, then a blank line, then the email body.
"""


def parse(text: str, cat: dict[str, Entry]) -> tuple[str, list[Segment], list[Highlight], list[str]]:
    subject = ""
    m = re.match(r"\s*Subject:\s*(.*)\n", text)
    if m:
        subject, text = m.group(1).strip(), text[m.end():]
    text = text.strip("\n")
    segments: list[Segment] = []
    highlights: list[Highlight] = []
    warnings: list[str] = []
    pos = 0
    for m in HL_RE.finditer(text):
        if m.start() > pos:
            segments.append(Segment(text=text[pos:m.start()]))
        key, inner = m.group(1), m.group(2)
        entry = cat.get(key)
        if entry is None:
            warnings.append(f'The model cited a note that does not exist ("{key}"); that text is shown without a highlight.')
            segments.append(Segment(text=inner))
        else:
            hid = f"h{len(highlights) + 1}"
            highlights.append(entry.highlight(hid))
            segments.append(Segment(text=inner, highlight_id=hid))
        pos = m.end()
    if pos < len(text):
        segments.append(Segment(text=text[pos:]))
    # Stray or unclosed tags never reach the user as markup.
    for s in segments:
        s.text = re.sub(r"</?hl[^>]*>", "", s.text).replace("**", "")
    return subject, segments, highlights, warnings


def inject_unknown_ref(raw: str) -> str:
    """Rename the second <hl> tag (the first if there is only one) to a ref no note has."""
    tags = list(HL_RE.finditer(raw))
    if not tags:
        return raw
    m = tags[1] if len(tags) > 1 else tags[0]
    return raw[:m.start(1)] + "fact:injected_unknown" + raw[m.end(1):]


def generate(req: DraftRequest, note: Optional[ContactNote], style: Optional[ScenarioStyle],
             external: list[ExternalItem], complete: Callable[[str], str]) -> Draft:
    scenario = (note.scenario if note and note.scenario else None) or (style.scenario if style else DEFAULT_SCENARIO)
    cat = build_catalog(note, style, external)
    raw = complete(build_prompt(req, note, scenario, cat))
    if req.inject == "unknown_ref":
        raw = inject_unknown_ref(raw)
    subject, segments, highlights, warnings = parse(raw, cat)
    if note is None:
        warnings.append("No contact note for this address; used your scenario style only.")
    return Draft(draft_id=uuid.uuid4().hex[:12], to=req.to, scenario=scenario, subject=subject,
                 segments=segments, highlights=highlights, warnings=warnings)
