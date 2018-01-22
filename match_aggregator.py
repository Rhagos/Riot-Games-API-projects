__author__ = "Daniel Wu"

import requests
import json
import os.path

def request_player_data(region, player_name, API_key):
    URL = "https://" + region + ".api.riotgames.com/lol/summoner/v3/summoners/by-name/" + player_name + "?api_key=" + API_key
    response = requests.get(URL)
    return response.json()

def request_matches(region, ID, API_key, recently):
    URL = "https://" + region + ".api.riotgames.com/lol/match/v3/matchlists/by-account/" + ID
    if recently:
        URL += "/recent"
    URL += "?api_key=" + API_key

    response = requests.get(URL)
    return response.json()

def log(filename, data):
    if os.path.isfile(filename) == False:
        open(filename, 'a').close()
    with open(filename, 'w') as outfile:
        json.dump(data, outfile)

def main():
    #region = sys.argv[1]
    #When you roll out to dynamic regions
    region = 'na1'
    API_key = 'RGAPI-610d0bf1-fbcd-464f-97d7-6c4c13ce46d8'
    player = 'Domath'
    player_data_JSON = request_player_data(region, player, API_key)
    log('domath_data.txt', player_data_JSON)
    player_id = str(player_data_JSON['id'])
    
    match_history_JSON = request_matches(region, player_id, API_key, True)
    print(match_history_JSON)
    log('recent_match_history_output.txt', match_history_JSON)

if __name__ == "__main__":
    main()





