---
{
  "email": "delivery@oakandco.example.com",
  "display_name": "Oak & Co Delivery Team",
  "relationship": "furniture vendor",
  "address_as": {
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
  },
  "address_as_by_context": [
    {
      "context": "default",
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
    },
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
    }
  ],
  "sign_off": {
    "value": "Thank you,\nMia",
    "count": 3,
    "total": 5,
    "status": "learned",
    "evidence": [
      {
        "message_id": "syn-vendor_service-012-m1",
        "quote": "Thank you,\nMia"
      },
      {
        "message_id": "syn-vendor_service-012-m2",
        "quote": "Thank you,\nMia"
      },
      {
        "message_id": "syn-vendor_service-013-m2",
        "quote": "Thank you,\nMia"
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
        "quote": "A few details for the delivery team"
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
        "quote": "Following up on two things"
      }
    ]
  },
  "facts": [
    {
      "id": "f1",
      "text": "January 2025 order (walnut dining table and six chairs) was booked for Saturday, January 25, 8:00 AM to 12:00 PM.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-vendor_service-012-m1",
          "quote": "Saturday, January 25 window from 8:00 AM to 12:00 PM"
        }
      ]
    },
    {
      "id": "f2",
      "text": "There are three steps up to the front door, and the dining table goes into the first-floor dining room.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-vendor_service-012-m1",
          "quote": "There are three steps up to the front door."
        }
      ]
    },
    {
      "id": "f3",
      "text": "Mia added haul-away of the old dining table to the January 2025 delivery.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-vendor_service-012-m2",
          "quote": "Yes, please add the haul-away."
        }
      ]
    },
    {
      "id": "f4",
      "text": "Victor was the contact on the January 2025 delivery day.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-vendor_service-012-m2",
          "quote": "Contact on delivery day: Victor"
        }
      ]
    },
    {
      "id": "f5",
      "text": "Mia confirmed someone would be home all morning on the January 2025 delivery day.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-vendor_service-012-m3",
          "quote": "we'll be home all morning"
        }
      ]
    },
    {
      "id": "f6",
      "text": "Mia was away on June 9, 2026 and asked to move the sofa delivery to a weekend morning.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-vendor_service-013-m1",
          "quote": "We'll be away on June 9."
        },
        {
          "message_id": "syn-vendor_service-013-m1",
          "quote": "ideally in the morning window"
        }
      ]
    },
    {
      "id": "f7",
      "text": "Sofa delivery was confirmed for Saturday, June 13, 2026, 8:00 AM to 12:00 PM.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-vendor_service-013-m2",
          "quote": "Saturday, June 13 from 8:00 AM to 12:00 PM is perfect."
        }
      ]
    },
    {
      "id": "f8",
      "text": "The sofa goes up one flight of stairs to the loft. The stairway is 40 inches wide, and Mia asked the team to bring tools just in case.",
      "status": "learned",
      "evidence": [
        {
          "message_id": "syn-vendor_service-013-m2",
          "quote": "The sofa goes up one flight of stairs to the loft."
        },
        {
          "message_id": "syn-vendor_service-013-m2",
          "quote": "The stairway is 40 inches wide"
        },
        {
          "message_id": "syn-vendor_service-013-m2",
          "quote": "please bring the tools just in case"
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
          "message_id": "syn-vendor_service-013-m1",
          "quote": "Dear Dana,"
        }
      ]
    },
    {
      "to": "Victor",
      "type": "delivery_contact_for_mia",
      "evidence": [
        {
          "message_id": "syn-vendor_service-012-m2",
          "quote": "Contact on delivery day: Victor"
        }
      ]
    }
  ],
  "core_connection": {
    "text": "Oak & Co is the furniture store Mia has bought from more than once. Mia emails its delivery team to set delivery windows and give access details: a walnut dining table and six chairs in January 2025, and a Linden sofa in June 2026.",
    "evidence": [
      {
        "message_id": "syn-vendor_service-012-m1",
        "quote": "Thank you for letting us know the order is ready."
      },
      {
        "message_id": "syn-vendor_service-013-m1",
        "quote": "move the sofa delivery to Saturday, June 13"
      }
    ]
  },
  "external": []
}
---

# Oak & Co Delivery Team

Oak & Co is the furniture store Mia has bought from more than once. Mia emails its delivery team to set delivery windows and give access details: a walnut dining table and six chairs in January 2025, and a Linden sofa in June 2026.

- Address (default): Oak & Co (2/5 emails)
- Address (default): Dana (2/5 emails)
- January 2025 order (walnut dining table and six chairs) was booked for Saturday, January 25, 8:00 AM to 12:00 PM.
- There are three steps up to the front door, and the dining table goes into the first-floor dining room.
- Mia added haul-away of the old dining table to the January 2025 delivery.
- Victor was the contact on the January 2025 delivery day.
- Mia confirmed someone would be home all morning on the January 2025 delivery day.
- Mia was away on June 9, 2026 and asked to move the sofa delivery to a weekend morning.
- Sofa delivery was confirmed for Saturday, June 13, 2026, 8:00 AM to 12:00 PM.
- The sofa goes up one flight of stairs to the loft. The stairway is 40 inches wide, and Mia asked the team to bring tools just in case.

_Extracted offline by pipeline/extract.py; every entry is backed by verified quotes._
