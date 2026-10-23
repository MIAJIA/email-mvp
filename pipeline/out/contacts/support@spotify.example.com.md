---
{
  "email": "support@spotify.example.com",
  "display_name": "Spotify Support",
  "relationship": "customer support",
  "address_as": {
    "value": "Spotify Support",
    "count": 2,
    "total": 4,
    "status": "learned",
    "evidence": [
      {
        "message_id": "syn-refund_complaint-007-m1",
        "quote": "Hello Spotify Support,"
      },
      {
        "message_id": "syn-refund_complaint-018-m1",
        "quote": "Hello Spotify Support,"
      }
    ]
  },
  "address_as_by_context": [
    {
      "context": "default",
      "value": "Spotify Support",
      "count": 2,
      "total": 4,
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-007-m1",
          "quote": "Hello Spotify Support,"
        },
        {
          "message_id": "syn-refund_complaint-018-m1",
          "quote": "Hello Spotify Support,"
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
        "message_id": "syn-refund_complaint-007-m1",
        "quote": "Thank you,"
      },
      {
        "message_id": "syn-refund_complaint-007-m2",
        "quote": "Thank you,"
      },
      {
        "message_id": "syn-refund_complaint-018-m1",
        "quote": "Thank you,"
      },
      {
        "message_id": "syn-refund_complaint-018-m2",
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
        "message_id": "syn-refund_complaint-007-m1",
        "quote": "I was charged $16.99 for Premium Family"
      },
      {
        "message_id": "syn-refund_complaint-007-m2",
        "quote": "Thanks for checking."
      },
      {
        "message_id": "syn-refund_complaint-018-m1",
        "quote": "I cancelled my Premium Individual plan"
      },
      {
        "message_id": "syn-refund_complaint-018-m2",
        "quote": "Thanks for looking into this."
      }
    ]
  },
  "facts": [
    {
      "id": "f1",
      "text": "Spotify Support is the customer support service for Mia's Spotify Premium subscription. She writes to it about billing disputes.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-007-m1",
          "quote": "Hello Spotify Support,"
        }
      ]
    },
    {
      "id": "f2",
      "text": "Mia changed her plan from Premium Family to Premium Individual on March 30, 2025, and received a confirmation email the same day.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-007-m1",
          "quote": "I changed my plan to Premium Individual on March 30, 2025"
        },
        {
          "message_id": "syn-refund_complaint-007-m1",
          "quote": "I received a confirmation email for it the same day"
        }
      ]
    },
    {
      "id": "f3",
      "text": "On April 8, 2025, Mia was charged $16.99 for the Family plan instead of $11.99 for Individual, and she asked for the $5.00 difference back.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-007-m1",
          "quote": "I was charged $16.99 for Premium Family on April 8, 2025"
        },
        {
          "message_id": "syn-refund_complaint-007-m1",
          "quote": "I should have been charged $11.99 for Premium Individual"
        }
      ]
    },
    {
      "id": "f4",
      "text": "Mia argued that the confirmation email said the new plan would start at the next billing date, which was April 8.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-007-m2",
          "quote": "which was April 8"
        }
      ]
    },
    {
      "id": "f5",
      "text": "Mia cancelled Premium Individual on February 20, 2026, and her account showed that Premium would end on March 7, 2026.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-018-m1",
          "quote": "I cancelled my Premium Individual plan on February 20, 2026"
        },
        {
          "message_id": "syn-refund_complaint-018-m1",
          "quote": "Premium would end on March 7, 2026"
        }
      ]
    },
    {
      "id": "f6",
      "text": "On March 8, 2026, Mia was still charged $11.99, and Premium showed as active again. She asked Spotify to cancel the subscription, refund the charge and confirm there would be no further charges.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-018-m1",
          "quote": "On March 8, 2026 I was still charged $11.99"
        },
        {
          "message_id": "syn-refund_complaint-018-m1",
          "quote": "confirm that no further charges will be made"
        }
      ]
    },
    {
      "id": "f7",
      "text": "Mia says she did not restart Premium herself and has not played anything on the account since March 7, 2026. She asked Spotify to check which device restarted the subscription.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-018-m2",
          "quote": "I did not restart Premium on March 8, 2026"
        },
        {
          "message_id": "syn-refund_complaint-018-m2",
          "quote": "check which device restarted the subscription"
        }
      ]
    },
    {
      "id": "f8",
      "text": "When the first reply turns her down, Mia asks for the refund as a one-time exception and asks for the request to be escalated to the billing team.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-007-m2",
          "quote": "escalate the request to the billing team"
        },
        {
          "message_id": "syn-refund_complaint-018-m2",
          "quote": "as a one-time exception"
        }
      ]
    },
    {
      "id": "f9",
      "text": "Mia's emails to support are short, polite and specific: she gives exact dates and amounts and states clearly what she wants done.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-007-m1",
          "quote": "Since the plan change was made before the renewal date"
        }
      ]
    }
  ],
  "edges": [
    {
      "to": "billing team",
      "type": "escalation_target",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-007-m2",
          "quote": "please escalate the request to the billing team"
        }
      ]
    }
  ],
  "core_connection": {
    "text": "Mia contacts Spotify's support team about billing problems with her Spotify Premium subscription and asks for refunds of charges she says were wrong.",
    "evidence": [
      {
        "message_id": "syn-refund_complaint-007-m1",
        "quote": "Could you please refund the $5.00 difference"
      },
      {
        "message_id": "syn-refund_complaint-018-m1",
        "quote": "refund the March 8 charge"
      }
    ]
  },
  "external": []
}
---

# Spotify Support

Mia contacts Spotify's support team about billing problems with her Spotify Premium subscription and asks for refunds of charges she says were wrong.

- Address (default): Spotify Support (2/4 emails)
- Spotify Support is the customer support service for Mia's Spotify Premium subscription. She writes to it about billing disputes.
- Mia changed her plan from Premium Family to Premium Individual on March 30, 2025, and received a confirmation email the same day.
- On April 8, 2025, Mia was charged $16.99 for the Family plan instead of $11.99 for Individual, and she asked for the $5.00 difference back.
- Mia argued that the confirmation email said the new plan would start at the next billing date, which was April 8.
- Mia cancelled Premium Individual on February 20, 2026, and her account showed that Premium would end on March 7, 2026.
- On March 8, 2026, Mia was still charged $11.99, and Premium showed as active again. She asked Spotify to cancel the subscription, refund the charge and confirm there would be no further charges.
- Mia says she did not restart Premium herself and has not played anything on the account since March 7, 2026. She asked Spotify to check which device restarted the subscription.
- When the first reply turns her down, Mia asks for the refund as a one-time exception and asks for the request to be escalated to the billing team.
- Mia's emails to support are short, polite and specific: she gives exact dates and amounts and states clearly what she wants done.

_Extracted offline by pipeline/extract.py; every entry is backed by verified quotes._
