import requests
import time
from logger import logger
from env import get_url
from PIL import Image
import io
import base64

def fetch_data(url, start, end):
    """Fetches data in a given range with authentication."""
    params = {'password': 'carrot', 'start': start, 'end': end}
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

def find_flag(url, batch_size=10000):
    """Searches for the flag by fetching data in batches."""
    start = 0
    end = start + batch_size
    start_time = time.time()

    while True:
        data = fetch_data(url, start, end)
        if data:
            logger.debug(f"Data fetched for range {start}-{end}: {data}")
            flag = check_for_flag(data)
            if flag:
                time_elapsed = time.time() - start_time
                logger.info(f"Flag found: {flag}")
                logger.info(f"Time taken to find the flag: {time_elapsed:.2f} seconds")
                return flag  # Return the flag if found
            start = end + 1  # Prepare the next batch
            end = start + batch_size
        else:
            time_elapsed = time.time() - start_time
            logger.info("No more data to fetch or failed to fetch.")
            logger.info(f"Total time elapsed without finding the flag: {time_elapsed:.2f} seconds")
            return None  # Return None if no data is found or end of data is reached

def bytes_to_image(byte_data,output_path):
    try:
        image_data = base64.b64decode(byte_data)
        image = Image.open(io.BytesIO(image_data))
        image.save(output_path)
        logger.info(f"Image saved to {output_path}")
        return image
    except Exception as e:
        logger.error(f"Failed to convert bytes to image: {e}")
        return None

if __name__ == "__main__":
    url = get_url()
    flag = find_flag(url)
    if flag:
        image_path = "italiandude.png"
        image = bytes_to_image(flag, image_path)
        if image:
            image.show()
    print(f"Flag: {flag if flag else 'Not found'}")
