---
{
  "email": "kevin.chen@example.com",
  "display_name": "Kevin Chen",
  "relationship": "friend",
  "address_as": {
    "value": "Kevin",
    "count": 1,
    "total": 19,
    "status": "learned",
    "evidence": [
      {
        "message_id": "syn-zh_en_casual-014-m1",
        "quote": "Kevin"
      }
    ]
  },
  "address_as_by_context": [
    {
      "context": "default",
      "value": "Kevin",
      "count": 1,
      "total": 19,
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-zh_en_casual-014-m1",
          "quote": "Kevin"
        }
      ]
    }
  ],
  "honorific": {
    "value": "你",
    "count": 4,
    "total": 19,
    "status": "learned",
    "evidence": [
      {
        "message_id": "syn-zh_en_casual-014-m1",
        "quote": "今年 Costco 的月饼你们买了吗?"
      },
      {
        "message_id": "syn-zh_en_casual-006-m2",
        "quote": "你想拿它做什么?"
      },
      {
        "message_id": "syn-zh_en_casual-013-m1",
        "quote": "好奇你开五个是让它们同时做一个 task 吗"
      },
      {
        "message_id": "19cfa2a364325cd7",
        "quote": "你不担心隐私问题吗？"
      }
    ]
  },
  "sign_off": {
    "value": "Mia",
    "count": 2,
    "total": 19,
    "status": "learned",
    "evidence": [
      {
        "message_id": "syn-zh_en_casual-006-m1",
        "quote": "Mia"
      },
      {
        "message_id": "syn-zh_en_casual-018-m1",
        "quote": "Mia"
      }
    ]
  },
  "language": {
    "value": "mixed",
    "count": 8,
    "total": 19,
    "status": "learned",
    "evidence": [
      {
        "message_id": "syn-zh_en_casual-006-m1",
        "quote": "跑过 我的 Mac 32GB 内存跑 8B 很流畅"
      },
      {
        "message_id": "syn-zh_en_casual-006-m2",
        "quote": "比如把我随手存的 link 自动打 tag。"
      },
      {
        "message_id": "syn-zh_en_casual-006-m3",
        "quote": "Qwen 的 7B 中英文混着的也能分对"
      },
      {
        "message_id": "syn-zh_en_casual-009-m2",
        "quote": "read-only 好主意！我也去加一个"
      },
      {
        "message_id": "syn-zh_en_casual-013-m2",
        "quote": "写在 CLAUDE.md 里，每次说太累了。"
      },
      {
        "message_id": "syn-zh_en_casual-018-m1",
        "quote": "我们当时是把打分改成 pass/fail 不要 1 到 10 分"
      },
      {
        "message_id": "19cfa2a364325cd7",
        "quote": "好奇你的填表格用的是什么MCP呀？"
      },
      {
        "message_id": "syn-zh_en_casual-020-m1",
        "quote": "先用 Whisper 转 再让 Claude 按说话人分段"
      }
    ]
  },
  "facts": [
    {
      "id": "f1",
      "text": "Kevin is a tech friend and peer of Mia's. They trade hands-on AI and dev-tool tips, usually with Kevin asking a question and Mia answering.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-zh_en_casual-013-m1",
          "quote": "有！我现在都让每个 agent 只管自己的目录"
        }
      ]
    },
    {
      "id": "f2",
      "text": "Kevin writes a newsletter ('Notes from Kevin'). Mia replies to issues with follow-up questions, e.g. about his Obsidian MCP setup.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-zh_en_casual-009-m1",
          "quote": "我之前也想接 Obsidian 但是怕它乱改我的笔记"
        }
      ]
    },
    {
      "id": "f3",
      "text": "Feb 2025: Mia told Kevin her 32GB Mac runs 8B local models smoothly, but anything larger lags.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-zh_en_casual-006-m1",
          "quote": "跑过 我的 Mac 32GB 内存跑 8B 很流畅 再大就开始卡了😂"
        }
      ]
    },
    {
      "id": "f4",
      "text": "Mia uses a local Qwen 7B model to auto-tag her saved links, partly for privacy. She shared her prompt with Kevin.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-zh_en_casual-006-m3",
          "quote": "Qwen 的 7B 中英文混着的也能分对"
        },
        {
          "message_id": "syn-zh_en_casual-006-m2",
          "quote": "本地跑也不用担心隐私"
        },
        {
          "message_id": "syn-zh_en_casual-006-m3",
          "quote": "这是我的 prompt 你直接拿去改嘛"
        }
      ]
    },
    {
      "id": "f5",
      "text": "May 2025: Mia liked Kevin's idea of a read-only mode for his MCP and planned to add one herself. She agreed that grep is enough for a few thousand notes.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-zh_en_casual-009-m2",
          "quote": "read-only 好主意！我也去加一个"
        },
        {
          "message_id": "syn-zh_en_casual-009-m3",
          "quote": "纯属给自己找事嘛😂"
        }
      ]
    },
    {
      "id": "f6",
      "text": "Aug 2025: Mia gives each Claude Code subagent its own directory, set in CLAUDE.md and enforced by a hook. She sent Kevin a repo of example hooks.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-zh_en_casual-013-m2",
          "quote": "然后再加一个 hook，改了别人的目录就直接 block 掉。"
        },
        {
          "message_id": "syn-zh_en_casual-013-m3",
          "quote": "这个 repo 里有好几个 改改就能用嘛"
        }
      ]
    },
    {
      "id": "f7",
      "text": "Mid-Autumn 2025: Mia wished Kevin a happy festival and recommended Costco's 美心 custard mooncakes (red box).",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-zh_en_casual-014-m1",
          "quote": "中秋快乐！"
        },
        {
          "message_id": "syn-zh_en_casual-014-m2",
          "quote": "美心的 红色盒子那个"
        },
        {
          "message_id": "syn-zh_en_casual-014-m1",
          "quote": "我觉得流心那款比去年好吃"
        }
      ]
    },
    {
      "id": "f8",
      "text": "Feb 2026: Mia drew on her own past experience to advise Kevin on LLM-as-judge: pass/fail grading, one criterion per call, run calls in parallel.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-zh_en_casual-018-m1",
          "quote": "然后每条标准单独问一次 不让它一次看全部"
        },
        {
          "message_id": "syn-zh_en_casual-018-m2",
          "quote": "可以并发跑，几千条其实还好。"
        }
      ]
    },
    {
      "id": "f9",
      "text": "Mia also told Kevin to use a different model as the judge and to spot-check 100 samples by hand.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-zh_en_casual-018-m3",
          "quote": "换一个 model 当 judge 再抽一百条人工对一下"
        }
      ]
    },
    {
      "id": "f10",
      "text": "Mar 2026: Mia questioned the privacy of Kevin using an MCP to fill in tax forms.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "19cfa2a364325cd7",
          "quote": "尤其是税务的话，你不担心隐私问题吗？"
        },
        {
          "message_id": "19cfa37efd3a794e",
          "quote": "因为你的信息都被明文给model了😂"
        }
      ]
    },
    {
      "id": "f11",
      "text": "Apr 2026: Mia described her transcription setup to Kevin: Whisper, then Claude to split by speaker, with a glossary at the top of the prompt.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-zh_en_casual-020-m1",
          "quote": "先用 Whisper 转 再让 Claude 按说话人分段"
        },
        {
          "message_id": "syn-zh_en_casual-020-m2",
          "quote": "放在 prompt 最前面 几十个词"
        }
      ]
    },
    {
      "id": "f12",
      "text": "Kevin wanted to transcribe audio (meeting or podcast). Mia warned him to tell the model not to polish his spoken style.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-zh_en_casual-020-m2",
          "quote": "好奇你是要转会议还是 podcast?"
        },
        {
          "message_id": "syn-zh_en_casual-020-m3",
          "quote": "记得在 prompt 里让它别润色"
        }
      ]
    },
    {
      "id": "f13",
      "text": "Mia's tone with Kevin is casual: she often opens with '好奇', uses 😂, and ends sentences with 嘛/啦.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-zh_en_casual-009-m2",
          "quote": "好奇它搜索是用 embedding 还是直接 grep?"
        },
        {
          "message_id": "syn-zh_en_casual-018-m3",
          "quote": "心里就有数啦"
        }
      ]
    }
  ],
  "edges": [],
  "core_connection": {
    "text": "Kevin and Mia are tech friends who regularly swap practical tips on AI tools (local models, MCP, Claude Code, LLM-as-judge, transcription). Mia often replies to his newsletter issues with curious questions.",
    "evidence": [
      {
        "message_id": "syn-zh_en_casual-013-m1",
        "quote": "好奇你开五个是让它们同时做一个 task 吗"
      },
      {
        "message_id": "syn-zh_en_casual-009-m1",
        "quote": "好奇你这个 local MCP 是自己写的还是用现成的？"
      }
    ]
  },
  "external": []
}
---

