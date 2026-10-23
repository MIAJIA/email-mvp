import { useEffect, useRef, useState } from "react";
import { createDraft, errorText, getContacts, sendFeedback } from "./api";
import DraftBody, { type Mark } from "./components/DraftBody";
import HighlightCard from "./components/HighlightCard";
import { DEMO_ORDER, EXAMPLE_BRIEFS } from "./examples";
import type { ContactSummary, Draft } from "./types";

interface Active { id: string; el: HTMLElement; open: boolean }

export default function App() {
  const [contacts, setContacts] = useState<ContactSummary[]>([]);
  const [to, setTo] = useState("");
  const [brief, setBrief] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [draft, setDraft] = useState<Draft | null>(null);
  const [subject, setSubject] = useState("");
  const [marks, setMarks] = useState<Record<string, Mark>>({});
  const [edits, setEdits] = useState<Record<string, string>>({});
  const [active, setActive] = useState<Active | null>(null);
  const [busy, setBusy] = useState(false);
  const [cardError, setCardError] = useState<string | null>(null);
  const [toast, setToast] = useState<string | null>(null);
  const closeTimer = useRef<number | undefined>(undefined);
  const toastTimer = useRef<number | undefined>(undefined);

  useEffect(() => {
    getContacts().then((cs) => {
      const rank = (e: string) => (DEMO_ORDER.indexOf(e) + 1 || 99);
      const sorted = [...cs].sort((a, b) => rank(a.email) - rank(b.email));
      setContacts(sorted);
      if (sorted.length) pick(sorted[0].email);
    }, (e) => setError(`Could not load contacts: ${errorText(e)}`));
  }, []);

  function pick(email: string) {
    setTo(email);
    setBrief(EXAMPLE_BRIEFS[email] ?? "");
    setDraft(null);
    setActive(null);
  }

  const say = (msg: string) => {
    setToast(msg);
    window.clearTimeout(toastTimer.current);
    toastTimer.current = window.setTimeout(() => setToast(null), 4000);
  };
  const cancelClose = () => window.clearTimeout(closeTimer.current);
  const closeSoon = () => {
    cancelClose();
    closeTimer.current = window.setTimeout(() => setActive((a) => (a && a.open ? a : null)), 160);
  };

  // Hover only peeks; once a card is open, hovering another highlight leaves it alone.
  const peek = (id: string, el: HTMLElement) => {
    cancelClose();
    setActive((a) => (a && a.open && a.id !== id ? a : { id, el, open: a?.id === id ? a.open : false }));
  };
  const toggleOpen = (id: string, el: HTMLElement) => {
    cancelClose();
    setCardError(null);
    setActive((a) => (a && a.open && a.id === id ? null : { id, el, open: true }));
  };

  useEffect(() => {
    const onKey = (e: KeyboardEvent) => { if (e.key === "Escape") setActive(null); };
    const onDown = (e: MouseEvent) => {
      const t = e.target as HTMLElement;
      if (!t.closest(".card") && !t.closest("[data-id]")) setActive(null);
    };
    window.addEventListener("keydown", onKey);
    window.addEventListener("mousedown", onDown);
    return () => { window.removeEventListener("keydown", onKey); window.removeEventListener("mousedown", onDown); };
  }, []);

  async function generate() {
    setLoading(true);
    setError(null);
    setDraft(null);
    setMarks({});
    setEdits({});
    setActive(null);
    try {
      const d = await createDraft({ mode: "compose", to, brief });
      setDraft(d);
      setSubject(d.subject);
    } catch (e) {
      setError(`Could not write the draft: ${errorText(e)}`);
    } finally {
      setLoading(false);
    }
  }

  async function feedback(highlightId: string, action: "accept" | "reject") {
    if (!draft) return;
    setBusy(true);
    setCardError(null);
    try {
      await sendFeedback({ draft_id: draft.draft_id, highlight_id: highlightId, action });
      setMarks((m) => ({ ...m, [highlightId]: action === "accept" ? "kept" : "rejected" }));
      setActive(null);
      const name = contactName;
      say(action === "accept" ? `Saved to ${name}'s note.` : `Won't use this for ${name} again.`);
    } catch (e) {
      setCardError(`Could not save: ${errorText(e)}`);
    } finally {
      setBusy(false);
    }
  }

  function edited(id: string, text: string) {
    if (!draft) return;
    const original = draft.segments.filter((s) => s.highlight_id === id).map((s) => s.text);
    setEdits((x) => ({ ...x, [id]: text }));
    setMarks((m) => {
      const next = { ...m };
      if (original.includes(text)) delete next[id];
      else next[id] = "edited";
      return next;
    });
  }

  const contactName = contacts.find((c) => c.email === to)?.display_name ?? to;
  const hl = draft && active ? draft.highlights.find((h) => h.id === active.id) : undefined;
  const ids = draft ? draft.highlights.map((h) => h.id) : [];
  const strong = draft ? draft.highlights.filter((h) => h.strength === "strong" && !marks[h.id]).length + ids.filter((i) => marks[i] === "kept").length : 0;
  const weak = draft ? draft.highlights.filter((h) => h.strength === "weak" && !marks[h.id]).length : 0;
  const mine = ids.filter((i) => marks[i] === "edited").length;

  return (
    <main className="wrap">
      <section className="surface" aria-label="Compose">
        <div className="row">
          <span className="k">To</span>
          <select id="to" value={to} onChange={(e) => pick(e.target.value)}>
            {contacts.map((c) => (
              <option key={c.email} value={c.email}>{c.display_name}{c.relationship ? ` · ${c.relationship}` : ""}</option>
            ))}
          </select>
        </div>
        {draft && (
          <div className="row">
            <span className="k">Subject</span>
            <input id="subject" value={subject} onChange={(e) => setSubject(e.target.value)} />
          </div>
        )}
        <div className="brief">
          <label htmlFor="brief" className="muted small">What do you want to say?</label>
          <textarea id="brief" rows={3} value={brief} onChange={(e) => setBrief(e.target.value)} />
          <div className="bar">
            {loading && <span className="muted small">Writing as you would to {contactName}…</span>}
            <button type="button" className="btn primary" onClick={generate} disabled={loading || !to || !brief.trim()}>
              {draft ? "Regenerate" : "Generate draft"}
            </button>
          </div>
          {error && <p className="error">{error}</p>}
        </div>

        {draft && (
          <>
            <div className="status">
              <span className="count">
                <span className="item"><span className="dot strong" />{strong} backed by your emails</span>
                {weak > 0 && <span className="item"><span className="dot weak" />{weak} to check</span>}
                {mine > 0 && <span className="item"><span className="dot mine" />{mine} edited by you</span>}
              </span>
              <span>Edit the email directly</span>
            </div>
            {draft.warnings.map((w, i) => <p key={i} className="warn">{w}</p>)}
            <DraftBody
              draft={draft}
              marks={marks}
              activeId={active?.id ?? null}
              onHover={peek}
              onLeave={closeSoon}
              onOpen={toggleOpen}
              onEdit={edited}
              onTyping={() => setActive(null)}
            />
          </>
        )}
      </section>

      {draft && active && hl && (
        <HighlightCard
          key={hl.id}
          highlight={hl}
          contactName={contactName}
          scenario={draft.scenario}
          mark={marks[hl.id]}
          editedText={edits[hl.id]}
          originalText={draft.segments.find((s) => s.highlight_id === hl.id)?.text ?? ""}
          anchor={active.el}
          open={active.open}
          busy={busy}
          error={cardError}
          onEnter={cancelClose}
          onLeave={closeSoon}
          onFeedback={(a) => feedback(hl.id, a)}
        />
      )}
      <div className={`toast${toast ? " show" : ""}`} role="status">{toast}</div>
    </main>
  );
}
