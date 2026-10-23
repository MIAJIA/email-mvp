---
{
  "email": "delivery@oakandco.example.com",
  "display_name": "Oak & Co Delivery Team",
  "relationship": "vendor",
  "address_as": {
    "value": "Dana",
    "count": 2,
    "total": 5,
    "status": "learned",
    "evidence": [
      {
        "message_id": "syn-vendor_service-013-m1",
        "quote": "Dear Dana,"
      },
      {
        "message_id": "syn-vendor_service-013-m2",
        "quote": "Dear Dana,"
      }
    ]
  },
  "address_as_by_context": [
    {
      "context": "default",
      "value": "Dana",
      "count": 2,
      "total": 5,
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-vendor_service-013-m1",
          "quote": "Dear Dana,"
        },
        {
          "message_id": "syn-vendor_service-013-m2",
          "quote": "Dear Dana,"
        }
      ]
    },
    {
      "context": "formal",
      "value": "Oak & Co",
      "count": 2,
      "total": 5,
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-vendor_service-012-m1",
          "quote": "Hi Oak & Co,"
        },
        {
          "message_id": "syn-vendor_service-012-m2",
          "quote": "Hi Oak & Co,"
        }
      ]
    }
  ],
  "sign_off": {
    "value": "Thank you, Mia",
    "count": 3,
    "total": 5,
    "status": "learned",
    "evidence": [
      {
        "message_id": "syn-vendor_service-012-m1",
        "quote": "Thank you,"
      },
      {
        "message_id": "syn-vendor_service-012-m2",
        "quote": "Thank you,"
      },
      {
        "message_id": "syn-vendor_service-013-m2",
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
        "message_id": "syn-vendor_service-012-m1",
        "quote": "Thank you for letting us know the order is ready."
      },
      {
        "message_id": "syn-vendor_service-012-m2",
        "quote": "Yes, please add the haul-away."
      },
      {
        "message_id": "syn-vendor_service-012-m3",
        "quote": "Yes, we'll be home all morning."
      },
      {
        "message_id": "syn-vendor_service-013-m1",
        "quote": "We'll be away on June 9."
      },
      {
        "message_id": "syn-vendor_service-013-m2",
        "quote": "Thank you so much!"
      }
    ]
  },
  "facts": [
    {
      "id": "f1",
      "text": "This is the delivery team of Oak & Co, a furniture vendor Mia has ordered from more than once.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-vendor_service-012-m1",
          "quote": "A few details for the delivery team:"
        }
      ]
    },
    {
      "id": "f2",
      "text": "Dana from the Oak & Co delivery team handled the June 2026 sofa delivery.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-vendor_service-013-m1",
          "quote": "Dear Dana,"
        }
      ]
    },
    {
      "id": "f3",
      "text": "In January 2025 Mia chose the delivery window of Saturday, January 25, 8:00 AM to 12:00 PM.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-vendor_service-012-m1",
          "quote": "Saturday, January 25 window from 8:00 AM to 12:00 PM"
        }
      ]
    },
    {
      "id": "f4",
      "text": "There are three steps up to Mia's front door, and the dining table went into the dining room on the first floor.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-vendor_service-012-m1",
          "quote": "There are three steps up to the front door."
        },
        {
          "message_id": "syn-vendor_service-012-m1",
          "quote": "dining room on the first floor"
        }
      ]
    },
    {
      "id": "f5",
      "text": "Mia asked about haul-away of her old dining table and then added it to the order.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-vendor_service-012-m1",
          "quote": "Is haul-away of our old dining table available"
        },
        {
          "message_id": "syn-vendor_service-012-m2",
          "quote": "Yes, please add the haul-away."
        }
      ]
    },
    {
      "id": "f6",
      "text": "Victor was the contact person on the January 2025 delivery day.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-vendor_service-012-m2",
          "quote": "Contact on delivery day: Victor"
        }
      ]
    },
    {
      "id": "f7",
      "text": "Mia confirmed that someone would be home all morning on the January 2025 delivery day.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-vendor_service-012-m3",
          "quote": "we'll be home all morning"
        }
      ]
    },
    {
      "id": "f8",
      "text": "Mia was away on June 9, 2026, so she asked to move the sofa delivery to June 13 or 14, preferably in the morning.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-vendor_service-013-m1",
          "quote": "We'll be away on June 9."
        },
        {
          "message_id": "syn-vendor_service-013-m1",
          "quote": "Saturday, June 13 or Sunday, June 14"
        }
      ]
    },
    {
      "id": "f9",
      "text": "The sofa delivery was confirmed for Saturday, June 13, 2026, 8:00 AM to 12:00 PM.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-vendor_service-013-m2",
          "quote": "Saturday, June 13 from 8:00 AM to 12:00 PM is perfect"
        }
      ]
    },
    {
      "id": "f10",
      "text": "The sofa had to go up one flight of stairs to the loft, and the stairway is 40 inches wide.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-vendor_service-013-m2",
          "quote": "The sofa goes up one flight of stairs to the loft."
        },
        {
          "message_id": "syn-vendor_service-013-m2",
          "quote": "The stairway is 40 inches wide"
        }
      ]
    },
    {
      "id": "f11",
      "text": "Mia asked the team to bring tools in case the sofa legs had to come off.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-vendor_service-013-m2",
          "quote": "please bring the tools just in case"
        }
      ]
    },
    {
      "id": "f12",
      "text": "Mia prefers morning delivery windows (8:00 AM to 12:00 PM).",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-vendor_service-013-m1",
          "quote": "ideally in the morning window"
        }
      ]
    }
  ],
  "edges": [
    {
      "to": "Dana",
      "type": "staff_member",
      "evidence": [
        {
          "message_id": "syn-vendor_service-013-m2",
          "quote": "Dear Dana,"
        }
      ]
    },
    {
      "to": "Victor",
      "type": "delivery_contact",
      "evidence": [
        {
          "message_id": "syn-vendor_service-012-m2",
          "quote": "Contact on delivery day: Victor"
        }
      ]
    }
  ],
  "core_connection": {
    "text": "Oak & Co is a furniture store. Mia writes to its delivery team to book delivery slots and explain how to get the furniture into her home, first for a dining table in January 2025 and then for a sofa in June 2026.",
    "evidence": [
      {
        "message_id": "syn-vendor_service-012-m1",
        "quote": "Thank you for letting us know the order is ready."
      },
      {
        "message_id": "syn-vendor_service-013-m1",
        "quote": "move the sofa delivery"
      }
    ]
  },
  "external": []
}
---

