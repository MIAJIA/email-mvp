# GLOSSARY

只有一份，放在主检出目录，不进 git。每个 session 第一次编辑前用绝对路径（`$MAIN/GLOSSARY.md`）读它。规则见 `~/.claude/skills/swarm-control/procedures/contract.md`。

- **先登记再使用。**新词先追加到这里，状态写 `proposed`，再出现在代码、文档或界面里。Lead 在下一个检查点确认。
- **重命名或重新定义一个词，属于契约的破坏性改动。**要问用户并记进 DECISIONS.md。
- **`check.sh` 遇到任何已废弃的名字都会失败**（"Deprecated" 一列，每个名字用反引号括起来，逗号分隔）。

Last confirmed by the Lead: 2026-10-23 14:00, contract revision `0.1`.

| Term | Definition | In code | Label for users | Not to be confused with | Deprecated | Status |
| --- | --- | --- | --- | --- | --- | --- |
| 收件人笔记 | 关于一个收件人的一份 Markdown 文件：你怎么称呼他、用不用敬语、用什么语言、你们之间的事实、他和别人的关系，每条都带证据。画像的第二层。 | `ContactNote`, `contacts/<email>.md` | "Contact note" | 场景风格（不分对象） | | proposed |
| 场景风格 | 你在某一类场景下的通用写法（长度、开头、结尾、落款、语气），从所有该场景邮件中提取。画像的第一层，收件人笔记缺的部分由它补。 | `ScenarioStyle`, `styles/<scenario>.json` | "Your style for <scenario>" | 收件人笔记 | | proposed |
| 场景 | 一封邮件的类别，例如 `friend_scheduling`、`vendor_service`、`zh_en_casual`、`refund_complaint`。按"这封信"判断，不按"这个人"。 | `scenario`（样例邮件 JSONL 里的字段名是 `category`，含义相同） | "Scenario" | 关系（属于人，不属于信） | | proposed |
| 习惯 | 场景风格里的一条可统计的写法，带计数和证据。 | `Habit`, `habit_id` | "Habit" | 事实 | | proposed |
| 事实 | 收件人笔记里一条关于这个人或你们之间的具体信息，带证据。 | `Fact`, `fact_id` | "What you know" | 习惯 | | proposed |
| 外部上下文 | 不来自你邮件的、关于收件人的近期信息，例如酒店近期活动、教练的社交动态。MVP 中全部为 mock 数据。 | `ExternalContext` | "Recent context" | 事实（来自你的邮件） | | proposed |
| 关系边 | 两个人之间的关系，例如"同事""夫妻"，带证据。所有边合起来就是关系图谱。 | `Edge` | "Connection" | | | proposed |
| 证据 | 一条可核对的出处：邮件编号加一段逐字原文（或外部上下文的条目编号）。入库前由代码核对原文确实存在。 | `Evidence{message_id, quote}` | "Source" | 理由 | | proposed |
| 理由 | 一句给用户看的解释，由代码根据笔记条目和计数拼出，不由模型生成。 | `rationale` | "Why" | 证据 | | proposed |
| 高亮 | 草稿里一段带来源的文字。属于某一层，有强弱，指向一个笔记条目。 | `Highlight` | 行内下划线 | | | proposed |
| 层 | 高亮来源：`person`（收件人笔记）、`scenario`（场景风格）、`external`（外部上下文）、`inferred`（没有证据，模型推断）。 | `layer` | "From your emails with X" / "From your <scenario> style" / "Recent context" / "Inferred" | 强度 | | proposed |
| 强度 | 证据多少，由代码按计数决定：`strong` 或 `weak`。 | `strength` | 实线 / 虚线 | 层 | | proposed |
| 草稿 | 一次 `/draft` 的结果：切好的片段加高亮列表。 | `Draft`, `draft_id` | "Draft" | | | proposed |
| 片段 | 草稿正文的一段文字，可能挂着一个高亮。前端按顺序渲染，不计算字符位置。 | `Segment` | | | | proposed |
| 标准答案 | 上下文数据线写的关系图谱真值（人物、称呼、敬语、事实、边、外部上下文），用来生成样例邮件和评估离线提取。离线管线不能读。 | `data/ground_truth/` | | 收件人笔记（是提取结果） | | proposed |
