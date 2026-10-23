"""Verify raw model extractions against the email bodies and write the final notes.

Every evidence quote must be a substring of the `body` of the email it cites (and, for contact notes, that email
must be addressed to this contact). Failing evidence is dropped; a field or fact with no evidence left is not
written. counts are computed here from verified evidence, never taken from the model.

Usage: python3 pipeline/verify.py   (re-verifies pipeline/out/raw/ without any model call)
"""
from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import OUT, RAW, load_emails, load_external, norm_email, safe_name  # noqa: E402

try:
    import yaml
except ImportError:  # JSON is valid YAML, so the frontmatter stays readable by yaml.safe_load
    yaml = None

HONORIFIC_VALUES = {"uses_nin": "您", "no_nin": "你", "formal_only": "您 (formal only)"}


class Stats:
    def __init__(self):
        self.c = Counter()

    def add(self, key, n=1):
        self.c[key] += n


def check_evidence(evidence, by_id, allowed_ids, stats: Stats) -> list[dict]:
    kept, seen = [], set()
    for ev in evidence or []:
        if not isinstance(ev, dict):
            stats.add("evidence_dropped")
            continue
        mid, quote = ev.get("message_id"), (ev.get("quote") or "")
        stats.add("evidence_total")
        email = by_id.get(mid)
        ok = (email is not None and quote.strip() and mid in allowed_ids and quote in (email.get("body") or ""))
        if not ok:
            stats.add("evidence_dropped")
            continue
        if (mid, quote) in seen:
            continue
        seen.add((mid, quote))
        kept.append({"message_id": mid, "quote": quote})
    return kept


def note_field(value, evidence, total) -> dict:
    return {"value": value, "count": len({e["message_id"] for e in evidence}), "total": total,
            "status": "learned", "evidence": evidence}


def build_contact(raw: dict, by_id: dict, external: dict, stats: Stats) -> dict | None:
    email = raw["email"]
    allowed = set(raw["message_ids"])
    total = len(allowed)
    data = raw.get("extraction") or {}
    fm: dict = {"email": email, "display_name": data.get("display_name") or raw.get("to_name") or email}
    if data.get("relationship"):
        fm["relationship"] = data["relationship"]

    def field(key, value, evidence):
        stats.add("fields_total")
        ev = check_evidence(evidence, by_id, allowed, stats)
        if value in (None, "", "n/a") or not ev:
            stats.add("fields_dropped")
            return None
        return note_field(value, ev, total)

    by_context = []
    for item in data.get("address_as") or []:
        f = field("address_as", item.get("value"), item.get("evidence"))
        if f:
            by_context.append({"context": item.get("context") or "default", **f})
    if by_context:
        default = next((a for a in by_context if a["context"] == "default"), None)
        default = default or max(by_context, key=lambda a: a["count"])
        fm["address_as"] = {k: default[k] for k in ("value", "count", "total", "status", "evidence")}
        fm["address_as_by_context"] = by_context

    for key in ("honorific", "sign_off", "language"):
        item = data.get(key) or {}
        value = item.get("value")
        if key == "honorific":
            value = HONORIFIC_VALUES.get(value)
        f = field(key, value, item.get("evidence"))
        if f:
            fm[key] = f

    facts = []
    for item in data.get("facts") or []:
        stats.add("facts_total")
        ev = check_evidence(item.get("evidence"), by_id, allowed, stats)
        if not ev or not item.get("text"):
            stats.add("facts_dropped")
            continue
        facts.append({"id": f"f{len(facts) + 1}", "text": item["text"], "status": "learned", "evidence": ev})
    fm["facts"] = facts

    edges = []
    for item in data.get("edges") or []:
        stats.add("edges_total")
        ev = check_evidence(item.get("evidence"), by_id, allowed, stats)
        if not ev or not item.get("to") or not item.get("type"):
            stats.add("edges_dropped")
            continue
        edges.append({"to": item["to"], "type": item["type"], "evidence": ev})
    fm["edges"] = edges

    cc = data.get("core_connection") or {}
    stats.add("fields_total")
    cc_ev = check_evidence(cc.get("evidence"), by_id, allowed, stats)
    if cc.get("text") and cc_ev:
        fm["core_connection"] = {"text": cc["text"], "evidence": cc_ev}
    else:
        stats.add("fields_dropped")

    fm["external"] = [{k: x.get(k) for k in ("id", "text", "source_label", "date")}
                      for x in external.get(email, [])]
    return fm


