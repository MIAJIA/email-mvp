import type { ContactSummary } from "./types";

// Example briefs, one per demo contact, in English so the demo audience can follow them
// (user decision 15:08). Same meaning as the demo script's Chinese briefs. These no longer match
// the recordings, so the replay service (8042) will not find them; the demo uses the live backend.
export const EXAMPLE_BRIEFS: Record<string, string> = {
  "wang.jianhua@example.com":
    "Confirm with Professor Wang when we can visit him at home next month, and ask if he'd like us to bring anything. I saw his calligraphy was selected for an exhibition, so I'd like to go see it while we're there.",
  "ethan.park@example.com":
    "Grab coffee with Ethan Friday afternoon. Ask if we can meet in person, Red Rock is fine. Also ask if his Saturday morning walking group is still taking people, and congratulate him on the new baby.",
  "reservations@hoshinoya-kyoto.example.com":
    "We'd like to stay again November 20 to 22, two adults. Ask if we can book the autumn-leaves evening boat and the Saturday afternoon autumn tea gathering. For dinner, remind them again that Victor doesn't eat raw shellfish.",
  "tang.shuyuan@example.com":
    "On behalf of the alumni association organizing committee, formally invite him to give a 10-minute speech at the alumni gala on December 6, and ask him to reply by next Friday whether he can.",
  "amy.wang@example.com": "Say yes to coffee, Friday afternoon works. Ask if we can meet in person at Red Rock.",
};

// Demo order agreed with the user: formal case first, then the coach, then the hotel.
export const DEMO_ORDER = [
  "wang.jianhua@example.com",
  "ethan.park@example.com",
  "reservations@hoshinoya-kyoto.example.com",
  "tang.shuyuan@example.com",
  "amy.wang@example.com",
];

// Demo-only trigger for the unknown-ref fallback: open the page with ?inject=unknown_ref.
export const DEMO_INJECT =
  new URLSearchParams(window.location.search).get("inject") === "unknown_ref" ? ("unknown_ref" as const) : null;

// The recorded failure case (recordings/amy-wang-1a5bafc33e.json) used this brief.
export const INJECT_BRIEFS: Record<string, string> = {
  "amy.wang@example.com": "Say yes to coffee, Friday afternoon works. Ask if we can meet in person at Red Rock.",
};

// Fallback when GET /contacts returns nothing (e.g. the replay service started without notes),
// so the demo cases can still be generated from recordings.
export const DEMO_CONTACTS: ContactSummary[] = [
  { email: "wang.jianhua@example.com", display_name: "王建华", relationship: null },
  { email: "ethan.park@example.com", display_name: "Ethan Park", relationship: null },
  { email: "reservations@hoshinoya-kyoto.example.com", display_name: "HOSHINOYA Kyoto", relationship: null },
  { email: "tang.shuyuan@example.com", display_name: "唐书远", relationship: null },
  { email: "amy.wang@example.com", display_name: "Amy", relationship: null },
];
