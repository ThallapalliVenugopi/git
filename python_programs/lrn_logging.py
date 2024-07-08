import logging

logging.basicConfig(filename="test.txt", level=logging.INFO,
                    format="%(levelname)s - %(asctime)s   - %(message)s", filemode='w')
logging.debug("I am a debug message")
logging.info("I am a info message")
logging.warning("I am a warning message")
logging.error("I am a error message")
logging.critical("I am a critical message")

logging.info(str(5*10))
