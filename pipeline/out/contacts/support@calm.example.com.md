---
{
  "email": "support@calm.example.com",
  "display_name": "Calm Support",
  "relationship": "customer support",
  "address_as": {
    "value": "Calm Support",
    "count": 2,
    "total": 4,
    "status": "learned",
    "evidence": [
      {
        "message_id": "syn-refund_complaint-009-m1",
        "quote": "Hello Calm Support,"
      },
      {
        "message_id": "syn-refund_complaint-020-m1",
        "quote": "Hello Calm Support,"
      }
    ]
  },
  "address_as_by_context": [
    {
      "context": "default",
      "value": "Calm Support",
      "count": 2,
      "total": 4,
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-009-m1",
          "quote": "Hello Calm Support,"
        },
        {
          "message_id": "syn-refund_complaint-020-m1",
          "quote": "Hello Calm Support,"
        }
      ]
    }
  ],
  "sign_off": {
    "value": "Thank you, Mia",
    "count": 4,
    "total": 4,
    "status": "learned",
    "evidence": [
      {
        "message_id": "syn-refund_complaint-009-m1",
        "quote": "Thank you,"
      },
      {
        "message_id": "syn-refund_complaint-009-m2",
        "quote": "Thank you,"
      },
      {
        "message_id": "syn-refund_complaint-020-m1",
        "quote": "Thank you,"
      },
      {
        "message_id": "syn-refund_complaint-020-m2",
        "quote": "Thank you,"
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
        "message_id": "syn-refund_complaint-009-m1",
        "quote": "Please confirm the cancellation"
      },
      {
        "message_id": "syn-refund_complaint-009-m2",
        "quote": "please escalate the request"
      },
      {
        "message_id": "syn-refund_complaint-020-m1",
        "quote": "Please confirm the plan change"
      },
      {
        "message_id": "syn-refund_complaint-020-m2",
        "quote": "Thank you for the option."
      }
    ]
  },
  "facts": [
    {
      "id": "f1",
      "text": "Mia's Calm Premium annual plan renewed on June 1, 2025, for $69.99, and she asked for it to be cancelled and refunded.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-009-m1",
          "quote": "The annual plan renewed at $69.99."
        }
      ]
    },
    {
      "id": "f2",
      "text": "Mia had not opened the app since August 2024 and said she got no reminder before the renewal.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-009-m1",
          "quote": "I have not opened the app since August 2024"
        }
      ]
    },
    {
      "id": "f3",
      "text": "Mia wants refunds sent to her original payment method, not as account credits.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-009-m1",
          "quote": "to the original payment method rather than account credits"
        }
      ]
    },
    {
      "id": "f4",
      "text": "Calm turned off auto-renewal but would not refund the 2025 charge, so Mia asked them to escalate her request.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-009-m2",
          "quote": "Thank you for turning off the auto-renewal."
        },
        {
          "message_id": "syn-refund_complaint-009-m2",
          "quote": "please escalate the request"
        }
      ]
    },
    {
      "id": "f5",
      "text": "On May 9, 2026, Mia restarted Calm Premium and chose the monthly plan at $14.99, but she was charged $69.99 for the annual plan.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-020-m1",
          "quote": "I selected the monthly plan at $14.99"
        },
        {
          "message_id": "syn-refund_complaint-020-m1",
          "quote": "I was charged $69.99 for the annual plan instead"
        }
      ]
    },
    {
      "id": "f6",
      "text": "Mia first asked Calm to switch her to the monthly plan and refund the $55.00 difference.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-020-m1",
          "quote": "refund the $55.00 difference"
        }
      ]
    },
    {
      "id": "f7",
      "text": "Mia then accepted Calm's offer to cancel the annual plan for a full $69.99 refund, and said she would sign up for the monthly plan again herself.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-020-m2",
          "quote": "Please cancel it and refund the full $69.99"
        },
        {
          "message_id": "syn-refund_complaint-020-m2",
          "quote": "I will sign up for the monthly plan again myself"
        }
      ]
    }
  ],
  "edges": [],
  "core_connection": {
    "text": "Calm is a subscription service Mia uses. She has written to its support team twice about billing: once about an unwanted annual renewal, and once about being charged for the wrong plan.",
    "evidence": [
      {
        "message_id": "syn-refund_complaint-009-m1",
        "quote": "I would like to cancel my Calm Premium subscription"
      },
      {
        "message_id": "syn-refund_complaint-020-m1",
        "quote": "I was charged $69.99 for the annual plan instead"
      }
    ]
  },
  "external": []
}
---

# Calm Support

Calm is a subscription service Mia uses. She has written to its support team twice about billing: once about an unwanted annual renewal, and once about being charged for the wrong plan.

- Address (default): Calm Support (2/4 emails)
- Mia's Calm Premium annual plan renewed on June 1, 2025, for $69.99, and she asked for it to be cancelled and refunded.
- Mia had not opened the app since August 2024 and said she got no reminder before the renewal.
- Mia wants refunds sent to her original payment method, not as account credits.
- Calm turned off auto-renewal but would not refund the 2025 charge, so Mia asked them to escalate her request.
- On May 9, 2026, Mia restarted Calm Premium and chose the monthly plan at $14.99, but she was charged $69.99 for the annual plan.
- Mia first asked Calm to switch her to the monthly plan and refund the $55.00 difference.
- Mia then accepted Calm's offer to cancel the annual plan for a full $69.99 refund, and said she would sign up for the monthly plan again herself.

_Extracted offline by pipeline/extract.py; every entry is backed by verified quotes._
