import type { ContactSummary, Draft, DraftRequest, Email, FeedbackRequest, FeedbackResponse } from "./types";

const BASE: string = import.meta.env.VITE_API_BASE ?? "http://localhost:8041";

async function request<T>(path: string, init?: RequestInit): Promise<T> {
  const res = await fetch(BASE + path, {
    ...init,
    headers: init?.body ? { "Content-Type": "application/json" } : undefined,
  });
  if (!res.ok) {
    const text = await res.text().catch(() => "");
    throw new Error(`${res.status} ${res.statusText}${text ? `: ${text}` : ""}`);
  }
  return res.json() as Promise<T>;
}

export const getContacts = () => request<ContactSummary[]>("/contacts");

export const createDraft = (body: DraftRequest) =>
  request<Draft>("/draft", { method: "POST", body: JSON.stringify(body) });

export const getEmail = (messageId: string) =>
  request<Email>(`/emails/${encodeURIComponent(messageId)}`);

export const sendFeedback = (body: FeedbackRequest) =>
  request<FeedbackResponse>("/feedback", { method: "POST", body: JSON.stringify(body) });

export const errorText = (e: unknown) => (e instanceof Error ? e.message : String(e));
