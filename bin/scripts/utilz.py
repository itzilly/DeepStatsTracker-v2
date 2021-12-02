from bin.scripts import getLogger
from bin.scripts import handlers
from bin.scripts import solos
from bin.scripts import duos
from bin.scripts import threes
from bin.scripts import fours
from bin.scripts import FoF
from datetime import datetime
from mcuuid import MCUUID
import requests
import os


def get_uuid(player_name):
    player = MCUUID(name=player_name)
    getLogger.info(f"Translated {player_name} to " + player.uuid)
    return player.uuid


def get_name(player_uuid):
    player = MCUUID(uuid=player_uuid)
    getLogger.info(f"Translated {player_uuid} to " + player.name)
    return player.name


def get_key():
    try:
        with open('bin/api-key.txt', 'r') as keyer:
            content = keyer.readlines()
            str_key = str(content[2])
            keyer.close()
            return str_key
    except IndexError:
        getLogger.severe("Please ensure you have saved your API key in 'bin/api-key.text'")
        exit()


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
    path = 'bin/api-key.txt'
    exists = os.path.exists(path)
    if not exists:
        getLogger.warn(f"API Key not found, generating input file! Please set your API key in {path}")
        with open(path, 'w') as key_file:
            key_file.write("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # \n")
            key_file.write("Please enter your api key on the line below:\n")
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
    my_date = date()

    test2 = player['success']
    if not test2:
        getLogger.severe(f"{player_name} is a malformed UUID! Please enter a valid username")
        exit()

    try:
        test = player["player"]["achievements"]["bedwars_level"]
    except KeyError:
        getLogger.severe("Invalid API Key! Please ensure your API Key is correct ( bin/api-key.yaml )")
        print("Invalid API Key! Please ensure your API Key is correct ( bin/api-key.yaml )")
        exit()
    else:

        check_player_workbook(uuid, player_name)

        achievement = player["player"]["achievements"]
        stars = achievement.get('bedwars_level', 0)
        data = player['player']['stats']['Bedwars']

        solos.save(data, uuid, stars)
        duos.save(data, uuid, stars)
        threes.save(data, uuid, stars)
        fours.save(data, uuid, stars)
        FoF.save(data, uuid, stars)
        