import requests
from custom_loggers import logger

url = 'https://httpbin.org/get'

try:
    response = requests.get(url)
    logger.info("Requesting from: %s", url)
except Exception as exc:
    logger.critical("Ocurrio un error critico.. %s", exc)
else:
    if response.status_code == 200:
        data = response.json()
        logger.info("Headers %s ", data["headers"])
    else:
        logger.error("Request failed with code: %s", response.status_code)













