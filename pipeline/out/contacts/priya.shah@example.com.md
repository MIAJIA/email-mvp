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
      "text": "Priya is a personal friend of Mia's. They meet for coffee, lunch and video calls to catch up.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-friend_scheduling-001-m1",
          "quote": "It's been way too long since we last caught up!"
        }
      ]
    },
    {
      "id": "f2",
      "text": "Priya works from an office, and Mia has suggested meeting somewhere near it.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-friend_scheduling-001-m1",
          "quote": "maybe Red Rock or somewhere near your office?"
        }
      ]
    },
    {
      "id": "f3",
      "text": "In September 2024 they met for coffee on a Thursday at 10am at Red Rock, which is a place they both know.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-friend_scheduling-001-m2",
          "quote": "See you Thursday 10am at Red Rock"
        }
      ]
    },
    {
      "id": "f4",
      "text": "Priya lives on Pacific time (PST).",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-friend_scheduling-005-m1",
          "quote": "That should be 5pm Pst the day before on your side."
        }
      ]
    },
    {
      "id": "f5",
      "text": "In March 2025 Mia was in Singapore for about two more weeks, and they had a video call at 9:00AM Singapore time, which was 5pm PST the day before for Priya.",
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
      "id": "f6",
      "text": "In August 2025 Priya had to move their Thursday lunch. Mia was fine with it but asked to meet in person the next Tuesday or Wednesday instead of a call.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-friend_scheduling-008-m1",
          "quote": "Totally fine!"
        },
        {
          "message_id": "syn-friend_scheduling-008-m1",
          "quote": "Can we meet in person next Tue or Wed?"
        }
      ]
    },
    {
      "id": "f7",
      "text": "They have a usual lunch spot, and Mia agreed to go back there. She also suggested a milk tea shop right next to it that has good food.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-friend_scheduling-008-m2",
          "quote": "Same place works for me!"
        },
        {
          "message_id": "syn-friend_scheduling-008-m2",
          "quote": "there's a milk tea"
        }
      ]
    },
    {
      "id": "f8",
      "text": "Mia's tone with Priya is casual and warm, and she uses emoji in short replies.",
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
    "text": "Priya is a friend of Mia's. They keep in touch through coffee, lunch and the occasional video call, and Mia likes to meet in person.",
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

Priya is a friend of Mia's. They keep in touch through coffee, lunch and the occasional video call, and Mia likes to meet in person.

- Address (default): Priya (3/6 emails)
- Priya is a personal friend of Mia's. They meet for coffee, lunch and video calls to catch up.
- Priya works from an office, and Mia has suggested meeting somewhere near it.
- In September 2024 they met for coffee on a Thursday at 10am at Red Rock, which is a place they both know.
- Priya lives on Pacific time (PST).
- In March 2025 Mia was in Singapore for about two more weeks, and they had a video call at 9:00AM Singapore time, which was 5pm PST the day before for Priya.
- In August 2025 Priya had to move their Thursday lunch. Mia was fine with it but asked to meet in person the next Tuesday or Wednesday instead of a call.
- They have a usual lunch spot, and Mia agreed to go back there. She also suggested a milk tea shop right next to it that has good food.
- Mia's tone with Priya is casual and warm, and she uses emoji in short replies.

_Extracted offline by pipeline/extract.py; every entry is backed by verified quotes._
