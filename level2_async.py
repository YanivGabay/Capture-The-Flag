import asyncio
import aiohttp
import time

async def fetch_data(session, base_url, start, end):
    params = {'start': start, 'end': end}
    async with session.get(base_url, params=params) as response:
        if response.status == 200:
            return await response.json()
        else:
            print(f"Failed to fetch data: {response.status}")
            return None
        
def check_for_flag(data, key='flag'):
    """ Check each item for the flag key directly. """
    for item in data:
        if key in item:
            return item[key]
    return None

async def main():
    """

    This function generates asynchronous requests to the server to fetch data and check if a flag exists within the data.
    The function uses the following variables:
    - base_url: The base URL of the server.
    - batch_size: The chunk size of data to be fetched in each request.
    - start: The starting index of the data to be fetched in each request.
    - end: The ending index of the data to be fetched in each request.
    The function uses an infinite loop to make requests until no more data is available to fetch.
    """
    base_url = "http://104.197.100.132:5000/level2/"  
    batch_size = 10000 
    start = 0
    end = start + batch_size

    start_time = time.time()  # Start timing

    async with aiohttp.ClientSession() as session:
        while True:
            data = await fetch_data(session, base_url, start, end)
            if data:
                flag = check_for_flag(data)
                if flag:
                    time_elapsed = time.time() - start_time 
                    print(f"Flag found: {flag}")
                    print(f"Time taken to find the flag: {time_elapsed:.2f} seconds")
                    break
                print(data)  
                start = end
                end += batch_size
            else:
                print("No more data to fetch or failed to fetch.")
                time_elapsed = time.time() - start_time  
                print(f"Time taken without finding the flag: {time_elapsed:.2f} seconds")
                break

if __name__ == "__main__":
    asyncio.run(main())
