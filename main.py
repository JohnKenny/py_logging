 # logging tests in python, log to file
 

import logging
import requests as rq

logging.basicConfig(level = logging.DEBUG, 
                    filename="log.out",
                    format='%(asctime)s - %(levelname)s - %(message)s')

def make_get_request(url: str) -> int:
    logging.debug(f"Function called with {url}")
    try:
        req = rq.get(url)
    except Exception as exc:
        logging.error(f"An error occured during the get request {exc}")
        return 404 
    else: 
        logging.info(f"Successful call to {url}, it returned {req.status_code}")
        return req.status_code

print(make_get_request("https://www.google.co.uk")) 

