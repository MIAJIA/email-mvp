"""Prompt templates for the offline extraction calls. Every claim must carry verbatim quotes from Mia's own text."""

CONTACT_PROMPT = """You are building a relationship note about ONE recipient, from emails that Mia wrote to them.
Each email below has a message_id, the subject, the scenario, and BODY (what Mia wrote). Some also have
PREV (the message Mia replied to) for context only.

Return ONLY one JSON object, no prose, with this shape:
{{
  "display_name": "how this person is named, e.g. 王建华 or Ethan Park",
  "relationship": "one or two words, e.g. advisor, coach, colleague, hotel, friend",
  "core_connection": {{"text": "one or two sentences: the main bond between Mia and this person", "evidence": [Q]}},
  "address_as": [
    {{"context": "private | default | formal", "value": "the exact greeting name Mia uses, e.g. 王老师, 老唐, Ethan", "evidence": [Q]}}
  ],
  "honorific": {{"value": "uses_nin | no_nin | formal_only | n/a", "evidence": [Q]}},
  "sign_off": {{"value": "the exact closing Mia uses, e.g. 学生 Mia敬上 / Best, Mia", "evidence": [Q]}},
  "language": {{"value": "zh | en | mixed", "evidence": [Q]}},
  "facts": [{{"text": "a specific fact about this person or about Mia and them", "evidence": [Q]}}],
  "edges": [{{"to": "email address or person name", "type": "e.g. spouse, colleague, student_of", "evidence": [Q]}}]
}}
where Q = {{"message_id": "...", "quote": "..."}}.

Rules:
- Every "quote" MUST be copied character for character from the BODY of that message_id (not from PREV, not
  from the subject). Keep quotes short (3 to 40 characters) and do not paraphrase, translate or fix typos.
  Quotes that are not exact substrings will be deleted by code.
- For address_as / honorific / sign_off / language give one quote per email where the pattern appears
  (up to 8), so counts can be computed from them.
- address_as: one entry per context in which the greeting differs. "formal" = official mail or others in copy,
  "private" = an intimate nickname used only in casual personal mails (e.g. 老X, 小X, a pet name),
  "default" = the plain name used in ordinary mails. If Mia uses both a nickname and a plain name, the nickname
  is "private" and the plain name is "default"; never put two different names under the same context.
  Most people have only "default".
- honorific: "uses_nin" if Mia addresses them with 您, "no_nin" if Chinese without 您, "formal_only" if 您 only
  in formal mails, "n/a" for English-only. Quote the 您 sentence as evidence.
- facts: up to 10, concrete and useful for writing future emails (dates, plans, shared history, preferences).
- If something is unknown, use null for value and an empty evidence list. Do not invent.

Recipient: {email}
Emails ({n}):
{emails}
"""

SCENARIO_PROMPT = """You are describing how Mia usually writes emails in ONE scenario: "{scenario}".
Below are {n} emails Mia wrote in this scenario (BODY only).

Return ONLY one JSON object, no prose:
{{
  "habits": [
    {{"id": "short_snake_case_id", "description": "one sentence describing the habit (length, opening, closing,
      sign-off, tone, structure, typical phrasing)", "evidence": [{{"message_id": "...", "quote": "..."}}]}}
  ]
}}

Rules:
- 4 to 8 habits that recur across several emails. Prefer habits that a writer could copy (e.g. "opens with
  thanks", "offers two time windows", "signs off with 'Best, Mia'").
- For each habit give one quote per email where it appears (up to 10). Quotes MUST be copied character for
  character from that email's BODY, 3 to 40 characters, no paraphrase. Wrong quotes will be deleted by code.
- Do not describe content specific to one recipient.

Emails:
{emails}
"""


def format_email(e: dict, with_prev: bool = True, max_body: int = 1500) -> str:
    parts = [f"--- message_id: {e['message_id']} | date: {e.get('date')} | scenario: {e.get('category')}",
             f"subject: {e.get('subject') or ''}"]
    if with_prev and e.get("prev"):
        parts.append(f"PREV (from {e.get('prev_sender') or 'them'}, context only): {e['prev'][:600]}")
    parts.append(f"BODY:\n{(e.get('body') or '')[:max_body]}")
    return "\n".join(parts)
