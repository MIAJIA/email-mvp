---
{
  "email": "hang.zhou@example.com",
  "display_name": "周航",
  "relationship": "friend",
  "address_as": {
    "value": "周航",
    "count": 1,
    "total": 14,
    "status": "learned",
    "evidence": [
      {
        "message_id": "syn-zh_en_casual-001-m1",
        "quote": "周航"
      }
    ]
  },
  "address_as_by_context": [
    {
      "context": "default",
      "value": "周航",
      "count": 1,
      "total": 14,
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-zh_en_casual-001-m1",
          "quote": "周航"
        }
      ]
    }
  ],
  "honorific": {
    "value": "你",
    "count": 5,
    "total": 14,
    "status": "learned",
    "evidence": [
      {
        "message_id": "syn-zh_en_casual-001-m3",
        "quote": "好奇你平时是用 Unity 吗?"
      },
      {
        "message_id": "syn-zh_en_casual-010-m1",
        "quote": "好奇你现在大概多长?"
      },
      {
        "message_id": "syn-zh_en_casual-011-m3",
        "quote": "你没遇到过吗?"
      },
      {
        "message_id": "syn-zh_en_casual-021-m1",
        "quote": "好奇你 description 现在怎么写的"
      },
      {
        "message_id": "syn-zh_en_casual-021-m3",
        "quote": "你的 skill 现在多长?"
      }
    ]
  },
  "language": {
    "value": "mixed",
    "count": 8,
    "total": 14,
    "status": "learned",
    "evidence": [
      {
        "message_id": "syn-zh_en_casual-001-m1",
        "quote": "装一个 blender-mcp 的 plugin"
      },
      {
        "message_id": "syn-zh_en_casual-001-m2",
        "quote": "道具先用 Tripo 生成"
      },
      {
        "message_id": "syn-zh_en_casual-001-m3",
        "quote": "单文件 index.html 就跑起来了"
      },
      {
        "message_id": "syn-zh_en_casual-010-m2",
        "quote": "全大写的那些现在的 model 反而会过度执行"
      },
      {
        "message_id": "syn-zh_en_casual-010-m3",
        "quote": "就能自己判断 edge case"
      },
      {
        "message_id": "syn-zh_en_casual-011-m2",
        "quote": "我看 diff 和测试"
      },
      {
        "message_id": "syn-zh_en_casual-011-m3",
        "quote": "它特别喜欢偷偷改测试让它 pass"
      },
      {
        "message_id": "syn-zh_en_casual-021-m2",
        "quote": "要 trigger 的词我中英文一起写"
      }
    ]
  },
  "facts": [
    {
      "id": "f1",
      "text": "周航 is a casual friend; the tone is relaxed, with emoji and 哈哈/啦, and Mia uses no sign-off.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-zh_en_casual-001-m2",
          "quote": "只能做方方正正的低多边形😂"
        }
      ]
    },
    {
      "id": "f2",
      "text": "In Sep 2024 Mia told 周航 she uses blender-mcp with Claude to build a pirate mini-game for practice.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-zh_en_casual-001-m1",
          "quote": "我在做一个海盗小游戏练手哈哈"
        }
      ]
    },
    {
      "id": "f3",
      "text": "Mia explained her pipeline: Tripo generates the props, and Claude fixes their size and pivot.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-zh_en_casual-001-m2",
          "quote": "道具先用 Tripo 生成 Claude 负责整理尺寸和轴心"
        }
      ]
    },
    {
      "id": "f4",
      "text": "Mia builds the game in Three.js instead of Unity. She asked whether 周航 usually uses Unity, but the emails don't give the answer.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-zh_en_casual-001-m3",
          "quote": "Three.js！单文件 index.html 就跑起来了"
        },
        {
          "message_id": "syn-zh_en_casual-001-m3",
          "quote": "好奇你平时是用 Unity 吗?"
        }
      ]
    },
    {
      "id": "f5",
      "text": "In Dec 2024 they hiked Mission Peak together on a Saturday, meeting at the parking lot at 7:30. Mia brought fruit.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-zh_en_casual-004-m1",
          "quote": "几点停车场集合？太晚就没位置了"
        },
        {
          "message_id": "syn-zh_en_casual-004-m2",
          "quote": "七点半可以 我带点水果"
        }
      ]
    },
    {
      "id": "f6",
      "text": "They have hiked together before. Last time they came down too fast, so Mia wanted to take it slower.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-zh_en_casual-004-m2",
          "quote": "上次下山走太快了 这次慢慢走啦"
        }
      ]
    },
    {
      "id": "f7",
      "text": "In Jun 2025 周航's system prompt had grown to about 2,000 characters. Mia advised keeping the role, the task and the 3 or 4 rules most often broken, and adding a reason after each rule.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-zh_en_casual-010-m1",
          "quote": "只写最容易错的三四条"
        },
        {
          "message_id": "syn-zh_en_casual-010-m2",
          "quote": "哈哈两千字太长了"
        },
        {
          "message_id": "syn-zh_en_casual-010-m2",
          "quote": "可以试试每条后面写一句为什么"
        }
      ]
    },
    {
      "id": "f8",
      "text": "In Jul 2025 周航 was deciding between Cursor and Claude Code. Mia mostly uses Claude Code and Cursor only for small edits.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-zh_en_casual-011-m1",
          "quote": "现在基本都是 Claude Code 了"
        },
        {
          "message_id": "syn-zh_en_casual-011-m1",
          "quote": "Cursor 改小地方还是快"
        }
      ]
    },
    {
      "id": "f9",
      "text": "Mia reviews agent code by looking at the diff and the tests, and she writes some tests herself because agents sometimes change tests to make them pass.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-zh_en_casual-011-m2",
          "quote": "不会每行看 我看 diff 和测试"
        },
        {
          "message_id": "syn-zh_en_casual-011-m3",
          "quote": "所以测试我会先自己写几个"
        }
      ]
    },
    {
      "id": "f10",
      "text": "In May 2026 周航 was writing Claude skills that often didn't trigger. Mia advised a concrete description with trigger words in both Chinese and English, a short main file and long examples in separate files.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-zh_en_casual-021-m1",
          "quote": "要把用户真的会说的话写进去"
        },
        {
          "message_id": "syn-zh_en_casual-021-m2",
          "quote": "要 trigger 的词我中英文一起写"
        },
        {
          "message_id": "syn-zh_en_casual-021-m3",
          "quote": "主文件尽量短，一两百行。"
        }
      ]
    },
    {
      "id": "f11",
      "text": "Mia often ends her advice by asking about 周航's own setup (prompt length, skill length, description).",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-zh_en_casual-010-m1",
          "quote": "好奇你现在大概多长?"
        },
        {
          "message_id": "syn-zh_en_casual-021-m3",
          "quote": "你的 skill 现在多长?"
        }
      ]
    }
  ],
  "edges": [],
  "core_connection": {
    "text": "A friend who hikes with Mia and often asks her practical questions about AI tools: Blender MCP, system prompts, Claude Code and Claude skills.",
    "evidence": [
      {
        "message_id": "syn-zh_en_casual-004-m1",
        "quote": "走！几点停车场集合？"
      },
      {
        "message_id": "syn-zh_en_casual-011-m1",
        "quote": "现在基本都是 Claude Code 了"
      },
      {
        "message_id": "syn-zh_en_casual-021-m1",
        "quote": "不触发多半是 description 写得太抽象"
      }
    ]
  },
  "external": []
}
---

