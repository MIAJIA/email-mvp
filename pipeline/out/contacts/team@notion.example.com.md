---
{
  "email": "team@notion.example.com",
  "display_name": "Notion Support",
  "relationship": "vendor support",
  "address_as": {
    "value": "Notion Support",
    "count": 4,
    "total": 7,
    "status": "learned",
    "evidence": [
      {
        "message_id": "syn-refund_complaint-003-m2",
        "quote": "Hello Notion Support,"
      },
      {
        "message_id": "syn-refund_complaint-003-m3",
        "quote": "Hello Notion Support,"
      },
      {
        "message_id": "syn-refund_complaint-014-m1",
        "quote": "Hello Notion Support,"
      },
      {
        "message_id": "syn-refund_complaint-014-m2",
        "quote": "Hello Notion Support,"
      }
    ]
  },
  "address_as_by_context": [
    {
      "context": "default",
      "value": "Notion Support",
      "count": 4,
      "total": 7,
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-003-m2",
          "quote": "Hello Notion Support,"
        },
        {
          "message_id": "syn-refund_complaint-003-m3",
          "quote": "Hello Notion Support,"
        },
        {
          "message_id": "syn-refund_complaint-014-m1",
          "quote": "Hello Notion Support,"
        },
        {
          "message_id": "syn-refund_complaint-014-m2",
          "quote": "Hello Notion Support,"
        }
      ]
    },
    {
      "context": "formal",
      "value": "Notion Billing Team",
      "count": 2,
      "total": 7,
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-003-m1",
          "quote": "Hello Notion Billing Team,"
        },
        {
          "message_id": "syn-refund_complaint-024-m1",
          "quote": "Hello Notion Billing Team,"
        }
      ]
    }
  ],
  "sign_off": {
    "value": "Thank you,\nMia",
    "count": 7,
    "total": 7,
    "status": "learned",
    "evidence": [
      {
        "message_id": "syn-refund_complaint-003-m1",
        "quote": "Thank you,"
      },
      {
        "message_id": "syn-refund_complaint-003-m2",
        "quote": "Thank you,"
      },
      {
        "message_id": "syn-refund_complaint-003-m3",
        "quote": "Thank you,"
      },
      {
        "message_id": "syn-refund_complaint-014-m1",
        "quote": "Thank you,"
      },
      {
        "message_id": "syn-refund_complaint-014-m2",
        "quote": "Thank you,"
      },
      {
        "message_id": "syn-refund_complaint-024-m1",
        "quote": "Thank you,"
      },
      {
        "message_id": "syn-refund_complaint-024-m2",
        "quote": "Thank you,"
      }
    ]
  },
  "language": {
    "value": "en",
    "count": 7,
    "total": 7,
    "status": "learned",
    "evidence": [
      {
        "message_id": "syn-refund_complaint-003-m1",
        "quote": "Please confirm the cancellation"
      },
      {
        "message_id": "syn-refund_complaint-003-m2",
        "quote": "I'm asking for a review of the remaining $48.00"
      },
      {
        "message_id": "syn-refund_complaint-003-m3",
        "quote": "I understand that the prorated refund is the standard policy"
      },
      {
        "message_id": "syn-refund_complaint-014-m1",
        "quote": "I noticed a monthly Notion AI add-on charge"
      },
      {
        "message_id": "syn-refund_complaint-014-m2",
        "quote": "Thank you for refunding the October and November charges."
      },
      {
        "message_id": "syn-refund_complaint-024-m1",
        "quote": "Only one member has used the workspace this month."
      },
      {
        "message_id": "syn-refund_complaint-024-m2",
        "quote": "Thanks for checking the history."
      }
    ]
  },
  "facts": [
    {
      "id": "f1",
      "text": "Mia's annual Notion Plus plan renewed on Nov 18, 2024 for $96.00. She asked to cancel it and downgrade to Free the next day.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-003-m1",
          "quote": "renewed yesterday, November 18, 2024, for $96.00"
        }
      ]
    },
    {
      "id": "f2",
      "text": "At that time her workspace had had no activity since Feb 11, 2024, and she was its only member.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-003-m1",
          "quote": "I am the only member"
        },
        {
          "message_id": "syn-refund_complaint-003-m3",
          "quote": "no activity in the workspace since February 11, 2024"
        }
      ]
    },
    {
      "id": "f3",
      "text": "Mia wants refunds sent to the original payment method, not given as account credits.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-003-m1",
          "quote": "I would prefer the refund to the original payment method rather than account credits"
        }
      ]
    },
    {
      "id": "f4",
      "text": "Notion refunded $48.00 prorated for the 2024 renewal. Mia asked for the remaining $48.00 to be escalated to a supervisor.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-003-m3",
          "quote": "$48.00 has been refunded and $48.00 remains"
        },
        {
          "message_id": "syn-refund_complaint-003-m3",
          "quote": "please escalate the request to the billing team or a supervisor"
        }
      ]
    },
    {
      "id": "f5",
      "text": "A Notion AI add-on charged her $10/month from May to Nov 2025, $70 in total, after she tried it once in an April trial. She removed it on Nov 11, 2025.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-014-m1",
          "quote": "seven charges from May 5 through November 5, 2025, for a total of $70.00"
        },
        {
          "message_id": "syn-refund_complaint-014-m1",
          "quote": "I have removed the add-on from my workspace settings today."
        }
      ]
    },
    {
      "id": "f6",
      "text": "Notion refunded the Oct and Nov 2025 AI charges. Mia asked for a review of the remaining five charges ($50.00), saying the add-on was never used.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-014-m2",
          "quote": "which total $50.00"
        },
        {
          "message_id": "syn-refund_complaint-014-m2",
          "quote": "no AI requests after the trial in April"
        }
      ]
    },
    {
      "id": "f7",
      "text": "Her Sept 5, 2026 invoice charged for two members ($24.00). She disputes $12.00 because she removed the second member on Aug 30, 2026.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-024-m1",
          "quote": "charged me for two members at $12.00 each"
        },
        {
          "message_id": "syn-refund_complaint-024-m1",
          "quote": "I removed them on August 30, 2026, before the billing date"
        }
      ]
    },
    {
      "id": "f8",
      "text": "When support first refunds only part of a charge, Mia asks again for a review or an escalation and asks for the maximum refund allowed.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-014-m2",
          "quote": "please escalate the request and refund the maximum amount permitted"
        }
      ]
    },
    {
      "id": "f9",
      "text": "In follow-up emails she adds her account email under her signature.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-003-m3",
          "quote": "account email: [EMAIL]"
        },
        {
          "message_id": "syn-refund_complaint-024-m2",
          "quote": "account email: [EMAIL]"
        }
      ]
    }
  ],
  "edges": [
    {
      "to": "billing@notion.example.com",
      "type": "same_organization",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-003-m1",
          "quote": "Hello Notion Billing Team,"
        }
      ]
    }
  ],
  "core_connection": {
    "text": "Notion's customer support team, which Mia contacts as a Notion customer to dispute charges and ask for refunds on her workspace plan and add-ons.",
    "evidence": [
      {
        "message_id": "syn-refund_complaint-003-m1",
        "quote": "Please cancel my Plus plan"
      },
      {
        "message_id": "syn-refund_complaint-014-m1",
        "quote": "Could you please refund these charges"
      },
      {
        "message_id": "syn-refund_complaint-024-m1",
        "quote": "Please refund the extra $12.00"
      }
    ]
  },
  "external": []
}
---

