---
{
  "email": "marco.rossi@example.com",
  "display_name": "Marco Rossi",
  "relationship": "running friend",
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
        "quote": "Thanks,"
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
        "quote": "I'm doing the shorter loop."
      },
      {
        "message_id": "syn-friend_scheduling-002-m2",
        "quote": "Perfect, see you there!"
      },
      {
        "message_id": "syn-friend_scheduling-006-m1",
        "quote": "Please don't wait for me to order."
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
      "text": "Mia runs the shorter loop on the group long runs, so she sometimes gets to coffee about 10 minutes late.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-friend_scheduling-002-m1",
          "quote": "I might be 10 min latter since"
        },
        {
          "message_id": "syn-friend_scheduling-002-m1",
          "quote": "I'm doing the shorter loop."
        }
      ]
    },
    {
      "id": "f2",
      "text": "In October 2024 Mia joined Marco's group for coffee after their Saturday long run.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-friend_scheduling-002-m1",
          "quote": "I'm in！"
        }
      ]
    },
    {
      "id": "f3",
      "text": "In May 2025 Mia overslept and asked to move their post-run coffee from 8:00 to 8:30. She told Marco not to wait for her to order.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-friend_scheduling-006-m1",
          "quote": "my alarm didn't went off"
        },
        {
          "message_id": "syn-friend_scheduling-006-m1",
          "quote": "coffee to 8:30?"
        }
      ]
    },
    {
      "id": "f4",
      "text": "Mia would rather plan in person after the run than over a call.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-friend_scheduling-010-m1",
          "quote": "in person after the run instead of a call?"
        }
      ]
    },
    {
      "id": "f5",
      "text": "In January 2026 Mia suggested the Starbucks by the park, because the other coffee shop had been too crowded the week before.",
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
    "text": "Marco and Mia run in the same group, and they often get coffee after the long runs.",
    "evidence": [
      {
        "message_id": "syn-friend_scheduling-002-m1",
        "quote": "Which coffee shop are you guys going to?"
      },
      {
        "message_id": "syn-friend_scheduling-006-m1",
        "quote": "Could we push"
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

Marco and Mia run in the same group, and they often get coffee after the long runs.

- Address (default): Marco (3/4 emails)
- Mia runs the shorter loop on the group long runs, so she sometimes gets to coffee about 10 minutes late.
- In October 2024 Mia joined Marco's group for coffee after their Saturday long run.
- In May 2025 Mia overslept and asked to move their post-run coffee from 8:00 to 8:30. She told Marco not to wait for her to order.
- Mia would rather plan in person after the run than over a call.
- In January 2026 Mia suggested the Starbucks by the park, because the other coffee shop had been too crowded the week before.

_Extracted offline by pipeline/extract.py; every entry is backed by verified quotes._
