import requests
import time

def fetch_data(base_url, start, end):
    params = {'start': start, 'end': end}
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return None

def check_for_flag(data, key='flag'):
    """ Check each item for the flag key directly. """
    for item in data:
        if key in item:
            return item[key]
    return None

def main():
    base_url = "http://104.197.100.132:5000/level2/"
    batch_size = 10
    start = 0
    end = start + batch_size

    start_time = time.time()  # Start timing

    while True:
        data = fetch_data(base_url, start, end)
        if data:
            flag = check_for_flag(data)
            if flag:
                time_elapsed = time.time() - start_time  # Calculate time elapsed
                print(f"Flag found: {flag}")
                print(f"Time taken to find the flag: {time_elapsed:.2f} seconds")
                break
            print(data) 
            start = end
            end += batch_size
        else:
            time_elapsed = time.time() - start_time  # Time when no data left
            print(f"No more data to fetch or failed to fetch.")
            print(f"Total time elapsed without finding the flag: {time_elapsed:.2f} seconds")
            break

if __name__ == "__main__":
    main()
