import os
from dotenv import load_dotenv
import validators

load_dotenv()

ENV = os.getenv('ENV')

ENDPOINT = os.getenv('URL_PATH')


if not validators.url(ENDPOINT):
    raise ValueError("Invalid URL")

if ENV not in ['dev','development','prod','production']:
    ENV = 'development'
print(f"Running in {ENV} environment")
print(f"This is the endpoint: {ENDPOINT}")


# now we can use this ENV variable in other files
# without having to load the .env file again
def get_env():
    return ENV

def get_url():
    return ENDPOINT