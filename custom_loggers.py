# module for logging configs
import logging

def my_logger() -> logging.Logger:
    """ Function defines a multi-output logger"""
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

    return logger

logger = my_logger()