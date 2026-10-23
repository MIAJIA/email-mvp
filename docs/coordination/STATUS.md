# STATUS

只有一份，放在主检出目录。Lead 负责更新，任何 session 都能读。

Last updated: 2026-10-23 14:00 by Lead. T0: 14:00. Freeze: 14:50. Now at: **CP0**.

## Lines

| Line | Session | Branch @ head | State | Last report | Next |
| --- | --- | --- | --- | --- | --- |
| 骨架线 | 待启动 | `line/skeleton` | planned | — | 和用户定契约、模型和语言，然后跑通 3 个例子 |
| 上下文数据线 | 待启动 | `line/context-data` | planned | — | 写标准答案，补敬语收件人和外部上下文 mock |
| Integrator | CP1 | `main` | planned | — | 第一次合并 |

## Merge batches

| Batch | Branches | Gate result | Walkthrough | Pushed | Report |
| --- | --- | --- | --- | --- | --- |
| | | | | | |

## Waiting for the user

| Since | Question | Asked by | Blocks |
| --- | --- | --- | --- |
| 14:00 | 用哪个模型、费用上限多少？ | Lead（骨架线会在它的对话里问） | 骨架线的真实运行 |
| 14:00 | 界面文字用中文还是英文？ | Lead（骨架线会问） | 前端文案 |
| 14:00 | 黄色"口癖/笔误"高亮做不做？ | Lead | 契约里 `layer` 的取值 |

## Must-haves

| Must-have | Owning line | State | Fits in the time left? |
| --- | --- | --- | --- |
| 离线提取（收件人笔记 + 场景风格），证据核对 | 骨架线 → 核心线 | not started | at risk（一小时很紧） |
| `POST /draft` 返回片段和高亮 | 骨架线 | not started | yes |
| 前端三层披露 | 骨架线 → 前端线 | not started | yes |
| 接受和拒绝回写笔记 | 核心线 + 前端线 | not started | at risk |
| 前后端分开 | 骨架线 | not started | yes |

## Checkpoints reached

| Checkpoint | Time (spent / left) | Evidence | Scope review: on course? | User's words |
| --- | --- | --- | --- | --- |
| CP0 | 14:00（0 / 60 分钟） | 共享文件和脚手架已提交 | 是 | "你开 Swarm，我到对应的 Chat 里面" |
