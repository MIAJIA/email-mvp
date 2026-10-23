import type { Highlight } from "../types";
import type { Decision } from "./DraftBody";

interface Props {
  highlight: Highlight;
  scenario: string;
  decision: Decision | undefined;
  top: number;
  left: number;
  busy: boolean;
  error: string | null;
  onEnter: () => void;
  onLeave: () => void;
  onFeedback: (action: Decision) => void;
  onViewSource: () => void;
}

function layerLabel(h: Highlight, scenario: string): string {
  switch (h.layer) {
    case "person": return "From your emails with this contact";
    case "scenario": return `From your style for ${scenario}`;
    case "external": return "Recent context";
    default: return "Inferred, no source";
  }
}

export default function HoverCard(p: Props) {
  const h = p.highlight;
  let status = h.strength === "strong" ? "● Well-supported" : "◌ Inferred · please confirm";
  if (h.count != null && h.total != null) status += ` · ${h.count} / ${h.total} emails`;
  if (p.decision === "accept") status = "● You confirmed";
  const quote = h.evidence[0]?.quote;
  const hasSource = h.evidence.some((e) => e.message_id || e.external_id);
  return (
    <div
      onMouseEnter={p.onEnter}
      onMouseLeave={p.onLeave}
      style={{
        position: "absolute", top: p.top, left: p.left, width: 340, zIndex: 10,
        background: "#fff", border: "1px solid #ccc", borderRadius: 6, padding: 10,
        boxShadow: "0 2px 8px rgba(0,0,0,0.15)", fontSize: 14,
      }}
    >
      <div style={{ fontWeight: 600 }}>{h.label}</div>
      <div style={{ color: h.strength === "strong" || p.decision === "accept" ? "#0072B2" : "#B45309" }}>{status}</div>
      <div style={{ color: "#666" }}>{layerLabel(h, p.scenario)}</div>
      <div>{h.rationale}</div>
      {quote && <div style={{ fontStyle: "italic", color: "#444" }}>"{quote}"</div>}
      <div style={{ display: "flex", gap: 6, marginTop: 8 }}>
        <button disabled={p.busy} onClick={() => p.onFeedback("accept")}>Yes, keep this</button>
        <button disabled={p.busy} onClick={() => p.onFeedback("reject")}>Not this</button>
        {hasSource && <button onClick={p.onViewSource}>View source →</button>}
      </div>
      {p.error && <div style={{ marginTop: 6 }}>{p.error}</div>}
    </div>
  );
}
