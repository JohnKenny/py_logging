# module for logging configs
import logging

my_formatter = logging.Formatter(f'%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def file_logger() -> logging.FileHandler:
    """Defines and returns a file handler"""
    file_logger = logging.FileHandler("log.out")
    file_logger.setLevel(logging.DEBUG)
    file_logger.setFormatter(my_formatter)
    
    return file_logger

def console_logger() -> logging.StreamHandler:
    """Defines and returns a stream handler"""
    console_logger = logging.StreamHandler()
    console_logger.setLevel(logging.INFO)
    console_logger.setFormatter(my_formatter)
    
    return console_logger

def my_logger() -> logging.Logger:
    """ Function defines a multi-output logger"""
    logger = logging.getLogger("Mylogger")
    logger.setLevel(level=logging.DEBUG)
    logger.addHandler(file_logger())
    logger.addHandler(console_logger())

    return logger

logger = my_logger()