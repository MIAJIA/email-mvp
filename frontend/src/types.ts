// Mirror of backend/app/schema.py (CONTRACT.md revision 0.2). Keep field names identical.
export const CONTRACT_REVISION = "0.2";

export type EntryStatus = "learned" | "confirmed" | "rejected";
export type Layer = "person" | "scenario" | "external" | "inferred";
export type RefKind = "address_as" | "honorific" | "sign_off" | "language" | "fact" | "habit" | "external";
export type Strength = "strong" | "weak";

export interface Evidence {
  message_id: string | null;
  external_id: string | null;
  quote: string;
}

export interface Email {
  thread_id: string;
  message_id: string;
  date: string;
  to: string;
  to_name: string | null;
  subject: string | null;
  body: string;
  prev: string | null;
  prev_sender: string | null;
  category: string | null;
  source: string | null;
}

export interface Ref {
  kind: RefKind;
  id: string;
}

export interface Highlight {
  id: string;
  layer: Layer;
  ref: Ref | null;
  strength: Strength;
  label: string;
  rationale: string;
  count: number | null;
  total: number | null;
  evidence: Evidence[];
}

export interface Segment {
  text: string;
  highlight_id: string | null;
}

export interface Draft {
  draft_id: string;
  to: string;
  scenario: string;
  subject: string;
  segments: Segment[];
  highlights: Highlight[];
  warnings: string[];
}

export interface ContactSummary {
  email: string;
  display_name: string;
  relationship: string | null;
}

export interface DraftRequest {
  mode: "compose" | "reply";
  to: string;
  thread_id?: string | null;
  brief: string;
  // Demo-only: rewrites one model tag to a ref that does not exist.
  inject?: "unknown_ref" | null;
}

export interface FeedbackRequest {
  draft_id: string;
  highlight_id: string;
  action: "accept" | "reject";
  correction?: string | null;
}

export interface FeedbackResponse {
  email: string;
  ref: Ref;
  status: EntryStatus;
}

// GET /contacts/{email} (backend/app/schema.py ContactNote).
export interface NoteField {
  value: string | null;
  count: number;
  total: number;
  status: EntryStatus;
  evidence: Evidence[];
}

export interface Fact {
  id: string;
  text: string;
  status: EntryStatus;
  evidence: Evidence[];
}

export interface Edge {
  to: string;
  type: string;
  evidence: Evidence[];
}

export interface ExternalItem {
  id: string;
  text: string;
  source_label: string;
  date: string;
}

// Contract 0.3: optional, one entry per context (private / default / formal).
export interface ContextAddress extends NoteField {
  context: "private" | "default" | "formal";
}

export interface ContactNote {
  email: string;
  display_name: string;
  relationship: string | null;
  scenario: string | null;
  address_as: NoteField;
  honorific: NoteField;
  sign_off: NoteField;
  language: NoteField;
  facts: Fact[];
  edges: Edge[];
  external: ExternalItem[];
  address_as_by_context?: ContextAddress[] | null;
  body: string;
}
