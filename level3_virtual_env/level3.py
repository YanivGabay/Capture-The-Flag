import asyncio
import aiohttp
import time

async def fetch_data(session, base_url, start, end, timeout):
    params = {'start': start, 'end': end}
    try:
        async with session.get(base_url, params=params, timeout=timeout) as response:
            if response.status == 200:
                return await response.json(), True
            else:
                print(f"Failed to fetch data: {response.status}")
                return None, False
    except asyncio.TimeoutError:
        print("Request timed out")
        return None, False

async def adaptive_fetch(session, base_url, start, initial_batch_size, scale_back_factor):
    batch_size = initial_batch_size
   # timeout = 10  # Starting timeout in seconds
    while True:
        data, success = await fetch_data(session, base_url, start, start + batch_size, timeout)
        if data:
            yield data
            if success:
                start += batch_size
               # timeout = max(5, timeout - 1)  # Decrease timeout after a success
            else:
                batch_size = max(100, int(batch_size * scale_back_factor))  # Scale back batch size on failure
               # timeout += 5  # Increase timeout on failure
        else:
            if batch_size > 100:
            #or timeout < 30:
                batch_size = max(100, int(batch_size * scale_back_factor))
               # timeout = min(30, timeout + 5)  # Adjust timeout up to a maximum
            else:
                print("Stopping after minimum batch size and +++maximum timeout reached.")
                break

def check_for_flag(data, key='flag'):
    for item in data:
        if key in item:
            return item[key]
    return None

async def main():
    #http://34.69.146.51/ the correct addres which handles the pressure
    base_url = "http://104.197.100.132:5000/level3/"  
    initial_batch_size = 5000  # Reduced initial batch size
    scale_back_factor = 0.75  

    start_time = time.time()

    async with aiohttp.ClientSession() as session:
        async for data in adaptive_fetch(session, base_url, 0, initial_batch_size, scale_back_factor):
            flag = check_for_flag(data)
            if flag:
                time_elapsed = time.time() - start_time
                print(f"Flag found: {flag}")
                print(f"Time taken to find the flag: {time_elapsed:.2f} seconds")
                break
            print(data)

if __name__ == "__main__":
    asyncio.run(main())
