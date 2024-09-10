
from logger import logger
from env import get_env, get_url
import requests
import time
## first part is to get the first password to probally get the image
## so lets try to shift triifk 

REQUEST_DELAY =2

def fetch_data(url,password):
    logger.debug(f"Trying password: {password} for url: {url}")
    params = {'password': password}  # Ensure these are the correct parameter names expected by the API
    response = requests.get(url, params=params)
    text = response.text
  
    ## if the response doesnt contain: ["error":"Password doesn't match triifk."]
    if "Password doesn't match triifk." not in text:
        logger.critical(f"Password found: {password}")
        try:
            return response.json()
        except ValueError:
            logger.error(f"Failed to decode JSON from response: {response.text}")
            return None
    else:
        logger.error(f"Failed to fetch data: {response.status_code}, {response.text}")
        return None
    
def decrypt_caesar_cipher(text, shifts=26):
    """ Decrypts a Caesar cipher by trying all possible shifts and returns a list of possible decryptions. """
    logger.debug(f"Decrypting text: {text}")
    decryptions = []
    for shift in range(1, shifts + 1):
        shifted_text = ''.join(chr((ord(char) - shift - 97) % 26 + 97) if 'a' <= char <= 'z' else char
                                for char in text.lower())
        decryptions.append((shift, shifted_text))
    return decryptions

def main():

    url = get_url()
    logger.debug(f"string to decrypt: triifk")
    decryptions = decrypt_caesar_cipher("triifk")
    logger.debug(f"Decryptions: {decryptions}")
    
    for shift, decrypted_password in decryptions[16:]:
        data = fetch_data(url,decrypted_password)
        logger.debug(f"sleeeping for {REQUEST_DELAY} seconds")
        time.sleep(REQUEST_DELAY)
        if data:
            print(data)
            break
        else:
            continue

if __name__ == "__main__":
    main()
