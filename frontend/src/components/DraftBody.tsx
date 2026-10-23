import { useEffect, useRef } from "react";
import type { Draft } from "../types";

// What the user did to one highlight in this draft.
//   kept     - accepted; underline fades
//   rejected - underline removed, text kept as written
//   edited   - the user changed the text; no underline (their own words need no explanation)
export type Mark = "kept" | "rejected" | "edited";

interface Props {
  draft: Draft;
  marks: Record<string, Mark>;
  activeId: string | null;
  onHover: (id: string, el: HTMLElement) => void;
  onLeave: () => void;
  onOpen: (id: string, el: HTMLElement) => void;
  onEdit: (id: string, text: string) => void;
  onTyping: () => void;
}

const escapeHtml = (s: string) =>
  s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");

// The body is a plain contenteditable rendered once per draft. After that it is only patched in place
// (class names), so the caret and anything the user typed outside highlights survive.
export default function DraftBody({ draft, marks, activeId, onHover, onLeave, onOpen, onEdit, onTyping }: Props) {
  const ref = useRef<HTMLDivElement>(null);
  const texts = useRef<Record<string, string>>({});
  const strength = new Map(draft.highlights.map((h) => [h.id, h.strength]));

  useEffect(() => {
    const el = ref.current!;
    texts.current = {};
    el.innerHTML = draft.segments
      .map((s) => {
        if (!s.highlight_id || !strength.has(s.highlight_id)) return escapeHtml(s.text);
        const id = s.highlight_id;
        // A highlight id can cover several segments (e.g. every "您"); give each span its own key.
        const key = `${id}#${Object.keys(texts.current).filter((k) => k.startsWith(id + "#")).length}`;
        texts.current[key] = s.text;
        return `<span data-id="${id}" data-key="${key}">${escapeHtml(s.text)}</span>`;
      })
      .join("");
    try { el.contentEditable = "plaintext-only"; } catch { el.contentEditable = "true"; }
    if (el.contentEditable !== "plaintext-only") el.contentEditable = "true";
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [draft.draft_id]);

  const beforeInput = useRef(handleBeforeInput);
  beforeInput.current = handleBeforeInput;
  useEffect(() => {
    const el = ref.current!;
    const fn = (e: Event) => beforeInput.current(e as InputEvent);
    el.addEventListener("beforeinput", fn);
    return () => el.removeEventListener("beforeinput", fn);
  }, []);

  // Patch class names whenever marks or the active highlight change.
  useEffect(() => {
    ref.current!.querySelectorAll<HTMLElement>("[data-id]").forEach((span) => {
      const id = span.dataset.id!;
      const mark = marks[id];
      const cls = mark === "rejected" || mark === "edited" ? "hl plain" : `hl ${strength.get(id)}${mark === "kept" ? " kept" : ""}`;
      span.className = cls + (id === activeId && !cls.includes("plain") ? " on" : "");
    });
  });

  const target = (e: React.SyntheticEvent) =>
    (e.target as HTMLElement).closest?.("[data-id]:not(.plain)") as HTMLElement | null;

  function handleInput() {
    onTyping();
    const seen = new Set<string>();
    ref.current!.querySelectorAll<HTMLElement>("[data-key]").forEach((span) => {
      const key = span.dataset.key!;
      seen.add(key);
      if (span.textContent !== texts.current[key]) {
        texts.current[key] = span.textContent ?? "";
        onEdit(span.dataset.id!, span.textContent ?? "");
      }
    });
    // A highlight span the browser removed entirely counts as an edit to an empty string.
    for (const key of Object.keys(texts.current)) {
      if (!seen.has(key) && texts.current[key] !== "") {
        texts.current[key] = "";
        onEdit(key.split("#")[0], "");
      }
    }
  }

  // Selecting a whole highlight and typing makes browsers drop the span and carry its underline style
  // onto the new text. Take over that case so the edit stays inside the original span.
  function handleBeforeInput(ev: InputEvent) {
    const sel = window.getSelection();
    if (!sel || !sel.rangeCount) return;
    const r = sel.getRangeAt(0);
    const host = (n: Node) => (n.nodeType === 1 ? (n as Element) : n.parentElement)?.closest("[data-key]") as HTMLElement | null;
    const span = host(r.startContainer);
    if (!span || span !== host(r.endContainer)) return;
    const offset = (node: Node, off: number) => {
      const x = document.createRange();
      x.setStart(span, 0);
      x.setEnd(node, off);
      return x.toString().length;
    };
    const text = span.textContent ?? "";
    const a = offset(r.startContainer, r.startOffset);
    const b = offset(r.endContainer, r.endOffset);
    if (!(a === 0 || b === text.length) || (r.collapsed && ev.inputType.startsWith("insert"))) return;
    let data: string | null = null;
    if (ev.inputType === "insertText" || ev.inputType === "insertReplacementText") data = ev.data ?? ev.dataTransfer?.getData("text/plain") ?? null;
    else if (ev.inputType === "insertFromPaste") data = ev.dataTransfer?.getData("text/plain") ?? null;
    else if (ev.inputType.startsWith("delete") && !r.collapsed) data = "";
    if (data === null) return;
    ev.preventDefault();
    span.textContent = text.slice(0, a) + data + text.slice(b);
    const node = span.firstChild;
    const c = document.createRange();
    if (node && node.nodeType === 3) c.setStart(node, Math.min(a + data.length, (node as Text).length));
    else c.setStart(span, 0);
    c.collapse(true);
    sel.removeAllRanges();
    sel.addRange(c);
    handleInput();
  }

  return (
    <div
      ref={ref}
      className="body"
      spellCheck={false}
      aria-label="Email body"
      suppressContentEditableWarning
      onInput={handleInput}
      onMouseOver={(e) => { const t = target(e); if (t) onHover(t.dataset.id!, t); }}
      onMouseOut={(e) => {
        const to = e.relatedTarget as HTMLElement | null;
        if (target(e) && !(to && (to.closest?.("[data-id]") || to.closest?.(".card")))) onLeave();
      }}
      onClick={(e) => { const t = target(e); if (t) onOpen(t.dataset.id!, t); }}
    />
  );
}