# Oak & Co Delivery Team

Oak & Co is a furniture store. Mia writes to its delivery team to book delivery slots and explain how to get the furniture into her home, first for a dining table in January 2025 and then for a sofa in June 2026.

- Address (default): Dana (2/5 emails)
- Address (formal): Oak & Co (2/5 emails)
- This is the delivery team of Oak & Co, a furniture vendor Mia has ordered from more than once.
- Dana from the Oak & Co delivery team handled the June 2026 sofa delivery.
- In January 2025 Mia chose the delivery window of Saturday, January 25, 8:00 AM to 12:00 PM.
- There are three steps up to Mia's front door, and the dining table went into the dining room on the first floor.
- Mia asked about haul-away of her old dining table and then added it to the order.
- Victor was the contact person on the January 2025 delivery day.
- Mia confirmed that someone would be home all morning on the January 2025 delivery day.
- Mia was away on June 9, 2026, so she asked to move the sofa delivery to June 13 or 14, preferably in the morning.
- The sofa delivery was confirmed for Saturday, June 13, 2026, 8:00 AM to 12:00 PM.
- The sofa had to go up one flight of stairs to the loft, and the stairway is 40 inches wide.
- Mia asked the team to bring tools in case the sofa legs had to come off.
- Mia prefers morning delivery windows (8:00 AM to 12:00 PM).

_Extracted offline by pipeline/extract.py; every entry is backed by verified quotes._
