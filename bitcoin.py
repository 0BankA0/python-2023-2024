import requests
import json

URL = "https://api.coindesk.com/v1/bpi/currentprice.json"


a = requests.get(URL)

#dati = a.json()

#print(json.dumps(dati,indent = 2))






price = a.json()['bpi']['USD']['rate_float']


lietotajs = float(input('ievadi cik gribu nopirkt: '))

print(price * lietotajs)
