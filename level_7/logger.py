import logging
import os
from env import get_env

def configure_logger():
    #default should be dev, make sense!!! (previosly was development)
    env = get_env()  
    
    logger = logging.getLogger(__name__)

    URL = os.getenv('URL_PATH')
    if not URL:
        raise ValueError("URL_PATH environment variable not set")
    # Setting different log levels based on the environment
    print(f"loggin in {env} environment")
    if env == 'development' or 'dev':
        log_level = logging.DEBUG  # Log everything in development
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    else:
        # In production, log only errors and critical messages
        log_level = logging.ERROR
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # Creating a handler that outputs to the console
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    handler.setLevel(log_level)  # Set handler level based on environment

    # Add the handler to the logger
    logger.addHandler(handler)
    logger.setLevel(log_level)  # Set logger level based on environment

    return logger

logger = configure_logger()
