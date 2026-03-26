 # logging tests in python

import logging

logging.basicConfig(level = logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def add(a: int, b: int):
    logging.info(f"Se ha llamado a la funcion add con entradas {a}, {b}.")
    logging.debug(f"A is {a} of type: {type(a)}")
    logging.debug(f"B is {b} of type: {type(b)}")

    try:
        return a + b
    except Exception as exc:
        logging.error(f"An error occured in the add function, {exc}")
        return 0;


print(add(10, 30))