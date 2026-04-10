import requests
from custom_loggers import logger

url = 'https://httpbin.org/get'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Datos de respuesta:")
    print(data["headers"])
else:
    print(f"La solicitud fallo con el codigo {response.status_code}")













