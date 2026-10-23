import { useEffect, useState } from "react";
import { errorText, getEmail } from "../api";
import type { Email, Evidence, Highlight } from "../types";

function EmailEvidence({ ev }: { ev: Evidence }) {
  const [email, setEmail] = useState<Email | null>(null);
  const [error, setError] = useState<string | null>(null);
  useEffect(() => {
    if (!ev.message_id) return;
    getEmail(ev.message_id).then(setEmail, (e) => setError(errorText(e)));
  }, [ev.message_id]);
  if (error) return <div>{error}</div>;
  if (!email) return <div>Loading…</div>;
  const idx = ev.quote ? email.body.indexOf(ev.quote) : -1;
  return (
    <div>
      <div><b>Subject:</b> {email.subject}</div>
      <div><b>To:</b> {email.to_name ? `${email.to_name} <${email.to}>` : email.to}</div>
      <div><b>Date:</b> {email.date}</div>
      {idx < 0 && <div style={{ fontSize: 12, color: "#666" }}>Quote not found in this email</div>}
      <div style={{ whiteSpace: "pre-wrap", marginTop: 6, fontSize: 14 }}>
        {idx < 0 ? email.body : (
          <>
            {email.body.slice(0, idx)}
            <mark style={{ background: "#E6F1F8" }}>{ev.quote}</mark>
            {email.body.slice(idx + ev.quote.length)}
          </>
        )}
      </div>
    </div>
  );
}

export default function SourcePanel({ highlight, onClose }: { highlight: Highlight; onClose: () => void }) {
  return (
    <aside style={{
      position: "fixed", top: 0, right: 0, bottom: 0, width: 380, overflowY: "auto",
      background: "#fafafa", borderLeft: "1px solid #ddd", padding: 16, boxSizing: "border-box",
    }}>
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
        <b>Sources: {highlight.label}</b>
        <button onClick={onClose}>Close</button>
      </div>
      {highlight.evidence.map((ev, i) => (
        <div key={i} style={{ borderTop: "1px solid #ddd", marginTop: 12, paddingTop: 12 }}>
          <div style={{ fontSize: 12, color: "#666" }}>{i + 1} of {highlight.evidence.length}</div>
          {ev.message_id ? <EmailEvidence ev={ev} /> : ev.external_id ? (
            <div><div>Recent context (mock)</div><div style={{ fontStyle: "italic" }}>"{ev.quote}"</div></div>
          ) : (
            <div style={{ fontStyle: "italic" }}>"{ev.quote}"</div>
          )}
        </div>
      ))}
    </aside>
  );
}
