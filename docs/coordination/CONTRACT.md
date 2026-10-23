# CONTRACT

契约的文字层。只有一份，放在主检出目录，不进 git，归 Lead 管。代码层在 `backend/app/schema.py`，归骨架线（之后是核心线）。前端的类型镜像在 `frontend/src/types.ts`，由骨架线决定是生成还是由 `check.sh` 校验。规则见 `~/.claude/skills/swarm-control/procedures/contract.md`。

当前修订：**0.1（Lead 起草，骨架线和用户一起定版；CP1 时升到 1）**。这里用到的词都在 `$MAIN/GLOSSARY.md` 里定义。

> 0.1 是草案。骨架线可以提出任何修改，经用户同意后由 Lead 更新这里。

## 形状

### Email（输入数据）

- 沿用 `email-style-demo/data/*.jsonl` 的字段：`thread_id, message_id, date, to, to_name, subject, body, prev, prev_sender, category, source`。
- `planted_*` 字段（`planted_habits`、上下文数据线新增的 `planted_address`、`planted_facts` 等）只给评估用，**离线管线不能读**。
- 不变量：`message_id` 全局唯一。

### Evidence

- 字段：`message_id`（必填，或外部上下文时填 `external_id`），`quote`（必填，逐字原文）。
- 不变量：入库前代码检查 `quote` 是 `message_id` 对应邮件 `body` 的子串；对不上的证据直接丢弃。

### ContactNote（`contacts/<email>.md`）

- frontmatter 字段：
  - `email`（必填）、`display_name`（必填）、`relationship`（可选，推断）、`language`（可选）。
  - `address_as`、`honorific`、`sign_off`：每个都是 `{ value, count, total, evidence: [Evidence] }`；`value` 可为 null，表示退回场景风格。
  - `edges`：`[{ to, type, evidence }]`。
  - `external`：`[{ id, text, source_label, date }]`（mock 外部上下文）。
- 正文：`## Facts` 下每条 `- <fact_id>: <text> [<message_id>: "<quote>"]`。
- 不变量：每条字段和事实至少有一条通过核对的证据，否则不写入。

### ScenarioStyle（`styles/<scenario>.json`）

- `{ scenario, habits: [{ id, description, count, total, evidence: [Evidence] }] }`

### Highlight

- `id`（必填）、`layer`：`person | scenario | external | inferred`、`ref`：`{ kind: address_as | honorific | sign_off | fact | habit | external, id }`（`inferred` 时为 null）、`strength`：`strong | weak`、`rationale`（字符串）、`evidence`：`[Evidence]`（`inferred` 时为空）。
- 不变量：`rationale`、`evidence`、`strength` 由代码根据 `ref` 从笔记里取出和拼接，**不由模型生成**。模型只输出 `ref`。

### Draft

- `{ draft_id, to, scenario, segments: [{ text, highlight_id? }], highlights: [Highlight] }`
- 不变量：把所有 `segments[].text` 按顺序拼起来就是邮件全文；每个 `highlight_id` 都能在 `highlights` 里找到。

## 接口

| 方法 | 路径 | 请求 | 响应 |
| --- | --- | --- | --- |
| GET | `/contacts` | — | `[{ email, display_name, relationship }]` |
| GET | `/contacts/{email}` | — | `ContactNote`（解析后的 JSON） |
| GET | `/threads` | — | `[{ thread_id, subject, last_from, messages: [...] }]` |
| GET | `/emails/{message_id}` | — | `Email` |
| POST | `/draft` | `{ mode: "compose" \| "reply", to, thread_id?, brief }` | `Draft` |
| POST | `/feedback` | `{ draft_id, highlight_id, action: "accept" \| "reject", correction? }` | 更新后的那条笔记字段 |

- 错误：找不到收件人笔记时不报错，`/draft` 退回只用场景风格；模型输出里引用了不存在的 `ref` 时，那段文字降为无高亮的普通片段，并在响应里带 `warnings`。

## 修改记录

| 时间 | 修订 | 改动 | 增量或破坏性 | 批准人 |
| --- | --- | --- | --- | --- |
| 2026-10-23 14:00 | 0.1 | 根据主对话里的设计起草 | — | Lead |
