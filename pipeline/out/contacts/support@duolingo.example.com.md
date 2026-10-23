---
{
  "email": "support@duolingo.example.com",
  "display_name": "Duolingo Support",
  "relationship": "customer support",
  "address_as": {
    "value": "Duolingo Support",
    "count": 2,
    "total": 4,
    "status": "learned",
    "evidence": [
      {
        "message_id": "syn-refund_complaint-010-m1",
        "quote": "Hello Duolingo Support,"
      },
      {
        "message_id": "syn-refund_complaint-021-m1",
        "quote": "Hello Duolingo Support,"
      }
    ]
  },
  "address_as_by_context": [
    {
      "context": "default",
      "value": "Duolingo Support",
      "count": 2,
      "total": 4,
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-010-m1",
          "quote": "Hello Duolingo Support,"
        },
        {
          "message_id": "syn-refund_complaint-021-m1",
          "quote": "Hello Duolingo Support,"
        }
      ]
    }
  ],
  "sign_off": {
    "value": "Thank you,\nMia",
    "count": 3,
    "total": 4,
    "status": "learned",
    "evidence": [
      {
        "message_id": "syn-refund_complaint-010-m1",
        "quote": "Thank you,"
      },
      {
        "message_id": "syn-refund_complaint-010-m2",
        "quote": "Thank you,"
      },
      {
        "message_id": "syn-refund_complaint-021-m1",
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
        "message_id": "syn-refund_complaint-010-m1",
        "quote": "Please refund the duplicate $12.99 charge"
      },
      {
        "message_id": "syn-refund_complaint-010-m2",
        "quote": "Thanks for checking."
      },
      {
        "message_id": "syn-refund_complaint-021-m1",
        "quote": "Please confirm the cancellation"
      },
      {
        "message_id": "syn-refund_complaint-021-m2",
        "quote": "Yes, that is the correct order."
      }
    ]
  },
  "facts": [
    {
      "id": "f1",
      "text": "On July 12, 2025 Mia was charged $12.99 twice for Super Duolingo, under two separate order numbers.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-010-m1",
          "quote": "two charges of $12.99 on July 12, 2025"
        }
      ]
    },
    {
      "id": "f2",
      "text": "Mia has one account and one subscription.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-010-m1",
          "quote": "I have one account and one subscription."
        }
      ]
    },
    {
      "id": "f3",
      "text": "Support said the second charge might be a pending authorization. Mia replied that both charges had posted and had been on her statement for six days.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-010-m2",
          "quote": "are posted, not pending"
        },
        {
          "message_id": "syn-refund_complaint-010-m2",
          "quote": "on my statement for six days"
        }
      ]
    },
    {
      "id": "f4",
      "text": "Her annual Super Duolingo plan renewed on June 7, 2026 for $84.99. Mia asked to cancel it and get a full refund.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-021-m1",
          "quote": "The renewal was $84.99."
        },
        {
          "message_id": "syn-refund_complaint-021-m1",
          "quote": "charged on June 7, 2026"
        }
      ]
    },
    {
      "id": "f5",
      "text": "Mia's last lesson was on September 14, 2025. She did not get a reminder before the plan renewed.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-021-m1",
          "quote": "My last lesson was on September 14, 2025"
        },
        {
          "message_id": "syn-refund_complaint-021-m1",
          "quote": "I did not receive a reminder"
        }
      ]
    },
    {
      "id": "f6",
      "text": "Mia wants refunds sent to the original payment method, not given as account credits.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-021-m1",
          "quote": "to the original payment method rather than account credits"
        }
      ]
    },
    {
      "id": "f7",
      "text": "Mia confirmed which order number should be refunded for the 2026 renewal.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-021-m2",
          "quote": "Yes, that is the correct order."
        }
      ]
    }
  ],
  "edges": [],
  "core_connection": {
    "text": "Mia is a Super Duolingo subscriber who has written to Duolingo Support twice about billing: a duplicate monthly charge in 2025 and an unwanted annual renewal in 2026.",
    "evidence": [
      {
        "message_id": "syn-refund_complaint-010-m1",
        "quote": "I was charged twice for Super Duolingo this month."
      },
      {
        "message_id": "syn-refund_complaint-021-m1",
        "quote": "Please cancel my Super Duolingo subscription"
      }
    ]
  },
  "external": []
}
---

# Duolingo Support

Mia is a Super Duolingo subscriber who has written to Duolingo Support twice about billing: a duplicate monthly charge in 2025 and an unwanted annual renewal in 2026.

- Address (default): Duolingo Support (2/4 emails)
- On July 12, 2025 Mia was charged $12.99 twice for Super Duolingo, under two separate order numbers.
- Mia has one account and one subscription.
- Support said the second charge might be a pending authorization. Mia replied that both charges had posted and had been on her statement for six days.
- Her annual Super Duolingo plan renewed on June 7, 2026 for $84.99. Mia asked to cancel it and get a full refund.
- Mia's last lesson was on September 14, 2025. She did not get a reminder before the plan renewed.
- Mia wants refunds sent to the original payment method, not given as account credits.
- Mia confirmed which order number should be refunded for the 2026 renewal.

_Extracted offline by pipeline/extract.py; every entry is backed by verified quotes._
