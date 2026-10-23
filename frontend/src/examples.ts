import type { ContactSummary } from "./types";

// Example briefs, one per demo contact: the three demo cases use the briefs in
// email-mvp-notes/demo/demo-script.md word for word (Lead decision 14:42); recordings are re-made
// against them, and the replay service (8042) matches on to + brief exactly.
export const EXAMPLE_BRIEFS: Record<string, string> = {
  "wang.jianhua@example.com": "跟王老师确认下个月去家里看他的时间，问他需不需要我们带什么；看到他的书法入选展览了，想顺便去看看",
  "ethan.park@example.com": "约 Ethan 周五下午喝咖啡，问他能不能线下见，Red Rock 就行；顺便问一下他周六早上的散步小组还收人吗；恭喜他最近生宝宝了",
  "reservations@hoshinoya-kyoto.example.com": "11 月 20 号到 22 号想再住一次，两个大人；问能不能约红叶夜游船和周六下午的红叶茶会；晚餐还是提醒 Victor 不吃生贝类",
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
