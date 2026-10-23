---
{
  "email": "hi@cursor.example.com",
  "display_name": "Cursor Support",
  "relationship": "customer support",
  "address_as": {
    "value": "Cursor Support",
    "count": 3,
    "total": 5,
    "status": "learned",
    "evidence": [
      {
        "message_id": "syn-refund_complaint-001-m1",
        "quote": "Hello Cursor Support,"
      },
      {
        "message_id": "syn-refund_complaint-012-m1",
        "quote": "Hello Cursor Support,"
      },
      {
        "message_id": "syn-refund_complaint-012-m3",
        "quote": "Hello Cursor Support,"
      }
    ]
  },
  "address_as_by_context": [
    {
      "context": "default",
      "value": "Cursor Support",
      "count": 3,
      "total": 5,
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-001-m1",
          "quote": "Hello Cursor Support,"
        },
        {
          "message_id": "syn-refund_complaint-012-m1",
          "quote": "Hello Cursor Support,"
        },
        {
          "message_id": "syn-refund_complaint-012-m3",
          "quote": "Hello Cursor Support,"
        }
      ]
    }
  ],
  "sign_off": {
    "value": "Thank you, Mia",
    "count": 4,
    "total": 5,
    "status": "learned",
    "evidence": [
      {
        "message_id": "syn-refund_complaint-001-m1",
        "quote": "Thank you,\nMia"
      },
      {
        "message_id": "syn-refund_complaint-012-m1",
        "quote": "Thank you,\nMia"
      },
      {
        "message_id": "syn-refund_complaint-012-m2",
        "quote": "Thank you,\nMia"
      },
      {
        "message_id": "syn-refund_complaint-012-m3",
        "quote": "Thank you,\nMia"
      }
    ]
  },
  "language": {
    "value": "en",
    "count": 5,
    "total": 5,
    "status": "learned",
    "evidence": [
      {
        "message_id": "syn-refund_complaint-001-m1",
        "quote": "Could you please make a one-time exception"
      },
      {
        "message_id": "syn-refund_complaint-001-m2",
        "quote": "Thank you for taking another look."
      },
      {
        "message_id": "syn-refund_complaint-012-m1",
        "quote": "Please refund the $40.00 Business charge"
      },
      {
        "message_id": "syn-refund_complaint-012-m2",
        "quote": "Could you please refund the remaining $20.00?"
      },
      {
        "message_id": "syn-refund_complaint-012-m3",
        "quote": "It has been six days"
      }
    ]
  },
  "facts": [
    {
      "id": "f1",
      "text": "This is Cursor's customer support address. Mia writes to it as a paying Cursor customer.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-001-m1",
          "quote": "Hello Cursor Support,"
        }
      ]
    },
    {
      "id": "f2",
      "text": "Support passes refund requests it cannot approve to a separate billing team, and Mia has asked for escalation there.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-001-m1",
          "quote": "escalate the request to the billing team"
        },
        {
          "message_id": "syn-refund_complaint-012-m3",
          "quote": "passing this to the billing team"
        }
      ]
    },
    {
      "id": "f3",
      "text": "In 2024, Mia's Cursor Pro subscription kept renewing every month from April 2024 after she stopped using it.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-001-m1",
          "quote": "renewed every month since April 2024"
        }
      ]
    },
    {
      "id": "f4",
      "text": "Her last activity on the account was April 3, 2024.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-001-m1",
          "quote": "from April 3, 2024"
        },
        {
          "message_id": "syn-refund_complaint-001-m2",
          "quote": "My last activity on the account was April 3, 2024"
        }
      ]
    },
    {
      "id": "f5",
      "text": "The unused renewals came to $100.00, which was five monthly charges of $20.00.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-001-m1",
          "quote": "The charges total $100.00"
        }
      ]
    },
    {
      "id": "f6",
      "text": "Mia asks for refunds to go back to her original payment method, not as account credits.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-001-m1",
          "quote": "to the original payment method"
        }
      ]
    },
    {
      "id": "f7",
      "text": "Support refunded only the most recent $20.00 of the 2024 charges.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-001-m2",
          "quote": "refunding the most recent $20.00 charge"
        }
      ]
    },
    {
      "id": "f8",
      "text": "Mia then asked for a review of the other four charges (May 3 to August 3, 2024), $80.00 in total.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-001-m2",
          "quote": "total $80.00"
        }
      ]
    },
    {
      "id": "f9",
      "text": "On September 2, 2025, Mia switched from a Business seat to an individual Pro plan.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-012-m1",
          "quote": "individual Pro plan on September 2, 2025"
        }
      ]
    },
    {
      "id": "f10",
      "text": "On September 3, 2025, she was charged for both plans: $40.00 for the Business seat and $20.00 for Pro.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-012-m1",
          "quote": "$40.00 for the Business seat"
        }
      ]
    },
    {
      "id": "f11",
      "text": "She removed the team workspace on the same day she switched plans, and asked support to confirm that no active seats remain.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-012-m1",
          "quote": "removed the team workspace the same day"
        }
      ]
    },
    {
      "id": "f12",
      "text": "Support refunded $20.00 of the $40.00 Business charge. Mia is still asking for the remaining $20.00.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-012-m2",
          "quote": "refunding $20.00 of the Business charge"
        }
      ]
    },
    {
      "id": "f13",
      "text": "Mia has the email confirming the Business seat was removed and offered it as proof.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-012-m2",
          "quote": "I have the removal confirmation email"
        }
      ]
    },
    {
      "id": "f14",
      "text": "As of September 18, 2025, the billing team had not replied for six days.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-012-m3",
          "quote": "It has been six days"
        }
      ]
    }
  ],
  "edges": [
    {
      "to": "Cursor billing team",
      "type": "escalates_to",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-012-m3",
          "quote": "passing this to the billing team"
        }
      ]
    }
  ],
  "core_connection": {
    "text": "Mia is a Cursor customer. All her emails to this support address are billing disputes asking for refunds, once in 2024 and again in 2025.",
    "evidence": [
      {
        "message_id": "syn-refund_complaint-001-m1",
        "quote": "Hello Cursor Support,"
      },
      {
        "message_id": "syn-refund_complaint-012-m1",
        "quote": "Please refund the $40.00 Business charge"
      }
    ]
  },
  "external": []
}
---

