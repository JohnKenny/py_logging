 # logging tests in python

import logging

logging.basicConfig(level = logging.DEBUG)

def add(a: int, b: int):
    logging.info(f"Se ha llamado a la funcion add con entradas {a}, {b}.")
    return a + b

print(add(10, 30))