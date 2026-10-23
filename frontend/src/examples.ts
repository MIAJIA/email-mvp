import type { ContactSummary } from "./types";

// Example briefs, one per demo contact. They match the briefs in recordings/ word for word
// (skeleton 428aee7), so the replay service (8042) can answer them without calling the model.
export const EXAMPLE_BRIEFS: Record<string, string> = {
  "wang.jianhua@example.com": "告诉王老师我下个月回北京，想约他见面当面道谢，问他哪天方便",
  "ethan.park@example.com":
    "Say yes to coffee, Friday afternoon works. Ask if we can meet in person at Red Rock or the boba place nearby.",
  "reservations@hoshinoya-kyoto.example.com":
    "We arrive Nov 14 around 9pm, ask if late check-in is ok; need a car from Kyoto Station for 2 adults and 1 baby; ask if the room can fit a baby crib. Also ask about anything special happening at the hotel during our stay.",
  "tang.shuyuan@example.com": "以校友会组委会的名义正式邀请他在 12 月 6 日的校友年会上做 10 分钟致辞，请他在下周五前回复是否方便",
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
