import { useEffect, useRef, useState } from "react";
import { createDraft, errorText, getContacts, sendFeedback } from "./api";
import DraftBody, { type Decision } from "./components/DraftBody";
import HoverCard from "./components/HoverCard";
import SourcePanel from "./components/SourcePanel";
import type { ContactSummary, Draft } from "./types";

// Demo-only trigger for the unknown-ref fallback: open the page with ?inject=unknown_ref
const DEMO_INJECT = new URLSearchParams(window.location.search).get("inject") === "unknown_ref" ? "unknown_ref" as const : null;

interface Hover { id: string; top: number; left: number }

export default function App() {
  const [contacts, setContacts] = useState<ContactSummary[]>([]);
  const [to, setTo] = useState("");
  const [brief, setBrief] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [draft, setDraft] = useState<Draft | null>(null);
  const [decisions, setDecisions] = useState<Record<string, Decision>>({});
  const [hover, setHover] = useState<Hover | null>(null);
  const [cardBusy, setCardBusy] = useState(false);
  const [cardError, setCardError] = useState<string | null>(null);
  const [sourceId, setSourceId] = useState<string | null>(null);
  const closeTimer = useRef<number | undefined>(undefined);

  useEffect(() => {
    getContacts().then((cs) => {
      setContacts(cs);
      if (cs.length) setTo(cs[0].email);
    }, (e) => setError(`Could not load contacts: ${errorText(e)}`));
  }, []);

  const cancelClose = () => window.clearTimeout(closeTimer.current);
  const scheduleClose = () => {
    cancelClose();
    closeTimer.current = window.setTimeout(() => setHover(null), 150);
  };

  const openCard = (id: string, el: HTMLElement) => {
    cancelClose();
    const r = el.getBoundingClientRect();
    if (hover?.id !== id) setCardError(null);
    setHover({ id, top: r.bottom + window.scrollY + 4, left: r.left + window.scrollX });
  };

  async function generate() {
    setLoading(true);
    setError(null);
    setDraft(null);
    setDecisions({});
    setHover(null);
    setSourceId(null);
    try {
      setDraft(await createDraft({ mode: "compose", to, brief, inject: DEMO_INJECT }));
    } catch (e) {
      setError(errorText(e));
    } finally {
      setLoading(false);
    }
  }

  async function feedback(highlightId: string, action: Decision) {
    if (!draft) return;
    setCardBusy(true);
    setCardError(null);
    try {
      await sendFeedback({ draft_id: draft.draft_id, highlight_id: highlightId, action });
      setDecisions((d) => ({ ...d, [highlightId]: action }));
      if (action === "reject") setHover(null);
    } catch (e) {
      setCardError(`Could not save feedback: ${errorText(e)}`);
    } finally {
      setCardBusy(false);
    }
  }

  const hovered = draft && hover ? draft.highlights.find((h) => h.id === hover.id) : undefined;
  const source = draft && sourceId ? draft.highlights.find((h) => h.id === sourceId) : undefined;
  const strong = draft?.highlights.filter((h) => h.strength === "strong").length ?? 0;
  const weak = draft?.highlights.filter((h) => h.strength === "weak").length ?? 0;

  return (
    <>
      <main style={{ maxWidth: 720, padding: 24, marginRight: source ? 400 : undefined }}>
        <h2 style={{ marginTop: 0 }}>Draft an email</h2>
        <div style={{ display: "flex", flexDirection: "column", gap: 8 }}>
          <label>
            To{" "}
            <select value={to} onChange={(e) => setTo(e.target.value)}>
              {contacts.map((c) => (
                <option key={c.email} value={c.email}>
                  {c.display_name} &lt;{c.email}&gt;{c.relationship ? ` (${c.relationship})` : ""}
                </option>
              ))}
            </select>
          </label>
          <label style={{ display: "flex", flexDirection: "column" }}>
            What do you want to say?
            <textarea rows={4} value={brief} onChange={(e) => setBrief(e.target.value)} />
          </label>
          <div>
            <button onClick={generate} disabled={loading || !to || !brief.trim()}>Generate</button>
            {loading && <span style={{ marginLeft: 8 }}>Generating…</span>}
          </div>
          {error && <div>{error}</div>}
        </div>

        {draft && (
          <section style={{ marginTop: 24 }}>
            <div><b>Subject:</b> {draft.subject}</div>
            <div style={{ color: "#555", margin: "4px 0 8px" }}>
              Uses {draft.highlights.length} notes: {strong} well-supported, {weak} inferred
            </div>
            {draft.warnings.map((w, i) => (
              <div key={i} style={{ background: "#f3f3f3", borderLeft: "4px solid #F59E0B", padding: "6px 10px", marginBottom: 8 }}>
                <b>Warning</b> {w}
              </div>
            ))}
            <DraftBody
              segments={draft.segments}
              highlights={draft.highlights}
              decisions={decisions}
              hoveredId={hover?.id ?? null}
              onEnter={openCard}
              onLeave={scheduleClose}
            />
          </section>
        )}
      </main>

      {draft && hover && hovered && (
        <HoverCard
          highlight={hovered}
          scenario={draft.scenario}
          decision={decisions[hovered.id]}
          top={hover.top}
          left={hover.left}
          busy={cardBusy}
          error={cardError}
          onEnter={cancelClose}
          onLeave={scheduleClose}
          onFeedback={(a) => feedback(hovered.id, a)}
          onViewSource={() => setSourceId(hovered.id)}
        />
      )}
      {source && <SourcePanel key={source.id} highlight={source} onClose={() => setSourceId(null)} />}
    </>
  );
}