# Cursor Support

Mia is a Cursor customer. All her emails to this support address are billing disputes asking for refunds, once in 2024 and again in 2025.

- Address (default): Cursor Support (3/5 emails)
- This is Cursor's customer support address. Mia writes to it as a paying Cursor customer.
- Support passes refund requests it cannot approve to a separate billing team, and Mia has asked for escalation there.
- In 2024, Mia's Cursor Pro subscription kept renewing every month from April 2024 after she stopped using it.
- Her last activity on the account was April 3, 2024.
- The unused renewals came to $100.00, which was five monthly charges of $20.00.
- Mia asks for refunds to go back to her original payment method, not as account credits.
- Support refunded only the most recent $20.00 of the 2024 charges.
- Mia then asked for a review of the other four charges (May 3 to August 3, 2024), $80.00 in total.
- On September 2, 2025, Mia switched from a Business seat to an individual Pro plan.
- On September 3, 2025, she was charged for both plans: $40.00 for the Business seat and $20.00 for Pro.
- She removed the team workspace on the same day she switched plans, and asked support to confirm that no active seats remain.
- Support refunded $20.00 of the $40.00 Business charge. Mia is still asking for the remaining $20.00.
- Mia has the email confirming the Business seat was removed and offered it as proof.
- As of September 18, 2025, the billing team had not replied for six days.

_Extracted offline by pipeline/extract.py; every entry is backed by verified quotes._
