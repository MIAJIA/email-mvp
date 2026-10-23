---
{
  "email": "support@dropbox.example.com",
  "display_name": "Dropbox Support",
  "relationship": "customer support",
  "address_as": {
    "value": "Dropbox Support",
    "count": 2,
    "total": 5,
    "status": "learned",
    "evidence": [
      {
        "message_id": "syn-refund_complaint-011-m1",
        "quote": "Hello Dropbox Support,"
      },
      {
        "message_id": "syn-refund_complaint-022-m1",
        "quote": "Hello Dropbox Support,"
      }
    ]
  },
  "address_as_by_context": [
    {
      "context": "default",
      "value": "Dropbox Support",
      "count": 2,
      "total": 5,
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-011-m1",
          "quote": "Hello Dropbox Support,"
        },
        {
          "message_id": "syn-refund_complaint-022-m1",
          "quote": "Hello Dropbox Support,"
        }
      ]
    }
  ],
  "sign_off": {
    "value": "Thank you,\nMia",
    "count": 4,
    "total": 5,
    "status": "learned",
    "evidence": [
      {
        "message_id": "syn-refund_complaint-011-m1",
        "quote": "Thank you,"
      },
      {
        "message_id": "syn-refund_complaint-011-m2",
        "quote": "Thank you,"
      },
      {
        "message_id": "syn-refund_complaint-022-m1",
        "quote": "Thank you,"
      },
      {
        "message_id": "syn-refund_complaint-022-m2",
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
        "message_id": "syn-refund_complaint-011-m1",
        "quote": "Please confirm the cancellation"
      },
      {
        "message_id": "syn-refund_complaint-011-m2",
        "quote": "Thank you for cancelling the plan."
      },
      {
        "message_id": "syn-refund_complaint-011-m3",
        "quote": "Yes, please send it to that card."
      },
      {
        "message_id": "syn-refund_complaint-022-m1",
        "quote": "never invited any members"
      },
      {
        "message_id": "syn-refund_complaint-022-m2",
        "quote": "Thanks for refunding the $8.00 difference for July."
      }
    ]
  },
  "facts": [
    {
      "id": "f1",
      "text": "In August 2025 Mia asked to cancel Dropbox Plus, which had renewed on August 2, 2025 for $119.88, and to get a full refund.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-011-m1",
          "quote": "renewed on August 2, 2025 for $119.88"
        }
      ]
    },
    {
      "id": "f2",
      "text": "Mia said she had moved her files to another service in fall 2024. Her last upload was on October 21, 2024.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-011-m1",
          "quote": "files to another service last fall"
        },
        {
          "message_id": "syn-refund_complaint-011-m1",
          "quote": "October 21, 2024"
        }
      ]
    },
    {
      "id": "f3",
      "text": "Mia consistently wants refunds sent to her original payment method, not as account credits.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-011-m1",
          "quote": "rather than account credits"
        },
        {
          "message_id": "syn-refund_complaint-022-m2",
          "quote": "rather than account credits"
        }
      ]
    },
    {
      "id": "f4",
      "text": "Support first added the 2025 refund as an account credit. Mia asked them to reverse it, then confirmed the refund should go to her card.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-011-m2",
          "quote": "reverse the credit and refund the $119.88"
        },
        {
          "message_id": "syn-refund_complaint-011-m3",
          "quote": "Yes, please send it to that card."
        }
      ]
    },
    {
      "id": "f5",
      "text": "Mia asks for escalation if the first support level cannot approve a full refund.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-011-m1",
          "quote": "please escalate the request"
        },
        {
          "message_id": "syn-refund_complaint-022-m1",
          "quote": "please escalate the request"
        }
      ]
    },
    {
      "id": "f6",
      "text": "Mia upgraded to the Family plan on March 3, 2026 but never invited any members. She switched back to Plus in July 2026.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-022-m1",
          "quote": "Family plan on March 3, 2026"
        },
        {
          "message_id": "syn-refund_complaint-022-m1",
          "quote": "never invited any members"
        },
        {
          "message_id": "syn-refund_complaint-022-m1",
          "quote": "switched the account back to Plus today"
        }
      ]
    },
    {
      "id": "f7",
      "text": "Family cost $19.99 a month versus $11.99 for Plus. Mia asked for the $40.00 difference to be refunded.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-022-m1",
          "quote": "charged $19.99 each month"
        },
        {
          "message_id": "syn-refund_complaint-022-m1",
          "quote": "the extra cost is $40.00"
        }
      ]
    },
    {
      "id": "f8",
      "text": "Support refunded only $8.00 for July 2026. Mia is still asking for the remaining $32.00 for March through June 2026.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-022-m2",
          "quote": "Thanks for refunding the $8.00 difference for July."
        },
        {
          "message_id": "syn-refund_complaint-022-m2",
          "quote": "refund the remaining $32.00"
        }
      ]
    }
  ],
  "edges": [],
  "core_connection": {
    "text": "Dropbox's customer support team, which Mia contacts about cancelling plans and getting billing refunds for her Dropbox account.",
    "evidence": [
      {
        "message_id": "syn-refund_complaint-011-m1",
        "quote": "Please cancel my Dropbox Plus plan"
      },
      {
        "message_id": "syn-refund_complaint-022-m1",
        "quote": "Could you please refund the $40.00 difference"
      }
    ]
  },
  "external": []
}
---

# Dropbox Support

Dropbox's customer support team, which Mia contacts about cancelling plans and getting billing refunds for her Dropbox account.

- Address (default): Dropbox Support (2/5 emails)
- In August 2025 Mia asked to cancel Dropbox Plus, which had renewed on August 2, 2025 for $119.88, and to get a full refund.
- Mia said she had moved her files to another service in fall 2024. Her last upload was on October 21, 2024.
- Mia consistently wants refunds sent to her original payment method, not as account credits.
- Support first added the 2025 refund as an account credit. Mia asked them to reverse it, then confirmed the refund should go to her card.
- Mia asks for escalation if the first support level cannot approve a full refund.
- Mia upgraded to the Family plan on March 3, 2026 but never invited any members. She switched back to Plus in July 2026.
- Family cost $19.99 a month versus $11.99 for Plus. Mia asked for the $40.00 difference to be refunded.
- Support refunded only $8.00 for July 2026. Mia is still asking for the remaining $32.00 for March through June 2026.

_Extracted offline by pipeline/extract.py; every entry is backed by verified quotes._
