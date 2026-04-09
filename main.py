 # logging tests in python, Log Handlers
 
import logging

logger = logging.getLogger("Mylogger")
logger.setLevel(level=logging.DEBUG)

# Adds file handler
file_logger = logging.FileHandler("log.out")
file_logger.setLevel(logging.DEBUG)

# Adds console handler
console_logger = logging.StreamHandler()
console_logger.setLevel(logging.INFO)

# Adds formatting
formatter = logging.Formatter(f'%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_logger.setFormatter(formatter)
console_logger.setFormatter(formatter)

# Adds handlers to the logger
logger.addHandler(file_logger)
logger.addHandler(console_logger)


def myfunc():
    logger.info("mensaje de informacion")
    logger.debug("mensaje de debug")

myfunc()



