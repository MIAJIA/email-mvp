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
        "quote": "Hello Spotify Support,"
      },
      {
        "message_id": "syn-refund_complaint-007-m2",
        "quote": "Thanks for checking."
      },
      {
        "message_id": "syn-refund_complaint-018-m1",
        "quote": "Hello Spotify Support,"
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
      "text": "On March 30, 2025, Mia changed her plan from Premium Family to Premium Individual.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-007-m1",
          "quote": "I changed my plan to Premium Individual on March 30, 2025"
        }
      ]
    },
    {
      "id": "f2",
      "text": "On April 8, 2025, Mia was still charged the Family price of $16.99.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-007-m1",
          "quote": "I was charged $16.99 for Premium Family on April 8, 2025"
        }
      ]
    },
    {
      "id": "f3",
      "text": "Mia asked for the $5.00 difference to be refunded as a one-time exception. She argued the April 8 charge should have been at the Individual price.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-007-m2",
          "quote": "The April 8 charge should therefore have been at the Individual price."
        },
        {
          "message_id": "syn-refund_complaint-007-m2",
          "quote": "as a one-time exception"
        }
      ]
    },
    {
      "id": "f4",
      "text": "Mia cancelled her Premium Individual plan on February 20, 2026. Her account page showed Premium would end on March 7, 2026.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-018-m1",
          "quote": "I cancelled my Premium Individual plan on February 20, 2026"
        }
      ]
    },
    {
      "id": "f5",
      "text": "Mia was still charged $11.99 on March 8, 2026, and Premium showed as active again on her account.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-018-m1",
          "quote": "On March 8, 2026 I was still charged $11.99"
        }
      ]
    },
    {
      "id": "f6",
      "text": "Mia says she did not restart Premium herself and has not played anything on the account since March 7, 2026. She asked which device restarted it.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-018-m2",
          "quote": "I did not restart Premium on March 8, 2026"
        },
        {
          "message_id": "syn-refund_complaint-018-m2",
          "quote": "I have not played anything on the account since March 7"
        },
        {
          "message_id": "syn-refund_complaint-018-m2",
          "quote": "check which device restarted the subscription"
        }
      ]
    },
    {
      "id": "f7",
      "text": "When first-level support turns down a request, Mia asks for it to be escalated to the billing team.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-007-m2",
          "quote": "please escalate the request to the billing team"
        },
        {
          "message_id": "syn-refund_complaint-018-m2",
          "quote": "please escalate the request to the billing team"
        }
      ]
    }
  ],
  "edges": [],
  "core_connection": {
    "text": "Mia is a Spotify Premium subscriber who writes to Spotify Support to dispute billing charges and ask for refunds.",
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

Mia is a Spotify Premium subscriber who writes to Spotify Support to dispute billing charges and ask for refunds.

- Address (default): Spotify Support (2/4 emails)
- On March 30, 2025, Mia changed her plan from Premium Family to Premium Individual.
- On April 8, 2025, Mia was still charged the Family price of $16.99.
- Mia asked for the $5.00 difference to be refunded as a one-time exception. She argued the April 8 charge should have been at the Individual price.
- Mia cancelled her Premium Individual plan on February 20, 2026. Her account page showed Premium would end on March 7, 2026.
- Mia was still charged $11.99 on March 8, 2026, and Premium showed as active again on her account.
- Mia says she did not restart Premium herself and has not played anything on the account since March 7, 2026. She asked which device restarted it.
- When first-level support turns down a request, Mia asks for it to be escalated to the billing team.

_Extracted offline by pipeline/extract.py; every entry is backed by verified quotes._
