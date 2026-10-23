---
{
  "email": "hi@cursor.example.com",
  "display_name": "Cursor Support",
  "relationship": "vendor support",
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
        "quote": "Thank you,"
      },
      {
        "message_id": "syn-refund_complaint-012-m1",
        "quote": "Thank you,"
      },
      {
        "message_id": "syn-refund_complaint-012-m2",
        "quote": "Thank you,"
      },
      {
        "message_id": "syn-refund_complaint-012-m3",
        "quote": "Thank you,"
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
        "quote": "Thank you,"
      },
      {
        "message_id": "syn-refund_complaint-012-m2",
        "quote": "Could you please refund the remaining $20.00?"
      },
      {
        "message_id": "syn-refund_complaint-012-m3",
        "quote": "Thank you for passing this to the billing team."
      }
    ]
  },
  "facts": [
    {
      "id": "f1",
      "text": "In 2024, Mia's Cursor Pro plan renewed every month without use. Her last session was on April 3, 2024, and the unused renewals cost $100 (5 × $20, from May 3 to Sep 3, 2024).",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-001-m1",
          "quote": "from April 3, 2024"
        },
        {
          "message_id": "syn-refund_complaint-001-m1",
          "quote": "The charges total $100.00"
        }
      ]
    },
    {
      "id": "f2",
      "text": "Mia wants refunds to go to her original payment method, not to account credits.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-001-m1",
          "quote": "rather than account credits"
        }
      ]
    },
    {
      "id": "f3",
      "text": "Support refunded only the most recent $20. Mia asked for the remaining $80 (May 3 to Aug 3, 2024) to be escalated to billing or a supervisor.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-001-m2",
          "quote": "Thanks for refunding the most recent $20.00 charge."
        },
        {
          "message_id": "syn-refund_complaint-001-m2",
          "quote": "escalate this to the billing team"
        }
      ]
    },
    {
      "id": "f4",
      "text": "On September 2, 2025, Mia switched from a Business seat to an individual Pro plan. On September 3 she was charged for both: $40 for Business and $20 for Pro.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-012-m1",
          "quote": "on September 2, 2025"
        },
        {
          "message_id": "syn-refund_complaint-012-m1",
          "quote": "$40.00 for the Business seat"
        }
      ]
    },
    {
      "id": "f5",
      "text": "Support refunded $20 of the $40 Business charge. Mia is asking for the remaining $20 because the seat was removed the day before the charge, and she has the removal confirmation email.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-012-m2",
          "quote": "Thanks for refunding $20.00 of the Business charge."
        },
        {
          "message_id": "syn-refund_complaint-012-m2",
          "quote": "I have the removal confirmation email"
        }
      ]
    },
    {
      "id": "f6",
      "text": "As of September 18, 2025, the billing team had not replied six days after the escalation. $20 is still open, and Mia wants confirmation that the team workspace has no active seats.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-012-m3",
          "quote": "It has been six days and I have not heard back yet."
        },
        {
          "message_id": "syn-refund_complaint-012-m3",
          "quote": "no active seats left on the team workspace"
        }
      ]
    },
    {
      "id": "f7",
      "text": "Mia's style with support: she states exact dates and amounts, asks for a one-time exception, and asks them to escalate if first-level support can't approve it.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-001-m1",
          "quote": "please escalate the request to the billing team"
        },
        {
          "message_id": "syn-refund_complaint-001-m2",
          "quote": "as a one-time exception"
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
          "quote": "Thank you for passing this to the billing team."
        }
      ]
    }
  ],
  "core_connection": {
    "text": "Mia, as a paying user, contacts Cursor's support desk about refunds and billing errors on her Cursor subscriptions.",
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

Mia, as a paying user, contacts Cursor's support desk about refunds and billing errors on her Cursor subscriptions.

- Address (default): Cursor Support (3/5 emails)
- In 2024, Mia's Cursor Pro plan renewed every month without use. Her last session was on April 3, 2024, and the unused renewals cost $100 (5 × $20, from May 3 to Sep 3, 2024).
- Mia wants refunds to go to her original payment method, not to account credits.
- Support refunded only the most recent $20. Mia asked for the remaining $80 (May 3 to Aug 3, 2024) to be escalated to billing or a supervisor.
- On September 2, 2025, Mia switched from a Business seat to an individual Pro plan. On September 3 she was charged for both: $40 for Business and $20 for Pro.
- Support refunded $20 of the $40 Business charge. Mia is asking for the remaining $20 because the seat was removed the day before the charge, and she has the removal confirmation email.
- As of September 18, 2025, the billing team had not replied six days after the escalation. $20 is still open, and Mia wants confirmation that the team workspace has no active seats.
- Mia's style with support: she states exact dates and amounts, asks for a one-time exception, and asks them to escalate if first-level support can't approve it.

_Extracted offline by pipeline/extract.py; every entry is backed by verified quotes._
