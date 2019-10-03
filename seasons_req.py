import requests
import json
import time
import matplotlib.pyplot as plt


# Get info from RWC

# API Info - this requests print out all tournaments
api_key = 'n7qqfj52et4d63phqtqbwq5j'  # for rugby union
season_id = '59616'  # for rwc
response = requests.get('https://api.sportradar.us/rugby/trial/v2/union/en/seasons.json?api_key=' + api_key)

print('Get team status code: ' + str(response.status_code))
print('\n')

data = response.json()
print(json.dumps(data, indent=4, sort_keys=True))

seasons = data['seasons']

# Looping through all comps in season
for s in seasons:
    print(s['competition']['id'] + ' - ' + s['competition']['name'] + ' - ' + s['id'])

print(json.dumps(data, indent=4, sort_keys=True))
