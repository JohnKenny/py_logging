 # logging tests in python, Log Handlers
 
import logging

logging.basicConfig(level = logging.DEBUG)

def some_function():
    logging.debug("Mira, llamamos a la funcion.")
    return 123

some_function()

