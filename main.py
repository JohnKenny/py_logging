 # logging tests in python, Log Handlers
 
import logging

logger = logging.getLogger("Mylogger")

# Adds file handler
file_logger = logging.FileHandler("log.out")
file_logger.setLevel(logging.DEBUG)

# Adds console handler
console_logger = logging.StreamHandler()
console_logger.setLevel(logging.INFO)



