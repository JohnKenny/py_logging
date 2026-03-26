 # logging tests in python, log to file

import logging
import requests as rq

logging.basicConfig(level = logging.INFO, 
                    filename="log.out",
                    format='%(asctime)s - %(levelname)s - %(message)s')

