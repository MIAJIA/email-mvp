---
{
  "email": "support@peloton.example.com",
  "display_name": "Peloton Member Support",
  "relationship": "customer support",
  "address_as": {
    "value": "Peloton Member Support",
    "count": 4,
    "total": 7,
    "status": "learned",
    "evidence": [
      {
        "message_id": "syn-refund_complaint-005-m1",
        "quote": "Hello Peloton Member Support,"
      },
      {
        "message_id": "syn-refund_complaint-016-m1",
        "quote": "Hello Peloton Member Support,"
      },
      {
        "message_id": "syn-refund_complaint-025-m1",
        "quote": "Hello Peloton Member Support,"
      },
      {
        "message_id": "syn-refund_complaint-025-m2",
        "quote": "Hello Peloton Member Support,"
      }
    ]
  },
  "address_as_by_context": [
    {
      "context": "default",
      "value": "Peloton Member Support",
      "count": 4,
      "total": 7,
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-005-m1",
          "quote": "Hello Peloton Member Support,"
        },
        {
          "message_id": "syn-refund_complaint-016-m1",
          "quote": "Hello Peloton Member Support,"
        },
        {
          "message_id": "syn-refund_complaint-025-m1",
          "quote": "Hello Peloton Member Support,"
        },
        {
          "message_id": "syn-refund_complaint-025-m2",
          "quote": "Hello Peloton Member Support,"
        }
      ]
    }
  ],
  "sign_off": {
    "value": "Thank you, Mia",
    "count": 6,
    "total": 7,
    "status": "learned",
    "evidence": [
      {
        "message_id": "syn-refund_complaint-005-m1",
        "quote": "Thank you,"
      },
      {
        "message_id": "syn-refund_complaint-005-m2",
        "quote": "Thank you,"
      },
      {
        "message_id": "syn-refund_complaint-016-m1",
        "quote": "Thank you,"
      },
      {
        "message_id": "syn-refund_complaint-016-m2",
        "quote": "Thank you,"
      },
      {
        "message_id": "syn-refund_complaint-025-m1",
        "quote": "Thank you,"
      },
      {
        "message_id": "syn-refund_complaint-025-m2",
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
        "message_id": "syn-refund_complaint-005-m1",
        "quote": "Please cancel my App One membership"
      },
      {
        "message_id": "syn-refund_complaint-005-m2",
        "quote": "Thanks for cancelling the membership"
      },
      {
        "message_id": "syn-refund_complaint-016-m1",
        "quote": "Please cancel my All-Access Membership"
      },
      {
        "message_id": "syn-refund_complaint-016-m2",
        "quote": "Thanks for cancelling the membership"
      },
      {
        "message_id": "syn-refund_complaint-025-m1",
        "quote": "Please cancel my App One annual membership"
      },
      {
        "message_id": "syn-refund_complaint-025-m2",
        "quote": "Thank you for cancelling the membership"
      },
      {
        "message_id": "syn-refund_complaint-025-m3",
        "quote": "Yes, please use the same payment method."
      }
    ]
  },
  "facts": [
    {
      "id": "f1",
      "text": "Peloton Member Support is the support team for Mia's Peloton subscriptions. She contacts them to cancel memberships and ask for refunds.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-005-m1",
          "quote": "Hello Peloton Member Support,"
        }
      ]
    },
    {
      "id": "f2",
      "text": "Mia mentions a billing team behind the support agents and asks support to escalate to them when a request can't be approved at the agent's level.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-016-m2",
          "quote": "review this with the billing team"
        },
        {
          "message_id": "syn-refund_complaint-005-m2",
          "quote": "please escalate the request"
        }
      ]
    },
    {
      "id": "f3",
      "text": "Mia always asks for refunds to the original payment method, not account credits, and asks them to confirm the cancellation, that no further charges will be made, and the total refunded.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-005-m1",
          "quote": "rather than account credits"
        },
        {
          "message_id": "syn-refund_complaint-016-m1",
          "quote": "that no further charges will be made"
        }
      ]
    },
    {
      "id": "f4",
      "text": "Mia usually asks for a 'one-time billing exception' and includes her account email at the end of her first message.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-005-m1",
          "quote": "a one-time billing exception"
        },
        {
          "message_id": "syn-refund_complaint-005-m1",
          "quote": "account email:"
        }
      ]
    },
    {
      "id": "f5",
      "text": "Feb 2025: Mia's App One free trial from October 2024 had turned into a paid plan without her noticing. She was charged $12.99 a month four times, $51.96 in total, and her last class was October 27, 2024.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-005-m1",
          "quote": "for a total of $51.96"
        },
        {
          "message_id": "syn-refund_complaint-005-m1",
          "quote": "My last class in the app was on October 27"
        }
      ]
    },
    {
      "id": "f6",
      "text": "Support cancelled App One and refunded only the February 18, 2025 charge. Mia asked for a review of the other three charges ($38.97).",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-005-m2",
          "quote": "refunding the February 18 charge"
        },
        {
          "message_id": "syn-refund_complaint-005-m2",
          "quote": "which total $38.97"
        }
      ]
    },
    {
      "id": "f7",
      "text": "Mia asked to cancel her All-Access Membership through the in-app chat on November 2, 2025, but it wasn't cancelled. She was charged $44.00 on December 2, 2025 and January 2, 2026, with no activity after October 30, 2025.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-016-m1",
          "quote": "through the chat in the app on November 2"
        },
        {
          "message_id": "syn-refund_complaint-016-m1",
          "quote": "a total of $88.00"
        }
      ]
    },
    {
      "id": "f8",
      "text": "Support refunded the January 2, 2026 charge but not December's. Mia says she still has the chat transcript with the agent's confirmation and offered to send it.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-016-m2",
          "quote": "refunding the January 2 charge"
        },
        {
          "message_id": "syn-refund_complaint-016-m2",
          "quote": "I still have the chat transcript"
        }
      ]
    },
    {
      "id": "f9",
      "text": "Sept 2026: Mia's App One annual membership renewed for $119.00 on September 27, 2026, with no reminder. Her last class was March 15, 2026, and she wrote two days after the charge.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-025-m1",
          "quote": "The membership renewed at $119.00."
        },
        {
          "message_id": "syn-refund_complaint-025-m1",
          "quote": "My last class was on March 15, 2026"
        },
        {
          "message_id": "syn-refund_complaint-025-m1",
          "quote": "I did not receive a reminder"
        }
      ]
    },
    {
      "id": "f10",
      "text": "Support gave a prorated refund of $109.08. Mia asked for a review of the remaining $9.92, and in October 2026 confirmed it should go to the same payment method.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-025-m2",
          "quote": "refunding $109.08"
        },
        {
          "message_id": "syn-refund_complaint-025-m2",
          "quote": "review of the remaining $9.92"
        },
        {
          "message_id": "syn-refund_complaint-025-m3",
          "quote": "Yes, please use the same payment method."
        }
      ]
    }
  ],
  "edges": [
    {
      "to": "Peloton billing team",
      "type": "colleague",
      "evidence": [
        {
          "message_id": "syn-refund_complaint-016-m2",
          "quote": "review this with the billing team"
        }
      ]
    }
  ],
  "core_connection": {
    "text": "Peloton's member support team, which Mia writes to when she cancels Peloton memberships and asks for refunds of renewal charges she didn't use.",
    "evidence": [
      {
        "message_id": "syn-refund_complaint-005-m1",
        "quote": "Please cancel my App One membership"
      },
      {
        "message_id": "syn-refund_complaint-016-m1",
        "quote": "Please cancel my All-Access Membership"
      },
      {
        "message_id": "syn-refund_complaint-025-m1",
        "quote": "refund the renewal charged on September 27"
      }
    ]
  },
  "external": []
}
---

