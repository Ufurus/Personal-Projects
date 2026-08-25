# target link: https://steamcommunity.com/profiles/76561198126545474/gcpd/440/
#Вашият Steam уеб API ключ
# Ключ: 485EC40E41D3AC8BF1584CE2605E5D94
# Домейн: localhost

API_KEY = '485EC40E41D3AC8BF1584CE2605E5D94'
USER_ID = 76561198126545474
APP_ID = 440

import json
import requests

#TODO more data information. Only achievements are available. Make more game stats like match history and inventory data.

def information_getter(given_data_type):
    text = ''

    if given_data_type == 'achievements':
        url_link = (f'http://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v0001/?appid='
                    f'{APP_ID}&key={API_KEY}&steamid={USER_ID}')
        target_file = 'data.json'

        response = requests.get(url_link)

        with open('data.json', 'w') as outfile:
            json.dump(response.json(), outfile)

        with open('data.json') as json_file:
            data = json.load(json_file)

        # achievement data
        with open('data.json', 'r') as f:
            information = json.load(f)
            for achivs, value in information.items():
                text += f'#{achivs}\n'
                for key, value in value.items():
                    if key != 'achievements':
                        text += f'{key} : {value}\n'
                        continue
                    text+= f'{key.upper()}:\n'
                    for achievement in value:
                        curr_achievement = [achievement['apiname'],
                                            achievement['achieved'],
                                            achievement['unlocktime']]

                        text += (f'achievement: {curr_achievement[0]},'
                                 f' unlocked: {curr_achievement[1]},'
                                 f' unlock time: {curr_achievement[2]}\n')

    #TODO - Match history information, currently searching for appropriate interface to use.
    elif given_data_type == 'match history':
        url_link = f''

        with open('data.json', 'w') as f:
            f.write(text)