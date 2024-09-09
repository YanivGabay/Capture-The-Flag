import os
from dotenv import load_dotenv
import validators

load_dotenv()

ENV = os.getenv('ENV','development')
print(f"Running in {ENV} environment")
ENDPOINT = os.getenv('ENDPOINT_URL')
print(f"This is the endpoint: {ENDPOINT}")

if not validators.url(ENDPOINT):
    raise ValueError("Invalid URL")

if ENV not in ['dev','development','prod','production']:
    ENV = 'development'
