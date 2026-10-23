---
{
  "email": "sophie.lin@example.com",
  "display_name": "Sophie Lin",
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
        "quote": "Any chance you are free this Sunday afternoon?"
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
      "text": "Sophie is a casual personal friend of Mia's. Their emails are all about making social plans.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-friend_scheduling-003-m1",
          "quote": "Yes let's go!"
        }
      ]
    },
    {
      "id": "f2",
      "text": "In November 2024 they planned to try a milk tea place together and agreed to meet on a Sunday.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-friend_scheduling-003-m2",
          "quote": "see you Sunday :)"
        }
      ]
    },
    {
      "id": "f3",
      "text": "When planning the milk tea outing, Mia offered Sunday afternoon or Monday evening after 6.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-friend_scheduling-003-m1",
          "quote": "Monday evening\nafter 6 works too"
        }
      ]
    },
    {
      "id": "f4",
      "text": "In June 2025 Sophie offered to bring something over to Mia's home, and Mia called it sweet and invited her for tea.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-friend_scheduling-007-m1",
          "quote": "come by for tea anytime in those windows"
        }
      ]
    },
    {
      "id": "f5",
      "text": "Mia lives with at least one other person (she writes 'We're home'). She gave Sophie Saturday after 2pm or Sunday before 11 as times to drop by.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-friend_scheduling-007-m1",
          "quote": "We're home Saturday after 2pm or Sunday morning before 11"
        }
      ]
    },
    {
      "id": "f6",
      "text": "Sophie visits Mia at home for tea, so they likely live near each other.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-friend_scheduling-007-m1",
          "quote": "come by for tea"
        }
      ]
    },
    {
      "id": "f7",
      "text": "In April 2026 Sophie suggested a morning walk. Mia couldn't do the morning and offered the afternoon after 3 instead.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-friend_scheduling-011-m1",
          "quote": "Anytime after 3 is\ngood"
        }
      ]
    },
    {
      "id": "f8",
      "text": "Mia keeps plans flexible with Sophie and is happy to move them to another week.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-friend_scheduling-011-m1",
          "quote": "we can go next week too"
        }
      ]
    },
    {
      "id": "f9",
      "text": "Mia's tone with Sophie is warm and informal. Her emails are short and sometimes use emoticons.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-friend_scheduling-003-m2",
          "quote": "see you Sunday :)"
        }
      ]
    }
  ],
  "edges": [],
  "core_connection": {
    "text": "Sophie is a casual, friendly local friend. She and Mia make simple plans together, like trying a milk tea place, having tea at Mia's home and taking walks.",
    "evidence": [
      {
        "message_id": "syn-friend_scheduling-003-m1",
        "quote": "Yes let's go!"
      },
      {
        "message_id": "syn-friend_scheduling-007-m1",
        "quote": "come by for tea anytime in those windows"
      }
    ]
  },
  "external": []
}
---

# Sophie Lin

Sophie is a casual, friendly local friend. She and Mia make simple plans together, like trying a milk tea place, having tea at Mia's home and taking walks.

- Address (default): Sophie (3/4 emails)
- Sophie is a casual personal friend of Mia's. Their emails are all about making social plans.
- In November 2024 they planned to try a milk tea place together and agreed to meet on a Sunday.
- When planning the milk tea outing, Mia offered Sunday afternoon or Monday evening after 6.
- In June 2025 Sophie offered to bring something over to Mia's home, and Mia called it sweet and invited her for tea.
- Mia lives with at least one other person (she writes 'We're home'). She gave Sophie Saturday after 2pm or Sunday before 11 as times to drop by.
- Sophie visits Mia at home for tea, so they likely live near each other.
- In April 2026 Sophie suggested a morning walk. Mia couldn't do the morning and offered the afternoon after 3 instead.
- Mia keeps plans flexible with Sophie and is happy to move them to another week.
- Mia's tone with Sophie is warm and informal. Her emails are short and sometimes use emoticons.

_Extracted offline by pipeline/extract.py; every entry is backed by verified quotes._
