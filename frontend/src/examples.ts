import type { ContactSummary } from "./types";

// Example briefs, one per demo contact. They match the briefs in recordings/ word for word,
// so the replay service (8042) can answer them without calling the model.
export const EXAMPLE_BRIEFS: Record<string, string> = {
  "wang.laoshi@example.com": "告诉王老师我下个月回北京，想约她见面当面感谢推荐信，问她哪天方便",
  "ethan.park@example.com":
    "Say yes to coffee, Friday afternoon works. Ask if we can meet in person at Red Rock or the boba place nearby.",
  "reservations@hoshinoya-kyoto.example.com":
    "We arrive Nov 14 around 9pm, ask if late check-in is ok; need a car from Kyoto Station for 2 adults and 1 baby; ask if the room can fit a baby crib. Also ask about anything special happening at the hotel during our stay.",
};

// Demo order agreed with the user: formal case first, then the coach, then the hotel.
export const DEMO_ORDER = [
  "wang.laoshi@example.com",
  "ethan.park@example.com",
  "reservations@hoshinoya-kyoto.example.com",
];

// Demo-only trigger for the unknown-ref fallback: open the page with ?inject=unknown_ref.
export const DEMO_INJECT =
  new URLSearchParams(window.location.search).get("inject") === "unknown_ref" ? ("unknown_ref" as const) : null;

// The recorded failure case (recordings/ethan-park-7669d1a6fc.json) used this brief.
export const INJECT_BRIEFS: Record<string, string> = {
  "ethan.park@example.com": "Say yes to coffee, Friday afternoon works. Ask if we can meet in person at Red Rock.",
};

// Fallback when GET /contacts returns nothing (e.g. the replay service started without notes),
// so the three demo cases can still be generated from recordings.
export const DEMO_CONTACTS: ContactSummary[] = [
  { email: "wang.laoshi@example.com", display_name: "王老师", relationship: null },
  { email: "ethan.park@example.com", display_name: "Ethan Park", relationship: null },
  { email: "reservations@hoshinoya-kyoto.example.com", display_name: "Kenji (HOSHINOYA Kyoto)", relationship: null },
];
