"""Score the extracted contact notes against data/ground_truth/people.json (evaluation only; the pipeline itself
never reads ground truth).

Metrics:
- address accuracy: per ground-truth (person, context) entry, hit if the note has the same context with the same
  greeting value (whitespace and trailing punctuation ignored).
- honorific accuracy: per person, whether the note's 您 / 你 / formal-only value matches `uses_nin`
  (an English-only contact with no honorific field counts as correct when uses_nin is false).
- fact recall: per ground-truth fact, recalled if some extracted fact cites the same message with an
  overlapping quote (longest common substring >= 6 chars, or the shorter quote in full).

Usage: python3 pipeline/evaluate.py   -> writes pipeline/out/eval.md
"""
from __future__ import annotations

import json
import re
import sys
from difflib import SequenceMatcher
from pathlib import Path

try:
    import yaml
except ImportError:  # verify.py falls back to JSON frontmatter, which json can read
    yaml = None

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import DATA, OUT, safe_name  # noqa: E402

FOCUS = ["wang.jianhua@example.com", "tang.shuyuan@example.com", "zhao.liqun@example.com", "ethan.park@example.com"]


def norm(s: str | None) -> str:
    return re.sub(r"[\s,:：，。!！]+$", "", re.sub(r"\s+", "", s or ""))


def load_note(email: str) -> dict | None:
    path = OUT / "contacts" / f"{safe_name(email)}.md"
    if not path.exists():
        return None
    text = path.read_text(encoding="utf-8")
    head = text.split("---", 2)[1]
    return yaml.safe_load(head) if yaml else json.loads(head)


def quotes_overlap(a: str, b: str) -> bool:
    if not a or not b:
        return False
    m = SequenceMatcher(None, a, b).find_longest_match(0, len(a), 0, len(b))
    return m.size >= min(6, len(a), len(b))


def expected_honorific(uses_nin) -> str | None:
    return {True: "您", False: None, "formal_only": "您 (formal only)"}.get(uses_nin)


def main() -> None:
    people = json.loads((DATA / "ground_truth" / "people.json").read_text(encoding="utf-8"))["people"]
    rows, addr_hit, addr_n, hon_hit, hon_n, fact_hit, fact_n = [], 0, 0, 0, 0, 0, 0
    missed_facts: list[str] = []
    for p in people:
        note = load_note(p["email"]) or {}
        # address
        got = {}
        for a in note.get("address_as_by_context") or []:
            got.setdefault(a.get("context"), set()).add(norm(a.get("value")))
        a_hits = 0
        for a in p.get("address_as") or []:
            addr_n += 1
            if norm(a["value"]) in got.get(a["context"], set()):
                addr_hit += 1
                a_hits += 1
        # honorific
        exp = expected_honorific((p.get("honorific") or {}).get("uses_nin"))
        have = (note.get("honorific") or {}).get("value")
        hon_ok = (have == exp) or (exp is None and have in (None, "你"))
        hon_n += 1
        hon_hit += hon_ok
        # facts
        extracted = [ev for f in note.get("facts") or [] for ev in f.get("evidence") or []]
        f_hits = 0
        for f in p.get("facts") or []:
            fact_n += 1
            ok = any(ev["message_id"] == g["message_id"] and quotes_overlap(ev["quote"], g["quote"])
                     for g in f.get("evidence") or [] for ev in extracted)
            f_hits += ok
            if not ok and p["email"] in FOCUS:
                missed_facts.append(f"{p['display_name']}: {f['text']}")
        fact_hit += f_hits
        rows.append((p, note, a_hits, len(p.get("address_as") or []), exp, have, hon_ok, f_hits,
                     len(p.get("facts") or [])))

    def pct(a, b):
        return f"{a}/{b} = {100 * a / b:.0f}%" if b else "n/a"

    out = ["# Offline extraction vs ground truth", "",
           f"People in ground truth: {len(people)}; notes found: {sum(1 for r in rows if r[1])}.", "",
           "| Metric | Score |", "|---|---|",
           f"| Address accuracy (per person x context) | {pct(addr_hit, addr_n)} |",
           f"| Honorific accuracy (per person) | {pct(hon_hit, hon_n)} |",
           f"| Fact recall | {pct(fact_hit, fact_n)} |", "",
           "| Person | Address (expected -> got) | Honorific (expected -> got) | Facts recalled |",
           "|---|---|---|---|"]
    rows.sort(key=lambda r: (r[0]["email"] not in FOCUS, r[0]["email"]))
    for p, note, ah, an, exp, have, hon_ok, fh, fn in rows:
        exp_a = ", ".join(f"{a['context']}:{a['value']}" for a in p.get("address_as") or [])
        got_a = ", ".join(f"{a['context']}:{a['value']}" for a in note.get("address_as_by_context") or []) or "-"
        mark = "**" if p["email"] in FOCUS else ""
        out.append(f"| {mark}{p['display_name']}{mark} | {exp_a} -> {got_a} ({ah}/{an}) | "
                   f"{exp or '-'} -> {have or '-'} ({'ok' if hon_ok else 'wrong'}) | {fh}/{fn} |")
    if missed_facts:
        out += ["", "Facts missed for the focus people:", ""] + [f"- {m}" for m in missed_facts]
    (OUT / "eval.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    print("\n".join(out))


if __name__ == "__main__":
    main()
