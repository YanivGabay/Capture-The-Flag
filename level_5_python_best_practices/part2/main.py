from logger import logger

def main():
    logger.debug("This is a debug message")
    logger.debug("This msg wont show up in production")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")

if __name__ == "__main__":
    main()
