#laika noteikšana

import requests

URL = "http://worldtimeapi.org/api/timezone/Europe/Riga"

dati = requests.get(URL)

print(dati)


laiksLAtvija = dati.json()


print(laiksLAtvija)


print(laiksLAtvija["utc_datetime"])

URL2 = "http://worldtimeapi.org/api/timezone/america/new_york"


dati2 = requests.get(URL2)


laiksasv = dati2.json()


print(laiksasv["datetime"])