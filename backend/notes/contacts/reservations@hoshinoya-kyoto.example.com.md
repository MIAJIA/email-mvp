---
email: reservations@hoshinoya-kyoto.example.com
display_name: Kenji (HOSHINOYA Kyoto)
relationship: Reservations contact at HOSHINOYA Kyoto, the ryokan where Mia and Victor have stayed twice
scenario: vendor_service
address_as:
  value: Dear Kenji
  count: 6
  total: 8
  status: learned
  evidence:
  - message_id: syn-vendor_service-003-m1
    quote: Dear Kenji,
  - message_id: syn-vendor_service-018-m1
    quote: Dear Kenji,
honorific:
  count: 0
  total: 8
  status: learned
  evidence: []
sign_off:
  value: Thank you,
  count: 3
  total: 8
  status: learned
  evidence:
  - message_id: syn-vendor_service-003-m2
    quote: Thank you,
  - message_id: syn-vendor_service-004-m1
    quote: Thank you,
  - message_id: syn-vendor_service-018-m1
    quote: Thank you,
language:
  value: English
  count: 8
  total: 8
  status: learned
  evidence:
  - message_id: syn-vendor_service-004-m2
    quote: Thank you so much for finding it!
facts:
- id: repeat_guest
  text: Mia stayed at HOSHINOYA Kyoto March 28–30, 2025, and booked a return stay for April 6–8, 2026
  status: learned
  evidence:
  - message_id: syn-vendor_service-004-m1
    quote: Thank you so much for a wonderful stay from March 28 to 30.
  - message_id: syn-vendor_service-018-m1
    quote: it is lovely to hear from you again
- id: travels_with_victor
  text: Mia books for two adults, herself and Victor
  status: learned
  evidence:
  - message_id: syn-vendor_service-003-m1
    quote: '(2 adults: Mia & Victor)'
  - message_id: syn-vendor_service-018-m1
    quote: space for 2 adults (Mia & Victor)
- id: victor_no_raw_shellfish
  text: Victor prefers not to have raw shellfish; Mia asked the kitchen to swap that course
  status: learned
  evidence:
  - message_id: syn-vendor_service-003-m2
    quote: Victor prefers not to have raw shellfish
- id: scarf_shipped_ems
  text: Mia left a gray wool scarf in the room; Kenji found it and she paid for EMS shipping
  status: learned
  evidence:
  - message_id: syn-vendor_service-004-m1
    quote: I believe I left a gray wool scarf in our room
  - message_id: syn-vendor_service-004-m2
    quote: I've completed the payment for the EMS shipping.
- id: booked_experiences
  text: 'Mia books on-site experiences through Kenji: a 7:00 AM Zen meditation (2025) and a 3:00 PM tea ceremony (2026)'
  status: learned
  evidence:
  - message_id: syn-vendor_service-003-m2
    quote: Please reserve the 7:00 AM session on March 29 for both of us.
  - message_id: syn-vendor_service-018-m2
    quote: Please book the 3:00 PM tea ceremony on April 7 for both of us.
edges:
- to: Victor
  type: travel_companion
  evidence:
  - message_id: syn-vendor_service-003-m1
    quote: '(2 adults: Mia & Victor)'
external:
- id: ext-hoshinoya-001
  text: Autumn foliage night boat cruises on the Oi River run nightly from November 10 to November 30.
  source_label: Hotel news (mock)
  date: '2026-10-15'
---
Extracted from 8 sent emails by app.pipeline.extract. Dropped quotes: 0.
