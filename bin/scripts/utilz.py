from bin.scripts import getLogger
from bin.scripts import handlers
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

    try:
        test = player["player"]["achievements"]["bedwars_level"]
    except KeyError:
        getLogger.severe("Invalid API Key! Please ensure your API Key is correct ( bin/api-key.yaml )")
        print("Invalid API Key! Please ensure your API Key is correct ( bin/api-key.yaml )")
        exit()
    else:

        achievement = player["player"]["achievements"]
        data = player['player']['stats']['Bedwars']

#
        # Overall Statistics
        # stars = achievement.get('bedwars_level', 0)
        # kills = data.get('kills_bedwars', 0)
        # deaths = data.get('deaths_bedwars', 0)
        # kdr = kills / deaths
        # final_kills = data.get('final_kills_bedwars', 0)
        # final_deaths = data.get('final_deaths_bedwars', 0)
        # fkdr = final_kills / final_deaths
        # beds_broken = data.get('beds_broken_bedwars', 0)
        # beds_lost = data.get('beds_lost_bedwars', 0)
        # bblr = beds_broken / beds_lost
        # games_played = data.get('games_played_bedwars', 0)
        # wins = data.get('wins_bedwars', 0)
        # losses = data.get('losses_bedwars', 0)
        # wlr = wins / losses
        # coins = data.get('coins', 0)
        # xp = data.get('Experience', 0)

#
        # Solos Statistics
#       DATE
        solos_final_kills = data.get('eight_one_final_kills_bedwars', 0)
        solos_final_void_kills = data.get('eight_one_void_final_kills_bedwars', 0)
        solos_final_projectile_kills = data.get('eight_one_projectile_final_kills_bedwars', 0)
        solos_final_fall_kills = data.get('eight_one_fall_final_kills_bedwars', 0)
        solos_final_explosion_kills = data.get('eight_one_fire_tick_final_kills_bedwars', 0)
        solos_final_magic_kills = data.get('eight_one_magic_final_kills_bedwars', 0)
        solos_final_suffocation_kills = data.get('eight_one_suffocation_final_kills_bedwars', 0)

        solos_final_deaths = data.get('eight_one_final_deaths_bedwars', 0)
        solos_final_void_deaths = data.get('eight_one_void_final_deaths_bedwars', 0)
        solos_final_projectile_deaths = data.get('eight_one_projectile_final_deaths_bedwars', 0)
        solos_final_fall_deaths = data.get('eight_one_fall_final_deaths_bedwars', 0)
        solos_final_explosion_deaths = data.get('eight_one_fire_tick_final_deaths_bedwars', 0)
        solos_final_magic_deaths = data.get('eight_one_magic_final_deaths_bedwars', 0)
        solos_final_suffocation_deaths = data.get('eight_one_suffocation_final_deaths_bedwars', 0)

        solos_fkdr = solos_final_kills / solos_final_deaths

        solos_kills = data.get('eight_one_kills_bedwars', 0)
        solos_void_kills = data.get('eight_one_void_kills_bedwars', 0)
        solos_projectile_kills = data.get('eight_one_projectile_kills_bedwars', 0)
        solos_fall_kills = data.get('eight_one_fall_kills_bedwars', 0)
        solos_explosion_kills = data.get('eight_one_fire_tick_kills_bedwars', 0)
        solos_magic_kills = data.get('eight_one_magic_kills_bedwars', 0)
        solos_suffocation_kills = data.get('eight_one_suffocation_kills_bedwars', 0)

        solos_deaths = data.get('eight_one_deaths_bedwars', 0)
        solos_void_deaths = data.get('eight_one_void_deaths_bedwars', 0)
        solos_projectile_deaths = data.get('eight_one_projectile_deaths_bedwars', 0)
        solos_fall_deaths = data.get('eight_one_fall_deaths_bedwars', 0)
        solos_explosion_deaths = data.get('eight_one_fire_tick_deaths_bedwars', 0)
        solos_magic_deaths = data.get('eight_one_magic_deaths_bedwars', 0)
        solos_suffocation_deaths = data.get('eight_one_suffocation_deaths_bedwars', 0)

        solos_kdr = solos_kills / solos_deaths

        solos_games_played = data.get('eight_one_games_played_bedwars', 0)
        solos_wins = data.get('eight_one_wins_bedwars', 0)
        solos_losses = data.get('eight_one_losses_bedwars', 0)
        solos_wlr = solos_wins / solos_losses

        solos_iron = data.get('eight_one_iron_resources_collected_bedwars', 0)
        solos_gold = data.get('eight_one_gold_resources_collected_bedwars', 0)
        solos_diamonds = data.get('eight_one_diamond_resources_collected_bedwars', 0)
        solos_emeralds = data.get('eight_one_emerald_resources_collected_bedwars', 0)
        solos_total_resources = solos_iron + solos_gold + solos_diamonds + solos_emeralds

        solos_purchases = data.get('eight_one_items_purchased_bedwars', 0)
        solos_permanent_purchases = data.get('eight_one_permanent _items_purchased_bedwars', 0)

        check_player_workbook(uuid, player_name)

