## Level 2 route:

http://104.197.100.132:5000/level2/
{
  "error": "Request processing took too long and timed out... , try to fetch part of the data by specifying start and end of a batch"
}

## so we obviosly need to give some paramters like start and end to the endpoint

they want a pythonic solution so we will use request to slowly fetch in batches the end point
you can check the solution on level2.py and level2_async.py (using aiohttp)

## so we need to do async work with python and fetch bt batches
i first tried 5 as a batch
than 10
than 50
than 100 which even this as too slow
currently running 1000 as batch and searching for the flag
1000 was too slow so i switched to 10000 than
it took around 96 secs im sure i can improve this further