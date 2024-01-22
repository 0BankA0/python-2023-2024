import requests

URL = "https://api.coindesk.com/v1/bpi/currentprice.json"


a = requests.get(URL)

dati = a.json()

print(dati)