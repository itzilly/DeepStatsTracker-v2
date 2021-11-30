from bin.scripts import getLogger
from bin.scripts import handlers
from datetime import datetime
from mcuuid import MCUUID
import requests
import os
import yaml


def get_uuid(player_name):
    player = MCUUID(name=player_name)
    getLogger.info(f"Translated {player_name} to " + player.uuid)
    return player.uuid


def get_name(player_uuid):
    player = MCUUID(uuid=player_uuid)
    getLogger.info(f"Translated {player_uuid} to " + player.name)
    return player.name


def get_key():
    with open('bin/api-key.yaml') as keyer:
        key = yaml.load(keyer, Loader=yaml.FullLoader)
        return key


def time():
    now = datetime.now()
    fnow = now.strftime("%H-%M-%S")
    return fnow


def date():
    date = datetime.today()
    fdate = date.strftime("%m/%d/%Y")
    return fdate


def request(call):
    r = requests.get(call)
    return r.json()


# def checks(uuid, player_name):
#     check_data_folder()
#     check_player_workbook(uuid, player_name)
#     check_api_key()
#     check_tracking_list()


def check_data_folder():
    exists = os.path.exists('bin/playerData')
    if not exists:
        path = 'bin/playerData'
        os.mkdir(path)
        getLogger.warn(f"Player Data folder does not exist! Created Player Data folder in {path}")


def check_player_workbook(uuid, player_name):
    path = 'bin/playerData/' + uuid + '.xlsx'
    exists = os.path.exists(path)
    if not exists:
        getLogger.warn(f"Player's database doesn't exist! Creating player database for {player_name} in {path}")
        handlers.create_workbook(uuid, player_name)


def check_api_key():
    path = 'bin/api-key.yaml'
    exists = os.path.exists(path)
    if not exists:
        getLogger.warn(f"API Key not found, generating input file! Please set your API key in {path}")
        with open(path, 'w') as key_file:
            key_file.write("api-key: REPLACE_THIS_WITH_YOUR_API_KEY")
            key_file.close()


def check_tracking_list():
    path = 'bin/tracking-list.txt'
    exists = os.path.exists(path)
    if not exists:
        getLogger.warn(f"Tracking list file not found! Generating tracking file in {path}")
        with open(path, 'w') as trackers:
            trackers.write(" ")
            trackers.close()


def identity_theft(player_name):
    getLogger.info(f"Scraping {player_name}'s stats")
    uuid = get_uuid(player_name)
    key = get_key()
    url = f"https://api.hypixel.net/player?key={key}&uuid={uuid}"
    player = request(url)

    try:
        test = player["player"]["achievements"]["bedwars_level"]
        print(test)
    except KeyError:
        print("Invalid API Key! Please ensure your API Key is correct ( bin/api-key.yaml )")
    else:


        # Overall Statistics
        stars = player["player"]["achievements"]["bedwars_level"]
        kills = player["player"]["stats"]['Bedwars']['kills_bedwars']
        deaths = player["player"]["stats"]['Bedwars']['deaths_bedwars']
        kdr = kills / deaths
        final_deaths = player["player"]["stats"]['Bedwars']['final_deaths_bedwars']
        final_kills = player["player"]["stats"]['Bedwars']['final_kills_bedwars']
        fkdr = final_kills / final_deaths
        beds_broken = player["player"]["stats"]['Bedwars']['beds_broken_bedwars']
        beds_lost = player["player"]["stats"]['Bedwars']['beds_lost_bedwars']
        bblr = beds_broken / beds_lost
        coins = player["player"]["stats"]['Bedwars']['coins']
        games_played = player["player"]["stats"]['Bedwars']['games_played_bedwars']
        wins = player["player"]["stats"]["Bedwars"]["wins_bedwars"]
        losses = player["player"]["stats"]['Bedwars']['losses_bedwars']
        wlr = wins / losses

        overall_data = [stars, kills, deaths, kdr, final_deaths, final_kills, fkdr, beds_broken, beds_lost, bblr, coins, wins, losses, wlr]

        overall_data_length = len(overall_data)
        i = 0
        while i < overall_data_length:
            try:
                overall_data[i]
            except KeyError:
                overall_data[i] = 0
            print(overall_data[i])
            i += 1


        check_player_workbook(uuid, player_name)
