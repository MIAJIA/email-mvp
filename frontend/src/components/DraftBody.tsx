import type { CSSProperties } from "react";
import type { Highlight, Segment, Strength } from "../types";

export type Decision = "accept" | "reject";

const STYLE: Record<Strength, { line: CSSProperties; hoverBg: string }> = {
  strong: {
    line: { textDecorationLine: "underline", textDecorationStyle: "solid", textDecorationColor: "#0072B2" },
    hoverBg: "#E6F1F8",
  },
  weak: {
    line: { textDecorationLine: "underline", textDecorationStyle: "dashed", textDecorationColor: "#B45309" },
    hoverBg: "#FEF3E2",
  },
};

interface Props {
  segments: Segment[];
  highlights: Highlight[];
  decisions: Record<string, Decision>;
  hoveredId: string | null;
  onEnter: (id: string, el: HTMLElement) => void;
  onLeave: () => void;
}

export default function DraftBody({ segments, highlights, decisions, hoveredId, onEnter, onLeave }: Props) {
  const byId = new Map(highlights.map((h) => [h.id, h]));
  return (
    <div style={{ whiteSpace: "pre-wrap", border: "1px solid #ddd", padding: 12, borderRadius: 4 }}>
      {segments.map((seg, i) => {
        const h = seg.highlight_id ? byId.get(seg.highlight_id) : undefined;
        const decision = h ? decisions[h.id] : undefined;
        if (!h || decision === "reject") return <span key={i}>{seg.text}</span>;
        const s = STYLE[decision === "accept" ? "strong" : h.strength];
        return (
          <span
            key={i}
            style={{
              ...s.line,
              textDecorationThickness: "2px",
              textUnderlineOffset: "3px",
              cursor: "pointer",
              background: hoveredId === h.id ? s.hoverBg : undefined,
            }}
            onMouseEnter={(e) => onEnter(h.id, e.currentTarget)}
            onMouseLeave={onLeave}
          >
            {seg.text}
          </span>
        );
      })}
    </div>
  );
}
