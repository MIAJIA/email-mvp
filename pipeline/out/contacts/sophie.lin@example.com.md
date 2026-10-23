---
{
  "email": "sophie.lin@example.com",
  "display_name": "Sophie",
  "relationship": "friend",
  "address_as": {
    "value": "Sophie",
    "count": 3,
    "total": 4,
    "status": "learned",
    "evidence": [
      {
        "message_id": "syn-friend_scheduling-003-m1",
        "quote": "Hey Sophie,"
      },
      {
        "message_id": "syn-friend_scheduling-007-m1",
        "quote": "Hi Sophie,"
      },
      {
        "message_id": "syn-friend_scheduling-011-m1",
        "quote": "Hey Sophie,"
      }
    ]
  },
  "address_as_by_context": [
    {
      "context": "default",
      "value": "Sophie",
      "count": 3,
      "total": 4,
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-friend_scheduling-003-m1",
          "quote": "Hey Sophie,"
        },
        {
          "message_id": "syn-friend_scheduling-007-m1",
          "quote": "Hi Sophie,"
        },
        {
          "message_id": "syn-friend_scheduling-011-m1",
          "quote": "Hey Sophie,"
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
        "message_id": "syn-friend_scheduling-003-m1",
        "quote": "Mia"
      },
      {
        "message_id": "syn-friend_scheduling-003-m2",
        "quote": "Mia"
      },
      {
        "message_id": "syn-friend_scheduling-007-m1",
        "quote": "Thanks,"
      },
      {
        "message_id": "syn-friend_scheduling-011-m1",
        "quote": "Best,"
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
        "message_id": "syn-friend_scheduling-003-m1",
        "quote": "Yes let's go!"
      },
      {
        "message_id": "syn-friend_scheduling-003-m2",
        "quote": "Sounds good, see you Sunday :)"
      },
      {
        "message_id": "syn-friend_scheduling-007-m1",
        "quote": "That's so sweet of you！"
      },
      {
        "message_id": "syn-friend_scheduling-011-m1",
        "quote": "Tomorrow morning is a bit tight for me"
      }
    ]
  },
  "facts": [
    {
      "id": "f1",
      "text": "In November 2024 Mia agreed to go to a milk tea place with Sophie and suggested Sunday afternoon or Monday evening after 6. They settled on Sunday.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-friend_scheduling-003-m1",
          "quote": "free this Sunday afternoon?"
        },
        {
          "message_id": "syn-friend_scheduling-003-m1",
          "quote": "Monday evening"
        },
        {
          "message_id": "syn-friend_scheduling-003-m2",
          "quote": "see you Sunday :)"
        }
      ]
    },
    {
      "id": "f2",
      "text": "In June 2025 Sophie offered to drop by. Mia invited her over for tea on Saturday after 2pm or Sunday before 11.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-friend_scheduling-007-m1",
          "quote": "Saturday after 2pm or Sunday morning before 11"
        },
        {
          "message_id": "syn-friend_scheduling-007-m1",
          "quote": "come by for tea anytime"
        }
      ]
    },
    {
      "id": "f3",
      "text": "Mia writes 'we' about being home, so she probably lives with someone. Sophie visits her at home.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-friend_scheduling-007-m1",
          "quote": "We're home"
        }
      ]
    },
    {
      "id": "f4",
      "text": "In April 2026 Sophie suggested a walk. Mia couldn't make the morning and offered any time after 3pm, or the next week.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-friend_scheduling-011-m1",
          "quote": "Tomorrow morning is a bit tight for me"
        },
        {
          "message_id": "syn-friend_scheduling-011-m1",
          "quote": "Anytime after 3 is"
        },
        {
          "message_id": "syn-friend_scheduling-011-m1",
          "quote": "we can go next week too"
        }
      ]
    },
    {
      "id": "f5",
      "text": "Mia's emails to Sophie are short and warm. She offers specific time windows and adds an easy way out, such as 'no worries'.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-friend_scheduling-011-m1",
          "quote": "No worries if it's not available"
        }
      ]
    }
  ],
  "edges": [],
  "core_connection": {
    "text": "Sophie is a casual friend who seems to live nearby. She and Mia meet up for milk tea, tea at home and walks, and Sophie usually suggests the plans.",
    "evidence": [
      {
        "message_id": "syn-friend_scheduling-003-m1",
        "quote": "Yes let's go!"
      },
      {
        "message_id": "syn-friend_scheduling-007-m1",
        "quote": "come by for tea anytime"
      },
      {
        "message_id": "syn-friend_scheduling-011-m1",
        "quote": "we can go next week too"
      }
    ]
  },
  "external": []
}
---

# Sophie

Sophie is a casual friend who seems to live nearby. She and Mia meet up for milk tea, tea at home and walks, and Sophie usually suggests the plans.

- Address (default): Sophie (3/4 emails)
- In November 2024 Mia agreed to go to a milk tea place with Sophie and suggested Sunday afternoon or Monday evening after 6. They settled on Sunday.
- In June 2025 Sophie offered to drop by. Mia invited her over for tea on Saturday after 2pm or Sunday before 11.
- Mia writes 'we' about being home, so she probably lives with someone. Sophie visits her at home.
- In April 2026 Sophie suggested a walk. Mia couldn't make the morning and offered any time after 3pm, or the next week.
- Mia's emails to Sophie are short and warm. She offers specific time windows and adds an easy way out, such as 'no worries'.

_Extracted offline by pipeline/extract.py; every entry is backed by verified quotes._
