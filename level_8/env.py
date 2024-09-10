import os
from dotenv import load_dotenv

load_dotenv()

ENV = os.getenv('ENV')

GOOGLE_CRED = os.getenv('GOOGLE_CRED')
BUCKET_NAME = os.getenv('BUCKET_NAME')

if ENV not in ['dev','development','prod','production']:
    ENV = 'development'
print(f"Running in {ENV} environment")



# now we can use this ENV variable in other files
# without having to load the .env file again
def get_env():
    return ENV

def get_bucket_name():
    value = BUCKET_NAME
    if not value:
        raise ValueError("BUCKET_NAME environment variable not set")
    return value

def get_google_cred():
    value = GOOGLE_CRED
    if not value:
        raise ValueError("GOOGLE_CRED environment variable not set")
    return value
    r