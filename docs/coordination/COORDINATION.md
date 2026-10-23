# COORDINATION

只有一份，放在主检出目录，不进 git，归 Lead 管。

## Paths

| 名字 | 路径 |
| --- | --- |
| `$MAIN`（主检出，`main` 分支） | `/Users/mia/Downloads/mia星辰大海/email-mvp` |
| `$NOTES`（交接记录、合并请求、门禁报告） | `/Users/mia/Downloads/mia星辰大海/email-mvp-notes` |
| 快照 | `$MAIN/docs/coordination/` |
| 原始样例邮件（只读，属于另一个对话，不要改） | `/Users/mia/Downloads/mia星辰大海/email-style-demo/data/` |
| UX 调研报告（只读） | `/Users/mia/Downloads/mia星辰大海/email-highlight-research/report.md` |

## 保留端口和进程（谁都不碰）

| 端口 | 归属 |
| --- | --- |
| 8000、8030、5175 | 用户自己的服务器 |

停服务只能停自己作为后台任务启动的那个，按任务或自己的 PID 停。不准用 `kill`、`pkill`、`killall` 按名字杀进程。

## 端口表

| 端口 | 用途 | 归属 |
| --- | --- | --- |
| 8041 | 后端 API（真实模型） | 骨架线，之后是核心线 |
| 8042 | 后端回放服务（不调付费接口） | 骨架线，之后是核心线 |
| 5181 | 前端开发服务器 | 骨架线，之后是前端线 |

## 资源表

| 线 | Session | Worktree | 分支 | 拥有的路径 | 热文件 | 可以 push |
| --- | --- | --- | --- | --- | --- | --- |
| Lead | 主对话 | `$MAIN`（只写五份共享文件和根文档） | — | `README.md`, `CLAUDE.md`, `docs/` | 根文档 | 否 |
| 骨架线 | 待启动 | `$MAIN/.worktrees/skeleton` | `line/skeleton` | 除 `data/`、根文档、`.claude/`、`scripts/guard.sh`、`scripts/check.sh` 以外的所有路径（`backend/`、`frontend/`、`fixtures/`、`recordings/`） | `backend/app/schema.py`（契约代码）、`backend/app/main.py`、`frontend/src/types.ts`、依赖清单和锁文件（Integrator 出现前） | 否 |
| 上下文数据线 | 待启动 | `$MAIN/.worktrees/context-data` | `line/context-data` | `data/` | `data/ground_truth/`、`data/emails/` | 否 |
| Integrator | CP1 时启动 | `$MAIN` | `main` | 生成文件、依赖清单、锁文件（CP1 起） | | 唯一可以 push 的，每次要用户同意 |
| 核心线（暂定） | CP1 后 | 待定 | 待定 | `backend/` | | 否 |
| 前端线（暂定） | CP1 后 | 待定 | 待定 | `frontend/` | | 否 |

## 流程规则

- 每条线只在自己的路径、自己的分支、自己的端口里工作。提交，但不 push。
- 五份共享文件只在 `$MAIN` 里，worktree 里没有。用绝对路径读写。DECISIONS.md 只追加；新术语追加到 GLOSSARY.md，状态写 `proposed`。
- 合并进 `main` 由 Integrator 做，而且要用户先同意。
- 交接记录和合并请求写到 `$NOTES`，用模板 `~/.claude/skills/swarm-control/templates/handover.md` 和 `merge-request.md`。
- 护栏是绊线而不是墙：`scripts/guard.sh` 只能拦住常见写法（`/usr/bin/pkill`、`bash -c '...'`、`git -C . push` 拦不住），真正的墙是这些规则、Integrator 的流程和 pre-commit。

## 检查

| 名字 | 命令 | 状态 |
| --- | --- | --- |
| glossary | `scripts/check.sh __glossary` | 启用 |
| 其余（后端测试、前端构建、证据核对、fixture 校验） | 由骨架线在合并请求里提出 | 待用户批准 |

## 端到端走查

骨架线在 CP1 前补上：启动后端（8041）和前端（5181），依次跑 3 个例子，检查每个高亮的悬停卡片和原文。
