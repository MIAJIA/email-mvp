import { useLayoutEffect, useRef, useState } from "react";
import { errorText, getEmail } from "../api";
import type { Email, Evidence, Highlight } from "../types";
import type { Mark } from "./DraftBody";

interface Props {
  highlight: Highlight;
  contactName: string;
  scenario: string;
  mark: Mark | undefined;
  editedText: string | undefined;
  originalText: string;
  anchor: HTMLElement;
  open: boolean;
  busy: boolean;
  error: string | null;
  onEnter: () => void;
  onLeave: () => void;
  onFeedback: (action: "accept" | "reject") => void;
}

// One line under the title saying where this came from (GLOSSARY: 层 → user labels).
function sourceLine(h: Highlight, contactName: string, scenario: string): string {
  const n = h.count != null && h.total != null ? ` · ${h.count} / ${h.total}` : h.count != null ? ` · ${h.count} email${h.count > 1 ? "s" : ""}` : "";
  switch (h.layer) {
    case "person": return `From your emails with ${contactName}${n}`;
    case "scenario": return `Your ${scenario.replace(/_/g, " ")} style${n}`;
    case "external": return "Recent context";
    default: return "Inferred · not in your emails";
  }
}

export function Quote({ ev }: { ev: Evidence }) {
  const [email, setEmail] = useState<Email | null>(null);
  const [err, setErr] = useState<string | null>(null);
  const [shown, setShown] = useState(false);
  const toggle = () => {
    setShown((s) => !s);
    if (!email && ev.message_id) getEmail(ev.message_id).then(setEmail, (e) => setErr(errorText(e)));
  };
  const body = email?.body ?? "";
  const i = body.indexOf(ev.quote);
  return (
    <li>
      <span className="who">{ev.message_id ? (email ? `${email.date.slice(0, 10)} · ${email.subject ?? ev.message_id}` : ev.message_id) : `Source ${ev.external_id}`}</span>
      <span className="txt">{ev.quote}</span>
      {ev.message_id && (
        <button type="button" className="link" onClick={toggle}>{shown ? "Hide email" : "Show email"}</button>
      )}
      {shown && (
        <div className="full">
          {err ? `Could not load the email: ${err}` : !email ? "Loading…" : i < 0 ? body : (
            <>{body.slice(0, i)}<mark>{ev.quote}</mark>{body.slice(i + ev.quote.length)}</>
          )}
        </div>
      )}
    </li>
  );
}

// Same card in two sizes: hover peeks (title + source line, no buttons), click opens it in place
// (evidence and buttons grow in below). Positioned under the highlight, or above it near the bottom.
export default function HighlightCard(p: Props) {
  const h = p.highlight;
  const ref = useRef<HTMLDivElement>(null);
  const [pos, setPos] = useState<React.CSSProperties>({ left: 0, top: 0 });
  const [shown, setShown] = useState(false);

  useLayoutEffect(() => {
    const place = () => {
      const r = p.anchor.getClientRects()[0] ?? p.anchor.getBoundingClientRect();
      const w = Math.min(p.open ? 360 : 280, window.innerWidth - 24);
      const left = Math.min(Math.max(12, r.left - 14), window.innerWidth - w - 12);
      const h = p.open ? (ref.current?.scrollHeight ?? 260) + 160 : 90;
      const below = r.bottom + 10 + h < window.innerHeight || r.top < h + 20;
      setPos(below
        ? { left, top: r.bottom + 10, transformOrigin: `${Math.max(16, r.left - left + 16)}px top` }
        : { left, bottom: window.innerHeight - r.top + 10, transformOrigin: `${Math.max(16, r.left - left + 16)}px bottom` });
    };
    place();
    const id = requestAnimationFrame(() => setShown(true));
    window.addEventListener("scroll", place, { passive: true });
    window.addEventListener("resize", place);
    return () => { cancelAnimationFrame(id); window.removeEventListener("scroll", place); window.removeEventListener("resize", place); };
  }, [p.anchor, p.open]);

  const weak = h.strength === "weak";
  const edited = p.mark === "edited";
  const cls = `card${shown ? " show" : ""}${p.open ? " open" : ""}${weak || edited ? " is-weak" : ""}`;

  if (edited) {
    return (
      <div ref={ref} className={cls} style={pos} role="dialog" aria-label="Your edit" onMouseEnter={p.onEnter} onMouseLeave={p.onLeave}>
        <div className="c-head"><span className="dot mine" /><span className="c-name">Your edit</span>
          <span className="c-sub">Kept in this draft</span></div>
        <div className="more"><div><div className="inner">
          <ul className="ev">
            <li><span className="who">Was</span><span className="txt"><s>{p.originalText}</s></span></li>
            <li><span className="who">You wrote</span><span className="txt">{p.editedText?.trim() ? p.editedText : "(deleted)"}</span></li>
          </ul>
        </div></div></div>
      </div>
    );
  }

  const status = p.mark === "kept" ? " · You confirmed" : "";
  return (
    <div ref={ref} className={cls} style={pos} role="dialog" aria-label={h.label} onMouseEnter={p.onEnter} onMouseLeave={p.onLeave}>
      <div className="c-head">
        <span className={`dot ${weak ? "weak" : "strong"}`} />
        <span className="c-name">{h.label}</span>
        <span className="c-sub">{sourceLine(h, p.contactName, p.scenario)}{status}</span>
      </div>
      <div className="more"><div><div className="inner">
        <p className="why">{h.rationale}</p>
        {h.evidence.length > 0
          ? <ul className="ev">{h.evidence.map((ev, i) => <Quote key={i} ev={ev} />)}</ul>
          : <p className="why">No email backs this. The model wrote it from your brief.</p>}
        {p.mark !== "rejected" && h.ref && (
          <div className="btns">
            <button type="button" className="btn primary" disabled={p.busy || p.mark === "kept"} onClick={() => p.onFeedback("accept")}>Keep</button>
            <button type="button" className="btn" disabled={p.busy} onClick={() => p.onFeedback("reject")}>Reject</button>
          </div>
        )}
        {p.error && <p className="why">{p.error}</p>}
      </div></div></div>
    </div>
  );
}
