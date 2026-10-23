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
