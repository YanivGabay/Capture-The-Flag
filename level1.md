
## level 1 of the ctf challenge

after http://104.197.100.132:5000/level1/
[{"content":"Numquam ipsum ipsum dolorem sit ipsum quaerat neque.","id":"post-1-0"},{"content":"Non magnam aliquam tempora.","id":"post-1-1"},{"content":"Tempora non quiquia est quiquia sed ut.","id":"post-1-2"},{"content":"Ut est consectetur magnam ipsum modi porro est.","id":"post-1-3"},{"content":"Quisquam amet sit non labore dolore quiquia.","id":"post-1-4"},{"content":"Eius dolore amet aliquam quaerat.","id":"post-1-5"},{"content":"Dolorem aliquam neque amet.","flag":"First time's a charm!","id":"post-1-6"},{"content":"Eius etincidunt dolor voluptatem dolor.","id":"post-1-7"},{"content":"Labore eius voluptatem ipsum quaerat.","id":"post-1-8"},{"content":"Numquam adipisci modi dolor.","id":"post-1-9"}]

[
  {
    "content": "Numquam ipsum ipsum dolorem sit ipsum quaerat neque.",
    "id": "post-1-0"
  },
  {
    "content": "Non magnam aliquam tempora.",
    "id": "post-1-1"
  },
  {
    "content": "Tempora non quiquia est quiquia sed ut.",
    "id": "post-1-2"
  },
  {
    "content": "Ut est consectetur magnam ipsum modi porro est.",
    "id": "post-1-3"
  },
  {
    "content": "Quisquam amet sit non labore dolore quiquia.",
    "id": "post-1-4"
  },
  {
    "content": "Eius dolore amet aliquam quaerat.",
    "id": "post-1-5"
  },
  {
    "content": "Dolorem aliquam neque amet.",
    "flag": "First time's a charm!",
    "id": "post-1-6"
  },
  {
    "content": "Eius etincidunt dolor voluptatem dolor.",
    "id": "post-1-7"
  },
  {
    "content": "Labore eius voluptatem ipsum quaerat.",
    "id": "post-1-8"
  },
  {
    "content": "Numquam adipisci modi dolor.",
    "id": "post-1-9"
  }
]

## we have found the flag:
"First time's a charm!"

## level 2 route:
{
  "error": "Request processing took too long and timed out... , try to fetch part of the data by specifying start and end of a batch"
}
## so we obviosly need to give some paramters like start and end to the endpoint

they want a pythonic solution so we will use request to slowly fetch in batches the end point

