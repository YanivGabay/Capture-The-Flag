import logging
import os


def configure_logger():
    env = os.getenv('ENV', 'production')  # Default to production if not specified
    logger = logging.getLogger(__name__)

    URL = os.getenv('URL_PATH')
    if not URL:
        raise ValueError("URL_PATH environment variable not set")
    # Setting different log levels based on the environment
    if env == 'development':
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
