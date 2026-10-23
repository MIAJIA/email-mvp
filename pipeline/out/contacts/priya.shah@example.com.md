---
{
  "email": "priya.shah@example.com",
  "display_name": "Priya Shah",
  "relationship": "friend",
  "address_as": {
    "value": "Priya",
    "count": 3,
    "total": 6,
    "status": "learned",
    "evidence": [
      {
        "message_id": "syn-friend_scheduling-001-m1",
        "quote": "Hi Priya,"
      },
      {
        "message_id": "syn-friend_scheduling-005-m1",
        "quote": "Hey Priya,"
      },
      {
        "message_id": "syn-friend_scheduling-008-m2",
        "quote": "Hi Priya,"
      }
    ]
  },
  "address_as_by_context": [
    {
      "context": "default",
      "value": "Priya",
      "count": 3,
      "total": 6,
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-friend_scheduling-001-m1",
          "quote": "Hi Priya,"
        },
        {
          "message_id": "syn-friend_scheduling-005-m1",
          "quote": "Hey Priya,"
        },
        {
          "message_id": "syn-friend_scheduling-008-m2",
          "quote": "Hi Priya,"
        }
      ]
    }
  ],
  "sign_off": {
    "value": "Best, Mia",
    "count": 2,
    "total": 6,
    "status": "learned",
    "evidence": [
      {
        "message_id": "syn-friend_scheduling-001-m1",
        "quote": "Best,"
      },
      {
        "message_id": "syn-friend_scheduling-008-m2",
        "quote": "Best,"
      }
    ]
  },
  "language": {
    "value": "en",
    "count": 5,
    "total": 6,
    "status": "learned",
    "evidence": [
      {
        "message_id": "syn-friend_scheduling-001-m1",
        "quote": "Are you around next week for"
      },
      {
        "message_id": "syn-friend_scheduling-005-m1",
        "quote": "Yes, still here for two more weeks!"
      },
      {
        "message_id": "syn-friend_scheduling-005-m2",
        "quote": "talk to you tomorrow"
      },
      {
        "message_id": "syn-friend_scheduling-008-m1",
        "quote": "Totally fine!"
      },
      {
        "message_id": "syn-friend_scheduling-008-m2",
        "quote": "Same place works for me!"
      }
    ]
  },
  "facts": [
    {
      "id": "f1",
      "text": "In September 2024 they met for coffee at Red Rock on Thursday at 10am. Mia had suggested Red Rock or a place near Priya's office.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-friend_scheduling-001-m2",
          "quote": "See you Thursday 10am at Red Rock"
        },
        {
          "message_id": "syn-friend_scheduling-001-m1",
          "quote": "maybe Red Rock or somewhere near your office?"
        }
      ]
    },
    {
      "id": "f2",
      "text": "Priya works in an office and lives in the Pacific time zone (PST).",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-friend_scheduling-005-m1",
          "quote": "That should be 5pm Pst the day before on your side."
        }
      ]
    },
    {
      "id": "f3",
      "text": "In March 2025 Mia was in Singapore for two more weeks, and they set up a video call at 9:00AM Singapore time.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-friend_scheduling-005-m1",
          "quote": "Yes, still here for two more weeks!"
        },
        {
          "message_id": "syn-friend_scheduling-005-m1",
          "quote": "Would 9:00AM Singapore time work for you ?"
        }
      ]
    },
    {
      "id": "f4",
      "text": "In August 2025 Priya called off a Thursday lunch. Mia asked to meet in person the next week instead of doing a call, and they met at the same place as before.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-friend_scheduling-008-m1",
          "quote": "Totally fine! Can we meet in person next Tue or Wed?"
        },
        {
          "message_id": "syn-friend_scheduling-008-m2",
          "quote": "Same place works for me!"
        }
      ]
    },
    {
      "id": "f5",
      "text": "Mia suggested a milk tea shop next to their usual lunch place as a new option.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-friend_scheduling-008-m2",
          "quote": "there's a milk tea"
        }
      ]
    },
    {
      "id": "f6",
      "text": "Mia writes to Priya in a casual, warm way, often using emoji.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-friend_scheduling-001-m2",
          "quote": "Red Rock 😊"
        },
        {
          "message_id": "syn-friend_scheduling-005-m2",
          "quote": "talk to you tomorrow 😁"
        }
      ]
    }
  ],
  "edges": [],
  "core_connection": {
    "text": "Priya is a friend of Mia's. They keep in touch through coffee, lunch and video calls. Mia prefers to meet in person.",
    "evidence": [
      {
        "message_id": "syn-friend_scheduling-001-m1",
        "quote": "It's been way too long since we last caught up!"
      },
      {
        "message_id": "syn-friend_scheduling-008-m1",
        "quote": "Can we meet in person next Tue or Wed?"
      }
    ]
  },
  "external": []
}
---

# Priya Shah

Priya is a friend of Mia's. They keep in touch through coffee, lunch and video calls. Mia prefers to meet in person.

- Address (default): Priya (3/6 emails)
- In September 2024 they met for coffee at Red Rock on Thursday at 10am. Mia had suggested Red Rock or a place near Priya's office.
- Priya works in an office and lives in the Pacific time zone (PST).
- In March 2025 Mia was in Singapore for two more weeks, and they set up a video call at 9:00AM Singapore time.
- In August 2025 Priya called off a Thursday lunch. Mia asked to meet in person the next week instead of doing a call, and they met at the same place as before.
- Mia suggested a milk tea shop next to their usual lunch place as a new option.
- Mia writes to Priya in a casual, warm way, often using emoji.

_Extracted offline by pipeline/extract.py; every entry is backed by verified quotes._
