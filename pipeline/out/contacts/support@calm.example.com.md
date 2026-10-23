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
    "value": "Thank you,\nMia",
    "count": 4,
    "total": 4,
    "status": "learned",
    "evidence": [
      {
        "message_id": "syn-refund_complaint-009-m1",
        "quote": "Thank you,\nMia"
      },
      {
        "message_id": "syn-refund_complaint-009-m2",
        "quote": "Thank you,\nMia"
      },
      {
        "message_id": "syn-refund_complaint-020-m1",
        "quote": "Thank you,\nMia"
      },
      {
        "message_id": "syn-refund_complaint-020-m2",
        "quote": "Thank you,\nMia"
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
        "quote": "Hello Calm Support,"
      },
      {
        "message_id": "syn-refund_complaint-009-m2",
        "quote": "Thank you for turning off the auto-renewal."
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
      "text": "Calm Support is the customer support team for Calm, the meditation app where Mia has a Calm Premium subscription.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-009-m1",
          "quote": "cancel my Calm Premium subscription"
        }
      ]
    },
    {
      "id": "f2",
      "text": "Mia's Calm Premium annual plan renewed on June 1, 2025 for $69.99, and she asked for a refund.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-009-m1",
          "quote": "The annual plan renewed at $69.99."
        }
      ]
    },
    {
      "id": "f3",
      "text": "Mia had not opened the app since August 2024 and said she got no reminder before the renewal.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-009-m1",
          "quote": "I have not opened the app since August 2024"
        },
        {
          "message_id": "syn-refund_complaint-009-m1",
          "quote": "I did not receive a reminder"
        }
      ]
    },
    {
      "id": "f4",
      "text": "Mia contacted them two days after the June 2025 charge and wanted the refund sent to her original payment method, not as account credits.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-009-m1",
          "quote": "I'm contacting you two days after the charge."
        },
        {
          "message_id": "syn-refund_complaint-009-m1",
          "quote": "rather than account credits"
        }
      ]
    },
    {
      "id": "f5",
      "text": "Support turned off auto-renewal. Mia then asked them to review the charge again and escalate it if the first support level could not approve the refund.",
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
      "id": "f6",
      "text": "On May 9, 2026 Mia restarted Calm Premium and picked the $14.99 monthly plan, but was charged $69.99 for the annual plan.",
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
      "id": "f7",
      "text": "Mia first asked them to switch her to the monthly plan and refund the $55.00 difference.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-020-m1",
          "quote": "refund the $55.00 difference"
        }
      ]
    },
    {
      "id": "f8",
      "text": "Mia then asked them to cancel the annual plan and refund the full $69.99. She said she would sign up for the monthly plan again herself after the refund.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-020-m2",
          "quote": "refund the full $69.99"
        },
        {
          "message_id": "syn-refund_complaint-020-m2",
          "quote": "I will sign up for the monthly plan again myself"
        }
      ]
    },
    {
      "id": "f9",
      "text": "Mia's emails to them are polite but firm. She states the facts and asks them to confirm the cancellation and the exact refund amount.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-009-m1",
          "quote": "Please confirm the cancellation"
        },
        {
          "message_id": "syn-refund_complaint-020-m1",
          "quote": "Please confirm the plan change and the amount being refunded."
        }
      ]
    }
  ],
  "edges": [],
  "core_connection": {
    "text": "Calm Support is the customer support team for Mia's Calm Premium subscription. Mia has contacted them to cancel plans and get refunds for unwanted charges.",
    "evidence": [
      {
        "message_id": "syn-refund_complaint-009-m1",
        "quote": "I would like to cancel my Calm Premium subscription"
      },
      {
        "message_id": "syn-refund_complaint-020-m1",
        "quote": "refund the $55.00 difference"
      }
    ]
  },
  "external": []
}
---

# Calm Support

Calm Support is the customer support team for Mia's Calm Premium subscription. Mia has contacted them to cancel plans and get refunds for unwanted charges.

- Address (default): Calm Support (2/4 emails)
- Calm Support is the customer support team for Calm, the meditation app where Mia has a Calm Premium subscription.
- Mia's Calm Premium annual plan renewed on June 1, 2025 for $69.99, and she asked for a refund.
- Mia had not opened the app since August 2024 and said she got no reminder before the renewal.
- Mia contacted them two days after the June 2025 charge and wanted the refund sent to her original payment method, not as account credits.
- Support turned off auto-renewal. Mia then asked them to review the charge again and escalate it if the first support level could not approve the refund.
- On May 9, 2026 Mia restarted Calm Premium and picked the $14.99 monthly plan, but was charged $69.99 for the annual plan.
- Mia first asked them to switch her to the monthly plan and refund the $55.00 difference.
- Mia then asked them to cancel the annual plan and refund the full $69.99. She said she would sign up for the monthly plan again herself after the refund.
- Mia's emails to them are polite but firm. She states the facts and asks them to confirm the cancellation and the exact refund amount.

_Extracted offline by pipeline/extract.py; every entry is backed by verified quotes._
