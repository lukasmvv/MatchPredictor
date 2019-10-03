import requests
import json
import time
import matplotlib.pyplot as plt


# API Info
api_key = 'n7qqfj52et4d63phqtqbwq5j'  # for rugby union
season_id = '59616'  # for rwc

# RWC season request
response = requests.get('https://api.sportradar.us/rugby/trial/v2/union/en/seasons/sr:season:' + season_id + '/schedule.json?api_key=' + api_key)
print('Get team status code: ' + str(response.status_code))
print('\n')
data = response.json()
print(json.dumps(data, indent=4, sort_keys=True))

# Looping through all matches (this data does not include knock-out matches)
events = data['sport_events']
for e in events:
    team1 = e['competitors'][0]
    team1['tries'] = 0
    team2 = e['competitors'][1]
    team2['tries'] = 0
    match_date = e['scheduled']
    match_id = e['id']
    match_context = e['sport_event_context']
    status = e['status']
    venue = e['venue']

    # Getting match data
    time.sleep(0.5)
    match_response = requests.get('https://api.sportradar.us/rugby/trial/v2/union/en/matches/' + match_id + '/timeline.json?api_key=' + api_key)
    match_data = match_response.json()
    #print(json.dumps(match_data, indent=4, sort_keys=True))

    # Looping through match events looking for tries
    for t in match_data['timeline']:

        if t['type'] in ('try', 'penalty_try'):
            if t['team'] == 'home':
                team1['tries'] += 1
            elif t['team'] == 'away':
                team2['tries'] += 1

    # Printing info
    print('ID: ' + match_id + ' - ' + team1['abbreviation'] + ' vs ' + team2['abbreviation'])
    print(match_date + ' at ' + venue['name'] + ', ' + venue['city_name'] + ', ' + venue['country_name'])
    print('Match Status: ' + status)
    if status == 'closed':
        team1['score'] = match_data['sport_event_status']['home_score']
        team2['score'] = match_data['sport_event_status']['away_score']
        print(team1['abbreviation'] + ' ' + str(team1['score']) + '(' + str(team1['tries']) + ') : ' + str(team2['score']) + '(' + str(team2['tries']) + ') ' + team2['abbreviation'])
    print('\n')
