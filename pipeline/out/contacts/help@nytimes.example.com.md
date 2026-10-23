---
{
  "email": "help@nytimes.example.com",
  "display_name": "NYTimes Customer Care",
  "relationship": "customer support",
  "address_as": {
    "value": "NYTimes Customer Care",
    "count": 2,
    "total": 4,
    "status": "learned",
    "evidence": [
      {
        "message_id": "syn-refund_complaint-008-m1",
        "quote": "Hello NYTimes Customer Care,"
      },
      {
        "message_id": "syn-refund_complaint-019-m1",
        "quote": "Hello NYTimes Customer Care,"
      }
    ]
  },
  "address_as_by_context": [
    {
      "context": "default",
      "value": "NYTimes Customer Care",
      "count": 2,
      "total": 4,
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-008-m1",
          "quote": "Hello NYTimes Customer Care,"
        },
        {
          "message_id": "syn-refund_complaint-019-m1",
          "quote": "Hello NYTimes Customer Care,"
        }
      ]
    }
  ],
  "sign_off": {
    "value": "Thank you, Mia",
    "count": 3,
    "total": 4,
    "status": "learned",
    "evidence": [
      {
        "message_id": "syn-refund_complaint-008-m1",
        "quote": "Thank you,\nMia"
      },
      {
        "message_id": "syn-refund_complaint-019-m1",
        "quote": "Thank you,\nMia"
      },
      {
        "message_id": "syn-refund_complaint-019-m2",
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
        "message_id": "syn-refund_complaint-008-m1",
        "quote": "Could you please refund the May 3 charge"
      },
      {
        "message_id": "syn-refund_complaint-008-m2",
        "quote": "done"
      },
      {
        "message_id": "syn-refund_complaint-019-m1",
        "quote": "I would appreciate a one-time exception"
      },
      {
        "message_id": "syn-refund_complaint-019-m2",
        "quote": "I'm asking for a review of the remaining three payments"
      }
    ]
  },
  "facts": [
    {
      "id": "f1",
      "text": "This is the New York Times customer care desk. Mia contacts them about her All Access subscription.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-008-m1",
          "quote": "Hello NYTimes Customer Care,"
        }
      ]
    },
    {
      "id": "f2",
      "text": "In May 2025 Mia's introductory rate ended and she was charged $25.00 on May 3, 2025. She asked them to cancel and refund that charge as a one-time exception.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-008-m1",
          "quote": "I was charged $25.00 on May 3, 2025"
        },
        {
          "message_id": "syn-refund_complaint-008-m1",
          "quote": "refund the May 3 charge of $25.00 as a one-time exception"
        }
      ]
    },
    {
      "id": "f3",
      "text": "In 2025, Mia said she had not used articles, Games or Cooking since early April.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-008-m1",
          "quote": "I have not read any articles or used the Games or Cooking apps"
        }
      ]
    },
    {
      "id": "f4",
      "text": "Mia finished the May 2025 cancellation herself by following their link, and replied with one word.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-008-m2",
          "quote": "done"
        }
      ]
    },
    {
      "id": "f5",
      "text": "Mia subscribed again in November 2025 at the $1 per week introductory rate. In January 2026 the rate changed to $25.00 every four weeks without her noticing.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-019-m1",
          "quote": "I subscribed at the $1 per week introductory rate in November 2025"
        }
      ]
    },
    {
      "id": "f6",
      "text": "Mia was charged $25.00 on January 10, February 7, March 7 and April 4, 2026, $100.00 in total. She has not logged in since December 2025.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-019-m1",
          "quote": "for a total of $100.00"
        },
        {
          "message_id": "syn-refund_complaint-019-m1",
          "quote": "I have not logged in since December 2025."
        }
      ]
    },
    {
      "id": "f7",
      "text": "Mia wants refunds to go to the original payment method, not account credits. If first-level support cannot approve a refund, she asks them to escalate it.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-019-m1",
          "quote": "to the original payment method rather than account credits"
        },
        {
          "message_id": "syn-refund_complaint-019-m1",
          "quote": "please escalate the request"
        }
      ]
    },
    {
      "id": "f8",
      "text": "In April 2026 they cancelled the subscription and refunded the April 4 payment.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-019-m2",
          "quote": "Thanks for cancelling the subscription and refunding the April 4 payment."
        }
      ]
    },
    {
      "id": "f9",
      "text": "Still open (April 2026): Mia asked for a review of the remaining $75.00 (January 10 to March 7, 2026). She asked for a copy of the December rate-change notice, which she cannot find, or a refund.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-019-m2",
          "quote": "which total $75.00"
        },
        {
          "message_id": "syn-refund_complaint-019-m2",
          "quote": "Could you please send me a copy of that notice, or refund the remaining $75.00?"
        }
      ]
    }
  ],
  "edges": [],
  "core_connection": {
    "text": "Mia writes to New York Times Customer Care to cancel her All Access subscription and to ask for refunds after introductory rates ended and she was charged the full price.",
    "evidence": [
      {
        "message_id": "syn-refund_complaint-008-m1",
        "quote": "Please cancel my All Access subscription"
      },
      {
        "message_id": "syn-refund_complaint-019-m1",
        "quote": "Please cancel my subscription, effective immediately."
      }
    ]
  },
  "external": []
}
---

# NYTimes Customer Care

Mia writes to New York Times Customer Care to cancel her All Access subscription and to ask for refunds after introductory rates ended and she was charged the full price.

- Address (default): NYTimes Customer Care (2/4 emails)
- This is the New York Times customer care desk. Mia contacts them about her All Access subscription.
- In May 2025 Mia's introductory rate ended and she was charged $25.00 on May 3, 2025. She asked them to cancel and refund that charge as a one-time exception.
- In 2025, Mia said she had not used articles, Games or Cooking since early April.
- Mia finished the May 2025 cancellation herself by following their link, and replied with one word.
- Mia subscribed again in November 2025 at the $1 per week introductory rate. In January 2026 the rate changed to $25.00 every four weeks without her noticing.
- Mia was charged $25.00 on January 10, February 7, March 7 and April 4, 2026, $100.00 in total. She has not logged in since December 2025.
- Mia wants refunds to go to the original payment method, not account credits. If first-level support cannot approve a refund, she asks them to escalate it.
- In April 2026 they cancelled the subscription and refunded the April 4 payment.
- Still open (April 2026): Mia asked for a review of the remaining $75.00 (January 10 to March 7, 2026). She asked for a copy of the December rate-change notice, which she cannot find, or a refund.

_Extracted offline by pipeline/extract.py; every entry is backed by verified quotes._
