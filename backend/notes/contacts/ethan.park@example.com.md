---
email: ethan.park@example.com
display_name: Ethan Park
relationship: Her coach; they meet regularly for coaching sessions, often in person at coffee shops
scenario: friend_scheduling
address_as:
  value: Hey Ethan
  count: 15
  total: 46
  status: learned
  evidence:
  - message_id: 19e04c387de092e7
    quote: Hey Ethan,
  - message_id: 199e0f4032bd1990
    quote: Hey Ethan,
honorific:
  count: 0
  total: 46
  status: learned
  evidence: []
sign_off:
  value: Best,
  count: 13
  total: 46
  status: learned
  evidence:
  - message_id: 19ddf5cc113d2012
    quote: Best,
  - message_id: 19ba40a051210f63
    quote: Best,
language:
  value: English
  count: 46
  total: 46
  status: learned
  evidence:
  - message_id: 19ddf5cc113d2012
    quote: Do you have time on Friday?
facts:
- id: coaching_relationship
  text: Ethan is Mia's coach and they hold recurring coaching or check-in sessions.
  status: learned
  evidence:
  - message_id: 19ad08024b9953ee
    quote: check-in / coaching session?
- id: usual_spot_red_rock
  text: They often meet at Red Rock coffee, with Starbucks as the alternative.
  status: learned
  evidence:
  - message_id: 198ab7139243711d
    quote: see you tomorrow at Red Rock!
  - message_id: 19aa39943f651cad
    quote: Starbuck/redrock coffee ?
- id: prefers_offline
  text: Mia prefers meeting in person over Zoom when she can.
  status: learned
  evidence:
  - message_id: 19de5186aaeb9ed5
    quote: Are you available to meet offline?
- id: ethan_has_dog
  text: Ethan has a dog that needed vet visits.
  status: learned
  evidence:
  - message_id: 19a46d93cabaa53e
    quote: I hope your dog feels
  - message_id: 19a42551a63d1540
    quote: is your vet place located ?
- id: late_reschedules
  text: Mia has sometimes run late or moved sessions at the last minute and apologized.
  status: learned
  evidence:
  - message_id: syn-friend_scheduling-004-m3
    quote: will be about 15 minutes late.
  - message_id: 19aec3b81d52fc54
    quote: Sorry for the last-minute note
edges:
- to: Victor
  type: also_coached_by_ethan
  evidence:
  - message_id: 198af30eb0ec850f
    quote: I noticed your meeting with Victor wraps up around 2pm.
  - message_id: 199e38acd7fedecd
    quote: available before or after Victor's session today?
external: []
---
Extracted from 46 sent emails by app.pipeline.extract. Dropped quotes: 0.
