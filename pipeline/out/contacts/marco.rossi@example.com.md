---
{
  "email": "marco.rossi@example.com",
  "display_name": "Marco Rossi",
  "relationship": "friend",
  "address_as": {
    "value": "Marco",
    "count": 3,
    "total": 4,
    "status": "learned",
    "evidence": [
      {
        "message_id": "syn-friend_scheduling-002-m1",
        "quote": "Hey Marco,"
      },
      {
        "message_id": "syn-friend_scheduling-006-m1",
        "quote": "Hey Marco ,"
      },
      {
        "message_id": "syn-friend_scheduling-010-m1",
        "quote": "Hi Marco,"
      }
    ]
  },
  "address_as_by_context": [
    {
      "context": "default",
      "value": "Marco",
      "count": 3,
      "total": 4,
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-friend_scheduling-002-m1",
          "quote": "Hey Marco,"
        },
        {
          "message_id": "syn-friend_scheduling-006-m1",
          "quote": "Hey Marco ,"
        },
        {
          "message_id": "syn-friend_scheduling-010-m1",
          "quote": "Hi Marco,"
        }
      ]
    }
  ],
  "sign_off": {
    "value": "Mia",
    "count": 4,
    "total": 4,
    "status": "learned",
    "evidence": [
      {
        "message_id": "syn-friend_scheduling-002-m1",
        "quote": "Mia"
      },
      {
        "message_id": "syn-friend_scheduling-002-m2",
        "quote": "Mia"
      },
      {
        "message_id": "syn-friend_scheduling-006-m1",
        "quote": "Mia"
      },
      {
        "message_id": "syn-friend_scheduling-010-m1",
        "quote": "Mia"
      }
    ]
  },
  "language": {
    "value": "en",
    "count": 4,
    "total": 4,
    "status": "learned",
    "evidence": [
      {
        "message_id": "syn-friend_scheduling-002-m1",
        "quote": "I'm in！"
      },
      {
        "message_id": "syn-friend_scheduling-002-m2",
        "quote": "Perfect, see you there!"
      },
      {
        "message_id": "syn-friend_scheduling-006-m1",
        "quote": "So sorry"
      },
      {
        "message_id": "syn-friend_scheduling-010-m1",
        "quote": "Sunday works!"
      }
    ]
  },
  "facts": [
    {
      "id": "f1",
      "text": "Marco is a friend Mia runs with. He organises coffee after the group runs.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-friend_scheduling-002-m1",
          "quote": "I'm in！"
        }
      ]
    },
    {
      "id": "f2",
      "text": "Marco runs with a group of other people, and the whole group goes for coffee together.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-friend_scheduling-002-m1",
          "quote": "Which coffee shop are you guys going to?"
        }
      ]
    },
    {
      "id": "f3",
      "text": "Mia sometimes does the shorter loop, so she may arrive at coffee about 10 minutes after the others.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-friend_scheduling-002-m1",
          "quote": "I'm doing the shorter loop."
        },
        {
          "message_id": "syn-friend_scheduling-002-m1",
          "quote": "I might be 10 min latter since"
        }
      ]
    },
    {
      "id": "f4",
      "text": "In October 2024, Mia agreed to join Marco and the group for coffee after a Saturday long run.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-friend_scheduling-002-m2",
          "quote": "Perfect, see you there!"
        }
      ]
    },
    {
      "id": "f5",
      "text": "In May 2025, Mia overslept and asked to move their post-run coffee to 8:30. She told the others not to wait for her to order.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-friend_scheduling-006-m1",
          "quote": "my alarm didn't went off"
        },
        {
          "message_id": "syn-friend_scheduling-006-m1",
          "quote": "coffee to 8:30?"
        },
        {
          "message_id": "syn-friend_scheduling-006-m1",
          "quote": "Please don't wait for me to order."
        }
      ]
    },
    {
      "id": "f6",
      "text": "In January 2026, the group run moved to Sunday. Mia said Sunday worked for her.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-friend_scheduling-010-m1",
          "quote": "Sunday works!"
        }
      ]
    },
    {
      "id": "f7",
      "text": "Mia would rather plan things in person after the run than on a call.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-friend_scheduling-010-m1",
          "quote": "in person after the run instead of a call?"
        }
      ]
    },
    {
      "id": "f8",
      "text": "They meet at Starbucks. Mia suggested the one by the park because the other one had been too crowded.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-friend_scheduling-010-m1",
          "quote": "Maybe at the Starbuck by the park"
        },
        {
          "message_id": "syn-friend_scheduling-010-m1",
          "quote": "the other one was so crowded last week."
        }
      ]
    }
  ],
  "edges": [],
  "core_connection": {
    "text": "Marco is a running buddy. Mia and Marco do group long runs together and usually get coffee afterwards.",
    "evidence": [
      {
        "message_id": "syn-friend_scheduling-002-m1",
        "quote": "Which coffee shop are you guys going to?"
      },
      {
        "message_id": "syn-friend_scheduling-010-m1",
        "quote": "in person after the run"
      }
    ]
  },
  "external": []
}
---

# Marco Rossi

Marco is a running buddy. Mia and Marco do group long runs together and usually get coffee afterwards.

- Address (default): Marco (3/4 emails)
- Marco is a friend Mia runs with. He organises coffee after the group runs.
- Marco runs with a group of other people, and the whole group goes for coffee together.
- Mia sometimes does the shorter loop, so she may arrive at coffee about 10 minutes after the others.
- In October 2024, Mia agreed to join Marco and the group for coffee after a Saturday long run.
- In May 2025, Mia overslept and asked to move their post-run coffee to 8:30. She told the others not to wait for her to order.
- In January 2026, the group run moved to Sunday. Mia said Sunday worked for her.
- Mia would rather plan things in person after the run than on a call.
- They meet at Starbucks. Mia suggested the one by the park because the other one had been too crowded.

_Extracted offline by pipeline/extract.py; every entry is backed by verified quotes._
