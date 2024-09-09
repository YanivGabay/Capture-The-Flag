import logging
import os
from dotenv import load_dotenv
from env import get_env


def configure_logger():
    env = get_env()
    logger = logging.getLogger(__name__)
# Setting different log levels based on the environment
    if env == 'development':
        log_level = logging.DEBUG
    else:
        log_level = logging.ERROR  # Restrict to only errors in production

    # Creating a handler that outputs to the console
    handler = logging.StreamHandler()
    if env == 'development':
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    else:
        # Simplified format in production
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # set the format of the log
    # %(asctime)s: Adds the time of creation of the log record.
    # %(levelname)s: Adds the level of severity of the log record.
    # %(name)s: Adds the name of the logger used to log the call.
    # %(message)s: Adds the log message.
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    # set the format of the log
    handler.setFormatter(formatter)

    # set the log level
    handler.setLevel(log_level)

    # add the handler to the logger
    logger.addHandler(handler)

    # set the log level of the logger accordingly
    logger.setLevel(log_level)

    return logger


logger = configure_logger()