# Peloton Member Support

Peloton's member support team, which Mia writes to when she cancels Peloton memberships and asks for refunds of renewal charges she didn't use.

- Address (default): Peloton Member Support (4/7 emails)
- Peloton Member Support is the support team for Mia's Peloton subscriptions. She contacts them to cancel memberships and ask for refunds.
- Mia mentions a billing team behind the support agents and asks support to escalate to them when a request can't be approved at the agent's level.
- Mia always asks for refunds to the original payment method, not account credits, and asks them to confirm the cancellation, that no further charges will be made, and the total refunded.
- Mia usually asks for a 'one-time billing exception' and includes her account email at the end of her first message.
- Feb 2025: Mia's App One free trial from October 2024 had turned into a paid plan without her noticing. She was charged $12.99 a month four times, $51.96 in total, and her last class was October 27, 2024.
- Support cancelled App One and refunded only the February 18, 2025 charge. Mia asked for a review of the other three charges ($38.97).
- Mia asked to cancel her All-Access Membership through the in-app chat on November 2, 2025, but it wasn't cancelled. She was charged $44.00 on December 2, 2025 and January 2, 2026, with no activity after October 30, 2025.
- Support refunded the January 2, 2026 charge but not December's. Mia says she still has the chat transcript with the agent's confirmation and offered to send it.
- Sept 2026: Mia's App One annual membership renewed for $119.00 on September 27, 2026, with no reminder. Her last class was March 15, 2026, and she wrote two days after the charge.
- Support gave a prorated refund of $109.08. Mia asked for a review of the remaining $9.92, and in October 2026 confirmed it should go to the same payment method.

_Extracted offline by pipeline/extract.py; every entry is backed by verified quotes._