# 周航

A friend who hikes with Mia and often asks her practical questions about AI tools: Blender MCP, system prompts, Claude Code and Claude skills.

- Address (default): 周航 (1/14 emails)
- 周航 is a casual friend; the tone is relaxed, with emoji and 哈哈/啦, and Mia uses no sign-off.
- In Sep 2024 Mia told 周航 she uses blender-mcp with Claude to build a pirate mini-game for practice.
- Mia explained her pipeline: Tripo generates the props, and Claude fixes their size and pivot.
- Mia builds the game in Three.js instead of Unity. She asked whether 周航 usually uses Unity, but the emails don't give the answer.
- In Dec 2024 they hiked Mission Peak together on a Saturday, meeting at the parking lot at 7:30. Mia brought fruit.
- They have hiked together before. Last time they came down too fast, so Mia wanted to take it slower.
- In Jun 2025 周航's system prompt had grown to about 2,000 characters. Mia advised keeping the role, the task and the 3 or 4 rules most often broken, and adding a reason after each rule.
- In Jul 2025 周航 was deciding between Cursor and Claude Code. Mia mostly uses Claude Code and Cursor only for small edits.
- Mia reviews agent code by looking at the diff and the tests, and she writes some tests herself because agents sometimes change tests to make them pass.
- In May 2026 周航 was writing Claude skills that often didn't trigger. Mia advised a concrete description with trigger words in both Chinese and English, a short main file and long examples in separate files.
- Mia often ends her advice by asking about 周航's own setup (prompt length, skill length, description).

_Extracted offline by pipeline/extract.py; every entry is backed by verified quotes._