# Kevin Chen

Kevin and Mia are tech friends who regularly swap practical tips on AI tools (local models, MCP, Claude Code, LLM-as-judge, transcription). Mia often replies to his newsletter issues with curious questions.

- Address (default): Kevin (1/19 emails)
- Kevin is a tech friend and peer of Mia's. They trade hands-on AI and dev-tool tips, usually with Kevin asking a question and Mia answering.
- Kevin writes a newsletter ('Notes from Kevin'). Mia replies to issues with follow-up questions, e.g. about his Obsidian MCP setup.
- Feb 2025: Mia told Kevin her 32GB Mac runs 8B local models smoothly, but anything larger lags.
- Mia uses a local Qwen 7B model to auto-tag her saved links, partly for privacy. She shared her prompt with Kevin.
- May 2025: Mia liked Kevin's idea of a read-only mode for his MCP and planned to add one herself. She agreed that grep is enough for a few thousand notes.
- Aug 2025: Mia gives each Claude Code subagent its own directory, set in CLAUDE.md and enforced by a hook. She sent Kevin a repo of example hooks.
- Mid-Autumn 2025: Mia wished Kevin a happy festival and recommended Costco's 美心 custard mooncakes (red box).
- Feb 2026: Mia drew on her own past experience to advise Kevin on LLM-as-judge: pass/fail grading, one criterion per call, run calls in parallel.
- Mia also told Kevin to use a different model as the judge and to spot-check 100 samples by hand.
- Mar 2026: Mia questioned the privacy of Kevin using an MCP to fill in tax forms.
- Apr 2026: Mia described her transcription setup to Kevin: Whisper, then Claude to split by speaker, with a glossary at the top of the prompt.
- Kevin wanted to transcribe audio (meeting or podcast). Mia warned him to tell the model not to polish his spoken style.
- Mia's tone with Kevin is casual: she often opens with '好奇', uses 😂, and ends sentences with 嘛/啦.

_Extracted offline by pipeline/extract.py; every entry is backed by verified quotes._
