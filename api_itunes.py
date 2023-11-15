import requests
import json

URL = "http://itunes.apple.com/search?entity=song&limit=25&term=post_malone?"


atbilde = requests.get(URL)

print(atbilde)

dati = atbilde.json()

print(json.dumps(dati,indent = 2))


#konkreta lieluma izvadišana


#print(dati['results'][0]['trackName'])

for song in dati['results']:
    songn = song['trackName']
    print
