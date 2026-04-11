import logging
import time
from logging.handlers import RotatingFileHandler

handler = RotatingFileHandler(filename="log.out", 
                              maxBytes=2048, 
                              backupCount=4)

logger = logging.getLogger("MyLogger")
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

for _ in range(1000):
    statement = f"El momento es ahora {str(time.time())}"
    logger.debug(statement)















