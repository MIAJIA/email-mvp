import { useEffect, useState } from "react";
import { errorText, getContact } from "../api";
import type { ContactNote, ContactSummary, EntryStatus, Evidence } from "../types";
import { Quote } from "./HighlightCard";

const STATUS: Record<EntryStatus, string> = { learned: "Learned", confirmed: "You confirmed", rejected: "Rejected" };
const CONTEXT: Record<string, string> = { private: "In private", default: "Usually", formal: "Formally" };

interface Row { key: string; title: string; value: string; sub: string; status?: EntryStatus; evidence: Evidence[] }

function Entry({ row, open, onToggle }: { row: Row; open: boolean; onToggle: () => void }) {
  return (
    <div className={`entry${open ? " open" : ""}`}>
      <button type="button" className="e-head" aria-expanded={open} onClick={onToggle}>
        <span className="e-val">{row.value}</span>
        {row.status && <span className={`tag ${row.status}`}>{STATUS[row.status]}</span>}
        <span className="e-sub">{row.title}{row.sub ? ` · ${row.sub}` : ""}</span>
      </button>
      <div className="e-body"><div><div className="e-inner">
        {row.evidence.length ? <ul className="ev">{row.evidence.map((ev, i) => <Quote key={i} ev={ev} />)}</ul>
          : <p className="why">No source email.</p>}
      </div></div></div>
    </div>
  );
}

const emails = (n: number) => `${n} email${n === 1 ? "" : "s"}`;

// Read-only view of a contact note (GET /contacts/{email}). Editing entries needs a contract change
// (there is no endpoint for note entries outside a draft), see email-highlight-research/frontend-spec.md.
export default function ContactsPage({ contacts }: { contacts: ContactSummary[] }) {
  const [sel, setSel] = useState(contacts[0]?.email ?? "");
  const [note, setNote] = useState<ContactNote | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [open, setOpen] = useState<string | null>(null);

  useEffect(() => {
    if (!sel) return;
    setNote(null); setError(null); setOpen(null);
    getContact(sel).then(setNote, (e) => setError(`Could not load this note: ${errorText(e)}`));
  }, [sel]);

  const rows = (n: ContactNote): Row[] => {
    const out: Row[] = [];
    if (n.address_as_by_context?.length) {
      for (const a of n.address_as_by_context) if (a.value)
        out.push({ key: `addr-${a.context}`, title: `How you address them · ${CONTEXT[a.context] ?? a.context}`, value: a.value, sub: `${a.count} / ${a.total}`, status: a.status, evidence: a.evidence });
    } else if (n.address_as.value) {
      out.push({ key: "address_as", title: "How you address them", value: n.address_as.value, sub: `${n.address_as.count} / ${n.address_as.total}`, status: n.address_as.status, evidence: n.address_as.evidence });
    }
    for (const [key, title] of [["honorific", "Honorific"], ["sign_off", "Sign-off"], ["language", "Language"]] as const) {
      const f = n[key];
      if (f.value) out.push({ key, title, value: f.value, sub: `${f.count} / ${f.total}`, status: f.status, evidence: f.evidence });
    }
    return out;
  };
  const toggle = (k: string) => setOpen((o) => (o === k ? null : k));

  return (
    <>
      {contacts.length > 8 ? (
        <select className="contact-select" aria-label="Contact" value={sel} onChange={(e) => setSel(e.target.value)}>
          {contacts.map((c) => <option key={c.email} value={c.email}>{c.display_name}</option>)}
        </select>
      ) : (
        <div className="contacts" role="group" aria-label="Contacts">
          {contacts.map((c) => (
            <button key={c.email} type="button" className="chip" aria-pressed={c.email === sel} onClick={() => setSel(c.email)}>{c.display_name}</button>
          ))}
        </div>
      )}
      <section className="surface note" aria-label="Contact note">
        {error && <p className="error pad">{error}</p>}
        {!note && !error && <p className="muted pad">Loading…</p>}
        {note && (
          <>
            <div className="note-head">
              <h2>{note.display_name}</h2>
              <span className="muted">{note.email}</span>
              {note.relationship && <span>{note.relationship}</span>}
            </div>
            <div className="sec"><h3>How you write to them</h3>
              {rows(note).map((r) => <Entry key={r.key} row={r} open={open === r.key} onToggle={() => toggle(r.key)} />)}
            </div>
            {note.facts.length > 0 && (
              <div className="sec"><h3>What you know</h3>
                {note.facts.map((f) => <Entry key={f.id} row={{ key: f.id, title: "Fact", value: f.text, sub: emails(f.evidence.length), status: f.status, evidence: f.evidence }} open={open === f.id} onToggle={() => toggle(f.id)} />)}
              </div>
            )}
            {note.external.length > 0 && (
              <div className="sec"><h3>Recent context</h3>
                {note.external.map((x) => <Entry key={x.id} row={{ key: x.id, title: x.source_label, value: x.text, sub: x.date, evidence: [] }} open={open === x.id} onToggle={() => toggle(x.id)} />)}
              </div>
            )}
            {note.edges.length > 0 && (
              <div className="sec"><h3>Connections</h3>
                {note.edges.map((x, i) => <Entry key={`e${i}`} row={{ key: `e${i}`, title: x.type, value: x.to, sub: "", evidence: x.evidence }} open={open === `e${i}`} onToggle={() => toggle(`e${i}`)} />)}
              </div>
            )}
          </>
        )}
      </section>
    </>
  );
}