#

        solo_stats = [my_date, solos_final_kills, solos_final_void_kills,
                      solos_final_projectile_kills, solos_final_fall_kills,
                      solos_final_explosion_kills, solos_final_magic_kills,
                      solos_final_suffocation_kills, solos_final_deaths,
                      solos_final_void_deaths, solos_final_projectile_deaths,
                      solos_final_fall_deaths, solos_final_explosion_deaths,
                      solos_final_magic_deaths, solos_final_suffocation_deaths,
                      solos_fkdr, solos_kills, solos_void_kills,
                      solos_projectile_kills, solos_fall_kills, solos_explosion_kills,
                      solos_magic_kills, solos_suffocation_kills, solos_deaths,
                      solos_void_deaths, solos_projectile_deaths, solos_fall_deaths,
                      solos_explosion_deaths, solos_magic_deaths, solos_suffocation_deaths,
                      solos_kdr, solos_games_played, solos_wins, solos_losses, solos_wlr,
                      solos_iron, solos_gold, solos_diamonds, solos_emeralds,
                      solos_total_resources, solos_purchases, solos_permanent_purchases]

        handlers.save_solos(uuid, solo_stats)

        # Duos Statistics
        #       DATE
        duos_final_kills = data.get('eight_two_final_kills_bedwars', 0)
        duos_final_void_kills = data.get('eight_two_void_final_kills_bedwars', 0)
        duos_final_projectile_kills = data.get('eight_two_projectile_final_kills_bedwars', 0)
        duos_final_fall_kills = data.get('eight_two_fall_final_kills_bedwars', 0)
        duos_final_explosion_kills = data.get('eight_two_fire_tick_final_kills_bedwars', 0)
        duos_final_magic_kills = data.get('eight_two_magic_final_kills_bedwars', 0)
        duos_final_suffocation_kills = data.get('eight_two_suffocation_final_kills_bedwars', 0)

        duos_final_deaths = data.get('eight_two_final_deaths_bedwars', 0)
        duos_final_void_deaths = data.get('eight_two_void_final_deaths_bedwars', 0)
        duos_final_projectile_deaths = data.get('eight_two_projectile_final_deaths_bedwars', 0)
        duos_final_fall_deaths = data.get('eight_two_fall_final_deaths_bedwars', 0)
        duos_final_explosion_deaths = data.get('eight_two_fire_tick_final_deaths_bedwars', 0)
        duos_final_magic_deaths = data.get('eight_two_magic_final_deaths_bedwars', 0)
        duos_final_suffocation_deaths = data.get('eight_two_suffocation_final_deaths_bedwars', 0)

        duos_fkdr = duos_final_kills / duos_final_deaths

        duos_kills = data.get('eight_two_kills_bedwars', 0)
        duos_void_kills = data.get('eight_two_void_kills_bedwars', 0)
        duos_projectile_kills = data.get('eight_two_projectile_kills_bedwars', 0)
        duos_fall_kills = data.get('eight_two_fall_kills_bedwars', 0)
        duos_explosion_kills = data.get('eight_two_fire_tick_kills_bedwars', 0)
        duos_magic_kills = data.get('eight_two_magic_kills_bedwars', 0)
        duos_suffocation_kills = data.get('eight_two_suffocation_kills_bedwars', 0)

        duos_deaths = data.get('eight_two_deaths_bedwars', 0)
        duos_void_deaths = data.get('eight_two_void_deaths_bedwars', 0)
        duos_projectile_deaths = data.get('eight_two_projectile_deaths_bedwars', 0)
        duos_fall_deaths = data.get('eight_two_fall_deaths_bedwars', 0)
        duos_explosion_deaths = data.get('eight_two_fire_tick_deaths_bedwars', 0)
        duos_magic_deaths = data.get('eight_two_magic_deaths_bedwars', 0)
        duos_suffocation_deaths = data.get('eight_two_suffocation_deaths_bedwars', 0)

        duos_kdr = duos_kills / duos_deaths

        duos_games_played = data.get('eight_two_games_played_bedwars', 0)
        duos_wins = data.get('eight_two_wins_bedwars', 0)
        duos_losses = data.get('eight_two_losses_bedwars', 0)
        duos_wlr = duos_wins / duos_losses

        duos_iron = data.get('eight_two_iron_resources_collected_bedwars', 0)
        duos_gold = data.get('eight_two_gold_resources_collected_bedwars', 0)
        duos_diamonds = data.get('eight_two_diamond_resources_collected_bedwars', 0)
        duos_emeralds = data.get('eight_two_emerald_resources_collected_bedwars', 0)
        duos_total_resources = duos_iron + duos_gold + duos_diamonds + duos_emeralds

        duos_purchases = data.get('eight_two_items_purchased_bedwars', 0)
        duos_permanent_purchases = data.get('eight_two_permanent _items_purchased_bedwars', 0)

        duos_stats = [my_date, duos_final_kills, duos_final_void_kills,
                      duos_final_projectile_kills, duos_final_fall_kills,
                      duos_final_explosion_kills, duos_final_magic_kills,
                      duos_final_suffocation_kills, duos_final_deaths,
                      duos_final_void_deaths, duos_final_projectile_deaths,
                      duos_final_fall_deaths, duos_final_explosion_deaths,
                      duos_final_magic_deaths, duos_final_suffocation_deaths,
                      duos_fkdr, duos_kills, duos_void_kills,
                      duos_projectile_kills, duos_fall_kills, duos_explosion_kills,
                      duos_magic_kills, duos_suffocation_kills, duos_deaths,
                      duos_void_deaths, duos_projectile_deaths, duos_fall_deaths,
                      duos_explosion_deaths, duos_magic_deaths, duos_suffocation_deaths,
                      duos_kdr, duos_games_played, duos_wins, duos_losses, duos_wlr,
                      duos_iron, duos_gold, duos_diamonds, duos_emeralds,
                      duos_total_resources, duos_purchases, duos_permanent_purchases]

        handlers.save_duos(uuid, duos_stats)

        # Threes Statistics
        #       DATE
        threes_final_kills = data.get('four_three_final_kills_bedwars', 0)
        threes_final_void_kills = data.get('four_three_void_final_kills_bedwars', 0)
        threes_final_projectile_kills = data.get('four_three_projectile_final_kills_bedwars', 0)
        threes_final_fall_kills = data.get('four_three_fall_final_kills_bedwars', 0)
        threes_final_explosion_kills = data.get('four_three_fire_tick_final_kills_bedwars', 0)
        threes_final_magic_kills = data.get('four_three_magic_final_kills_bedwars', 0)
        threes_final_suffocation_kills = data.get('four_three_suffocation_final_kills_bedwars', 0)

        threes_final_deaths = data.get('four_three_final_deaths_bedwars', 0)
        threes_final_void_deaths = data.get('four_three_void_final_deaths_bedwars', 0)
        threes_final_projectile_deaths = data.get('four_three_projectile_final_deaths_bedwars', 0)
        threes_final_fall_deaths = data.get('four_three_fall_final_deaths_bedwars', 0)
        threes_final_explosion_deaths = data.get('four_three_fire_tick_final_deaths_bedwars', 0)
        threes_final_magic_deaths = data.get('four_three_magic_final_deaths_bedwars', 0)
        threes_final_suffocation_deaths = data.get('four_three_suffocation_final_deaths_bedwars', 0)

        threes_fkdr = threes_final_kills / threes_final_deaths

        threes_kills = data.get('four_three_kills_bedwars', 0)
        threes_void_kills = data.get('four_three_void_kills_bedwars', 0)
        threes_projectile_kills = data.get('four_three_projectile_kills_bedwars', 0)
        threes_fall_kills = data.get('four_three_fall_kills_bedwars', 0)
        threes_explosion_kills = data.get('four_three_fire_tick_kills_bedwars', 0)
        threes_magic_kills = data.get('four_three_magic_kills_bedwars', 0)
        threes_suffocation_kills = data.get('four_three_suffocation_kills_bedwars', 0)

        threes_deaths = data.get('four_three_deaths_bedwars', 0)
        threes_void_deaths = data.get('four_three_void_deaths_bedwars', 0)
        threes_projectile_deaths = data.get('four_three_projectile_deaths_bedwars', 0)
        threes_fall_deaths = data.get('four_three_fall_deaths_bedwars', 0)
        threes_explosion_deaths = data.get('four_three_fire_tick_deaths_bedwars', 0)
        threes_magic_deaths = data.get('four_three_magic_deaths_bedwars', 0)
        threes_suffocation_deaths = data.get('four_three_suffocation_deaths_bedwars', 0)

        threes_kdr = threes_kills / threes_deaths

        threes_games_played = data.get('four_three_games_played_bedwars', 0)
        threes_wins = data.get('four_three_wins_bedwars', 0)
        threes_losses = data.get('four_three_losses_bedwars', 0)
        threes_wlr = threes_wins / threes_losses

        threes_iron = data.get('four_three_iron_resources_collected_bedwars', 0)
        threes_gold = data.get('four_three_gold_resources_collected_bedwars', 0)
        threes_diamonds = data.get('four_three_diamond_resources_collected_bedwars', 0)
        threes_emeralds = data.get('four_three_emerald_resources_collected_bedwars', 0)
        threes_total_resources = threes_iron + threes_gold + threes_diamonds + threes_emeralds

        threes_purchases = data.get('four_three_items_purchased_bedwars', 0)
        threes_permanent_purchases = data.get('four_three_permanent _items_purchased_bedwars', 0)

        threes_stats = [my_date, threes_final_kills, threes_final_void_kills,
                      threes_final_projectile_kills, threes_final_fall_kills,
                      threes_final_explosion_kills, threes_final_magic_kills,
                      threes_final_suffocation_kills, threes_final_deaths,
                      threes_final_void_deaths, threes_final_projectile_deaths,
                      threes_final_fall_deaths, threes_final_explosion_deaths,
                      threes_final_magic_deaths, threes_final_suffocation_deaths,
                      threes_fkdr, threes_kills, threes_void_kills,
                      threes_projectile_kills, threes_fall_kills, threes_explosion_kills,
                      threes_magic_kills, threes_suffocation_kills, threes_deaths,
                      threes_void_deaths, threes_projectile_deaths, threes_fall_deaths,
                      threes_explosion_deaths, threes_magic_deaths, threes_suffocation_deaths,
                      threes_kdr, threes_games_played, threes_wins, threes_losses, threes_wlr,
                      threes_iron, threes_gold, threes_diamonds, threes_emeralds,
                      threes_total_resources, threes_purchases, threes_permanent_purchases]

        handlers.save_threes(uuid, threes_stats)


        # Fours Statistics
        #       DATE
        fours_final_kills = data.get('four_four_final_kills_bedwars', 0)
        fours_final_void_kills = data.get('four_four_void_final_kills_bedwars', 0)
        fours_final_projectile_kills = data.get('four_four_projectile_final_kills_bedwars', 0)
        fours_final_fall_kills = data.get('four_four_fall_final_kills_bedwars', 0)
        fours_final_explosion_kills = data.get('four_four_fire_tick_final_kills_bedwars', 0)
        fours_final_magic_kills = data.get('four_four_magic_final_kills_bedwars', 0)
        fours_final_suffocation_kills = data.get('four_four_suffocation_final_kills_bedwars', 0)

        fours_final_deaths = data.get('four_four_final_deaths_bedwars', 0)
        fours_final_void_deaths = data.get('four_four_void_final_deaths_bedwars', 0)
        fours_final_projectile_deaths = data.get('four_four_projectile_final_deaths_bedwars', 0)
        fours_final_fall_deaths = data.get('four_four_fall_final_deaths_bedwars', 0)
        fours_final_explosion_deaths = data.get('four_four_fire_tick_final_deaths_bedwars', 0)
        fours_final_magic_deaths = data.get('four_four_magic_final_deaths_bedwars', 0)
        fours_final_suffocation_deaths = data.get('four_four_suffocation_final_deaths_bedwars', 0)

        fours_fkdr = fours_final_kills / fours_final_deaths

        fours_kills = data.get('four_four_kills_bedwars', 0)
        fours_void_kills = data.get('four_four_void_kills_bedwars', 0)
        fours_projectile_kills = data.get('four_four_projectile_kills_bedwars', 0)
        fours_fall_kills = data.get('four_four_fall_kills_bedwars', 0)
        fours_explosion_kills = data.get('four_four_fire_tick_kills_bedwars', 0)
        fours_magic_kills = data.get('four_four_magic_kills_bedwars', 0)
        fours_suffocation_kills = data.get('four_four_suffocation_kills_bedwars', 0)

        fours_deaths = data.get('four_four_deaths_bedwars', 0)
        fours_void_deaths = data.get('four_four_void_deaths_bedwars', 0)
        fours_projectile_deaths = data.get('four_four_projectile_deaths_bedwars', 0)
        fours_fall_deaths = data.get('four_four_fall_deaths_bedwars', 0)
        fours_explosion_deaths = data.get('four_four_fire_tick_deaths_bedwars', 0)
        fours_magic_deaths = data.get('four_four_magic_deaths_bedwars', 0)
        fours_suffocation_deaths = data.get('four_four_suffocation_deaths_bedwars', 0)

        fours_kdr = fours_kills / fours_deaths

        fours_games_played = data.get('four_four_games_played_bedwars', 0)
        fours_wins = data.get('four_four_wins_bedwars', 0)
        fours_losses = data.get('four_four_losses_bedwars', 0)
        fours_wlr = fours_wins / fours_losses

        fours_iron = data.get('four_four_iron_resources_collected_bedwars', 0)
        fours_gold = data.get('four_four_gold_resources_collected_bedwars', 0)
        fours_diamonds = data.get('four_four_diamond_resources_collected_bedwars', 0)
        fours_emeralds = data.get('four_four_emerald_resources_collected_bedwars', 0)
        fours_total_resources = fours_iron + fours_gold + fours_diamonds + fours_emeralds

        fours_purchases = data.get('four_four_items_purchased_bedwars', 0)
        fours_permanent_purchases = data.get('four_four_permanent _items_purchased_bedwars', 0)

        fours_stats = [my_date, fours_final_kills, fours_final_void_kills,
                       fours_final_projectile_kills, fours_final_fall_kills,
                       fours_final_explosion_kills, fours_final_magic_kills,
                       fours_final_suffocation_kills, fours_final_deaths,
                       fours_final_void_deaths, fours_final_projectile_deaths,
                       fours_final_fall_deaths, fours_final_explosion_deaths,
                       fours_final_magic_deaths, fours_final_suffocation_deaths,
                       fours_fkdr, fours_kills, fours_void_kills,
                       fours_projectile_kills, fours_fall_kills, fours_explosion_kills,
                       fours_magic_kills, fours_suffocation_kills, fours_deaths,
                       fours_void_deaths, fours_projectile_deaths, fours_fall_deaths,
                       fours_explosion_deaths, fours_magic_deaths, fours_suffocation_deaths,
                       fours_kdr, fours_games_played, fours_wins, fours_losses, fours_wlr,
                       fours_iron, fours_gold, fours_diamonds, fours_emeralds,
                       fours_total_resources, fours_purchases, fours_permanent_purchases]

        handlers.save_fours(uuid, fours_stats)


        # FoF Statistics
        #       DATE
        FoF_final_kills = data.get('two_four_final_kills_bedwars', 0)
        FoF_final_void_kills = data.get('two_four_void_final_kills_bedwars', 0)
        FoF_final_projectile_kills = data.get('two_four_projectile_final_kills_bedwars', 0)
        FoF_final_fall_kills = data.get('two_four_fall_final_kills_bedwars', 0)
        FoF_final_explosion_kills = data.get('two_four_fire_tick_final_kills_bedwars', 0)
        FoF_final_magic_kills = data.get('two_four_magic_final_kills_bedwars', 0)
        FoF_final_suffocation_kills = data.get('two_four_suffocation_final_kills_bedwars', 0)

        FoF_final_deaths = data.get('two_four_final_deaths_bedwars', 0)
        FoF_final_void_deaths = data.get('two_four_void_final_deaths_bedwars', 0)
        FoF_final_projectile_deaths = data.get('two_four_projectile_final_deaths_bedwars', 0)
        FoF_final_fall_deaths = data.get('two_four_fall_final_deaths_bedwars', 0)
        FoF_final_explosion_deaths = data.get('two_four_fire_tick_final_deaths_bedwars', 0)
        FoF_final_magic_deaths = data.get('two_four_magic_final_deaths_bedwars', 0)
        FoF_final_suffocation_deaths = data.get('two_four_suffocation_final_deaths_bedwars', 0)

        FoF_fkdr = FoF_final_kills / FoF_final_deaths

        FoF_kills = data.get('two_four_kills_bedwars', 0)
        FoF_void_kills = data.get('two_four_void_kills_bedwars', 0)
        FoF_projectile_kills = data.get('two_four_projectile_kills_bedwars', 0)
        FoF_fall_kills = data.get('two_four_fall_kills_bedwars', 0)
        FoF_explosion_kills = data.get('two_four_fire_tick_kills_bedwars', 0)
        FoF_magic_kills = data.get('two_four_magic_kills_bedwars', 0)
        FoF_suffocation_kills = data.get('two_four_suffocation_kills_bedwars', 0)

        FoF_deaths = data.get('two_four_deaths_bedwars', 0)
        FoF_void_deaths = data.get('two_four_void_deaths_bedwars', 0)
        FoF_projectile_deaths = data.get('two_four_projectile_deaths_bedwars', 0)
        FoF_fall_deaths = data.get('two_four_fall_deaths_bedwars', 0)
        FoF_explosion_deaths = data.get('two_four_fire_tick_deaths_bedwars', 0)
        FoF_magic_deaths = data.get('two_four_magic_deaths_bedwars', 0)
        FoF_suffocation_deaths = data.get('two_four_suffocation_deaths_bedwars', 0)

        FoF_kdr = FoF_kills / FoF_deaths

        FoF_games_played = data.get('two_four_games_played_bedwars', 0)
        FoF_wins = data.get('two_four_wins_bedwars', 0)
        FoF_losses = data.get('two_four_losses_bedwars', 0)
        FoF_wlr = FoF_wins / FoF_losses

        FoF_iron = data.get('two_four_iron_resources_collected_bedwars', 0)
        FoF_gold = data.get('two_four_gold_resources_collected_bedwars', 0)
        FoF_diamonds = data.get('two_four_diamond_resources_collected_bedwars', 0)
        FoF_emeralds = data.get('two_four_emerald_resources_collected_bedwars', 0)
        FoF_total_resources = FoF_iron + FoF_gold + FoF_diamonds + FoF_emeralds

        FoF_purchases = data.get('two_four_items_purchased_bedwars', 0)
        FoF_permanent_purchases = data.get('two_four_permanent _items_purchased_bedwars', 0)

        FoF_stats = [my_date, FoF_final_kills, FoF_final_void_kills,
                      FoF_final_projectile_kills, FoF_final_fall_kills,
                      FoF_final_explosion_kills, FoF_final_magic_kills,
                      FoF_final_suffocation_kills, FoF_final_deaths,
                      FoF_final_void_deaths, FoF_final_projectile_deaths,
                      FoF_final_fall_deaths, FoF_final_explosion_deaths,
                      FoF_final_magic_deaths, FoF_final_suffocation_deaths,
                      FoF_fkdr, FoF_kills, FoF_void_kills,
                      FoF_projectile_kills, FoF_fall_kills, FoF_explosion_kills,
                      FoF_magic_kills, FoF_suffocation_kills, FoF_deaths,
                      FoF_void_deaths, FoF_projectile_deaths, FoF_fall_deaths,
                      FoF_explosion_deaths, FoF_magic_deaths, FoF_suffocation_deaths,
                      FoF_kdr, FoF_games_played, FoF_wins, FoF_losses, FoF_wlr,
                      FoF_iron, FoF_gold, FoF_diamonds, FoF_emeralds,
                      FoF_total_resources, FoF_purchases, FoF_permanent_purchases]

        handlers.save_FoF(uuid, FoF_stats)










