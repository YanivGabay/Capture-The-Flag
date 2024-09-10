import requests
import time
from env import get_url
from logger import logger

def fetch_data(url, start, end):
    params = {'password': 'dog', 'start': start, 'end': end}  # Ensure these are the correct parameter names expected by the API
    response = requests.get(url, params=params)
    if response.status_code == 200:
        try:
            return response.json()
        except ValueError:
            logger.error(f"Failed to decode JSON from response: {response.text}")
            return None
    else:
        logger.error(f"Failed to fetch data: {response.status_code}, {response.text}")
        return None

def check_for_flag(data, key='flag'):
    """ Check each item for the flag key directly. """
    if isinstance(data, list):  # Assuming the data is a list of dictionaries
        for item in data:
            if key in item:
                return item[key]
    return None

def main():
    url = get_url()
    batch_size = 10000
    start = 0
    end = start + batch_size
    start_time = time.time()  # Start timing

    while True:
        data = fetch_data(url, start, end)
        if data:
            print(data)
            flag = check_for_flag(data)
            if flag:
                time_elapsed = time.time() - start_time  # Calculate time elapsed
                print(f"Flag found: {flag}")
                print(f"Time taken to find the flag: {time_elapsed:.2f} seconds")
                break
            start = end + 1
            end = start + batch_size
        else:
            time_elapsed = time.time() - start_time  # Time when no data left
            print(f"No more data to fetch or failed to fetch.")
            print(f"Total time elapsed without finding the flag: {time_elapsed:.2f} seconds")
            break

if __name__ == "__main__":
    main()