def render_markdown(fm: dict) -> str:
    if yaml:
        head = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False, width=1000)
    else:
        head = json.dumps(fm, ensure_ascii=False, indent=2) + "\n"
    lines = [f"# {fm['display_name']}", ""]
    if fm.get("core_connection"):
        lines += [fm["core_connection"]["text"], ""]
    for a in fm.get("address_as_by_context", []):
        lines.append(f"- Address ({a['context']}): {a['value']} ({a['count']}/{a['total']} emails)")
    for f in fm.get("facts", []):
        lines.append(f"- {f['text']}")
    lines.append("")
    lines.append("_Extracted offline by pipeline/extract.py; every entry is backed by verified quotes._")
    return f"---\n{head}---\n\n" + "\n".join(lines) + "\n"


def build_style(raw: dict, by_id: dict, stats: Stats) -> dict:
    allowed = set(raw["message_ids"])
    total = len(allowed)
    habits = []
    for item in (raw.get("extraction") or {}).get("habits") or []:
        stats.add("habits_total")
        ev = check_evidence(item.get("evidence"), by_id, allowed, stats)
        if not ev or not item.get("description"):
            stats.add("habits_dropped")
            continue
        habits.append({"id": item.get("id") or f"h{len(habits) + 1}", "description": item["description"],
                       "count": len({e["message_id"] for e in ev}), "total": total,
                       "status": "learned", "evidence": ev})
    return {"scenario": raw["scenario"], "habits": habits}


def build_all() -> Counter:
    emails = load_emails()
    by_id = {e["message_id"]: e for e in emails}
    external = {norm_email(k): v for k, v in load_external().items()}
    stats = Stats()
    (OUT / "contacts").mkdir(parents=True, exist_ok=True)
    (OUT / "styles").mkdir(parents=True, exist_ok=True)

    for path in sorted((RAW / "contacts").glob("*.json")):
        raw = json.loads(path.read_text(encoding="utf-8"))
        fm = build_contact(raw, by_id, external, stats)
        stats.add("notes_written")
        (OUT / "contacts" / f"{safe_name(raw['email'])}.md").write_text(render_markdown(fm), encoding="utf-8")

    for path in sorted((RAW / "styles").glob("*.json")):
        raw = json.loads(path.read_text(encoding="utf-8"))
        style = build_style(raw, by_id, stats)
        stats.add("styles_written")
        (OUT / "styles" / f"{safe_name(raw['scenario'])}.json").write_text(
            json.dumps(style, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    c = stats.c
    report = [
        "# Verification report", "",
        f"- Contact notes written: {c['notes_written']}",
        f"- Scenario styles written: {c['styles_written']}",
        f"- Evidence quotes checked: {c['evidence_total']}, dropped (not a verbatim substring of the cited body): "
        f"{c['evidence_dropped']}",
        f"- Note fields dropped for lack of evidence: {c['fields_dropped']} of {c['fields_total']}",
        f"- Facts dropped: {c['facts_dropped']} of {c['facts_total']}",
        f"- Edges dropped: {c['edges_dropped']} of {c['edges_total']}",
        f"- Habits dropped: {c['habits_dropped']} of {c['habits_total']}",
    ]
    (OUT / "verify_report.md").write_text("\n".join(report) + "\n", encoding="utf-8")
    print("\n".join(report))
    return c


if __name__ == "__main__":
    build_all()
