---
{
  "email": "billing@vercel.example.com",
  "display_name": "Vercel Billing",
  "relationship": "vendor billing",
  "address_as": {
    "value": "Vercel Billing Team",
    "count": 2,
    "total": 4,
    "status": "learned",
    "evidence": [
      {
        "message_id": "syn-refund_complaint-002-m1",
        "quote": "Hello Vercel Billing Team,"
      },
      {
        "message_id": "syn-refund_complaint-013-m1",
        "quote": "Hello Vercel Billing Team,"
      }
    ]
  },
  "address_as_by_context": [
    {
      "context": "default",
      "value": "Vercel Billing Team",
      "count": 2,
      "total": 4,
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-002-m1",
          "quote": "Hello Vercel Billing Team,"
        },
        {
          "message_id": "syn-refund_complaint-013-m1",
          "quote": "Hello Vercel Billing Team,"
        }
      ]
    }
  ],
  "sign_off": {
    "value": "Thank you,\nMia",
    "count": 2,
    "total": 4,
    "status": "learned",
    "evidence": [
      {
        "message_id": "syn-refund_complaint-002-m1",
        "quote": "Thank you,"
      },
      {
        "message_id": "syn-refund_complaint-013-m1",
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
        "message_id": "syn-refund_complaint-002-m1",
        "quote": "I was charged twice for the same Pro plan"
      },
      {
        "message_id": "syn-refund_complaint-002-m2",
        "quote": "Yes, please refund it to the card on file."
      },
      {
        "message_id": "syn-refund_complaint-013-m1",
        "quote": "I downgraded my team to the Hobby plan"
      },
      {
        "message_id": "syn-refund_complaint-013-m2",
        "quote": "Yes, the original payment method is fine."
      }
    ]
  },
  "facts": [
    {
      "id": "f1",
      "text": "In October 2024 Mia was charged twice ($20.00 each, posted October 7, 2024) for the same Pro plan period, October 7 to November 6, 2024.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-002-m1",
          "quote": "I was charged twice for the same Pro plan billing period"
        },
        {
          "message_id": "syn-refund_complaint-002-m1",
          "quote": "both cover October 7 to November 6, 2024"
        }
      ]
    },
    {
      "id": "f2",
      "text": "Mia's Vercel account had only one team and one seat.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-002-m1",
          "quote": "My account has only one team and one seat"
        }
      ]
    },
    {
      "id": "f3",
      "text": "Mia asked for the duplicate 2024 charge to go back to the card on file.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-002-m2",
          "quote": "Yes, please refund it to the card on file."
        }
      ]
    },
    {
      "id": "f4",
      "text": "Mia downgraded her team to the Hobby plan on September 20, 2025.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-013-m1",
          "quote": "I downgraded my team to the Hobby plan on September 20, 2025"
        }
      ]
    },
    {
      "id": "f5",
      "text": "On October 13, 2025 Mia was still charged $20.00 for the Web Analytics Plus and Speed Insights add-ons after the downgrade. She has not deployed any project since the downgrade.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-013-m1",
          "quote": "Web Analytics Plus and Speed Insights"
        },
        {
          "message_id": "syn-refund_complaint-013-m1",
          "quote": "I have not deployed any project since the downgrade"
        }
      ]
    },
    {
      "id": "f6",
      "text": "Mia asked for both add-ons to be removed and for the October 2025 charge to be refunded as a one-time exception, back to the original payment method.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-013-m1",
          "quote": "Please remove both add-ons"
        },
        {
          "message_id": "syn-refund_complaint-013-m2",
          "quote": "Yes, the original payment method is fine."
        }
      ]
    },
    {
      "id": "f7",
      "text": "Mia's complaint emails always end by asking for written confirmation of the refund amount and that no further or duplicate charges will be made.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-002-m1",
          "quote": "Please confirm the amount being refunded"
        },
        {
          "message_id": "syn-refund_complaint-013-m1",
          "quote": "that no further charges will be made"
        }
      ]
    },
    {
      "id": "f8",
      "text": "When billing asks a confirmation question, Mia replies in one short sentence with no greeting or sign-off.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-002-m2",
          "quote": "Yes, please refund it to the card on file."
        },
        {
          "message_id": "syn-refund_complaint-013-m2",
          "quote": "Yes, the original payment method is fine."
        }
      ]
    }
  ],
  "edges": [],
  "core_connection": {
    "text": "Vercel's billing support team. Mia writes to them to dispute charges on her Vercel account and ask for refunds.",
    "evidence": [
      {
        "message_id": "syn-refund_complaint-002-m1",
        "quote": "Please refund the duplicate $20.00 charge"
      },
      {
        "message_id": "syn-refund_complaint-013-m1",
        "quote": "refund the October 13 charge as a one-time exception"
      }
    ]
  },
  "external": []
}
---

# Vercel Billing

Vercel's billing support team. Mia writes to them to dispute charges on her Vercel account and ask for refunds.

- Address (default): Vercel Billing Team (2/4 emails)
- In October 2024 Mia was charged twice ($20.00 each, posted October 7, 2024) for the same Pro plan period, October 7 to November 6, 2024.
- Mia's Vercel account had only one team and one seat.
- Mia asked for the duplicate 2024 charge to go back to the card on file.
- Mia downgraded her team to the Hobby plan on September 20, 2025.
- On October 13, 2025 Mia was still charged $20.00 for the Web Analytics Plus and Speed Insights add-ons after the downgrade. She has not deployed any project since the downgrade.
- Mia asked for both add-ons to be removed and for the October 2025 charge to be refunded as a one-time exception, back to the original payment method.
- Mia's complaint emails always end by asking for written confirmation of the refund amount and that no further or duplicate charges will be made.
- When billing asks a confirmation question, Mia replies in one short sentence with no greeting or sign-off.

_Extracted offline by pipeline/extract.py; every entry is backed by verified quotes._