# Notion Support

Notion's customer support team, which Mia contacts as a Notion customer to dispute charges and ask for refunds on her workspace plan and add-ons.

- Address (default): Notion Support (4/7 emails)
- Address (formal): Notion Billing Team (2/7 emails)
- Mia's annual Notion Plus plan renewed on Nov 18, 2024 for $96.00. She asked to cancel it and downgrade to Free the next day.
- At that time her workspace had had no activity since Feb 11, 2024, and she was its only member.
- Mia wants refunds sent to the original payment method, not given as account credits.
- Notion refunded $48.00 prorated for the 2024 renewal. Mia asked for the remaining $48.00 to be escalated to a supervisor.
- A Notion AI add-on charged her $10/month from May to Nov 2025, $70 in total, after she tried it once in an April trial. She removed it on Nov 11, 2025.
- Notion refunded the Oct and Nov 2025 AI charges. Mia asked for a review of the remaining five charges ($50.00), saying the add-on was never used.
- Her Sept 5, 2026 invoice charged for two members ($24.00). She disputes $12.00 because she removed the second member on Aug 30, 2026.
- When support first refunds only part of a charge, Mia asks again for a review or an escalation and asks for the maximum refund allowed.
- In follow-up emails she adds her account email under her signature.

_Extracted offline by pipeline/extract.py; every entry is backed by verified quotes._
