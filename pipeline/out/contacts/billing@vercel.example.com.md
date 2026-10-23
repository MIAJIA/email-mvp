---
{
  "email": "billing@vercel.example.com",
  "display_name": "Vercel Billing Team",
  "relationship": "billing support",
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
    "value": "Thank you, Mia",
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
        "quote": "I was charged twice for the same Pro plan billing period."
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
      "text": "This is Vercel's billing support team; Mia writes to them about charges on her Vercel account.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-002-m1",
          "quote": "Hello Vercel Billing Team,"
        }
      ]
    },
    {
      "id": "f2",
      "text": "In October 2024 Mia was charged twice ($20.00 each) for the same Pro plan period (October 7 to November 6, 2024).",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-002-m1",
          "quote": "Both charges are $20.00"
        },
        {
          "message_id": "syn-refund_complaint-002-m1",
          "quote": "both cover October 7 to November 6, 2024"
        }
      ]
    },
    {
      "id": "f3",
      "text": "Mia's Vercel account had only one team and one seat at that time.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-002-m1",
          "quote": "My account has only one team and one seat"
        }
      ]
    },
    {
      "id": "f4",
      "text": "Mia asked them to check that the subscription was not set up twice, and to confirm she would only be billed once from then on.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-002-m1",
          "quote": "check that the subscription is not set up twice"
        },
        {
          "message_id": "syn-refund_complaint-002-m1",
          "quote": "I will only be billed once going forward"
        }
      ]
    },
    {
      "id": "f5",
      "text": "In October 2024 Mia agreed to have the duplicate charge refunded to her card on file.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-002-m2",
          "quote": "please refund it to the card on file"
        }
      ]
    },
    {
      "id": "f6",
      "text": "Mia downgraded her team to the Hobby plan on September 20, 2025.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-013-m1",
          "quote": "Hobby plan on September 20, 2025"
        }
      ]
    },
    {
      "id": "f7",
      "text": "On October 13, 2025 Mia was still charged $20.00 for the Web Analytics Plus and Speed Insights add-ons after the downgrade. She had not known the add-ons would stay active.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-013-m1",
          "quote": "Web Analytics Plus and Speed Insights"
        },
        {
          "message_id": "syn-refund_complaint-013-m1",
          "quote": "I did not know these add-ons would stay active"
        }
      ]
    },
    {
      "id": "f8",
      "text": "Mia had not deployed any project since the downgrade. She asked for both add-ons to be removed and for a one-time exception refund.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-013-m1",
          "quote": "I have not deployed any project since the downgrade"
        },
        {
          "message_id": "syn-refund_complaint-013-m1",
          "quote": "Please remove both add-ons"
        }
      ]
    },
    {
      "id": "f9",
      "text": "In October 2025 Mia agreed to have the refund sent to her original payment method.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-013-m2",
          "quote": "the original payment method is fine"
        }
      ]
    },
    {
      "id": "f10",
      "text": "Mia's style with them: she states the facts with exact dates and amounts, then asks them to confirm the refund amount and that no further charges will be made. Her follow-up replies are one line.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-013-m1",
          "quote": "Please confirm that the add-ons are removed"
        },
        {
          "message_id": "syn-refund_complaint-002-m1",
          "quote": "Please confirm the amount being refunded"
        }
      ]
    }
  ],
  "edges": [],
  "core_connection": {
    "text": "Vercel's billing support team, which Mia contacts to dispute charges and request refunds on her Vercel account.",
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

# Vercel Billing Team

Vercel's billing support team, which Mia contacts to dispute charges and request refunds on her Vercel account.

- Address (default): Vercel Billing Team (2/4 emails)
- This is Vercel's billing support team; Mia writes to them about charges on her Vercel account.
- In October 2024 Mia was charged twice ($20.00 each) for the same Pro plan period (October 7 to November 6, 2024).
- Mia's Vercel account had only one team and one seat at that time.
- Mia asked them to check that the subscription was not set up twice, and to confirm she would only be billed once from then on.
- In October 2024 Mia agreed to have the duplicate charge refunded to her card on file.
- Mia downgraded her team to the Hobby plan on September 20, 2025.
- On October 13, 2025 Mia was still charged $20.00 for the Web Analytics Plus and Speed Insights add-ons after the downgrade. She had not known the add-ons would stay active.
- Mia had not deployed any project since the downgrade. She asked for both add-ons to be removed and for a one-time exception refund.
- In October 2025 Mia agreed to have the refund sent to her original payment method.
- Mia's style with them: she states the facts with exact dates and amounts, then asks them to confirm the refund amount and that no further charges will be made. Her follow-up replies are one line.

_Extracted offline by pipeline/extract.py; every entry is backed by verified quotes._
