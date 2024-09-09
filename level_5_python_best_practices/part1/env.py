import os
from dotenv import load_dotenv
import validators

load_dotenv()

## the second argument is the default value
## in case the environment variable is not set
ENV = os.getenv('ENV','development')
print(f"Running in {ENV} environment")
ENDPOINT = os.getenv('ENDPOINT_URL')
print(f"This is the endpoint: {ENDPOINT}")

if not validators.url(ENDPOINT):
    raise ValueError("Invalid URL")

## still as asked in the instructions
if ENV not in ['dev','development','prod','production']:
    ENV = 'development'


# now we can use this ENV variable in other files
# without having to load the .env file again
def get_env():
    return ENV