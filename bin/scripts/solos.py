from bin.scripts import handlers
from bin.scripts import utilz


def save(data, uuid, star):
    data = data
    date = utilz.date()
    stars = star

# # # # # # # # # # # # #
    # Stats to log:
# # # # # # # # # # # # #

# # # Kills and Deaths
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
    solos_non_void_final_deaths = solos_final_deaths - solos_final_void_deaths
    solos_non_void_final_kills = solos_final_kills - solos_final_void_kills
    solos_non_void_deaths = solos_deaths - solos_void_deaths
    solos_non_void_kills = solos_kills - solos_void_kills


# # # Game, Resources, and purchases Count
    solos_games_played = data.get('eight_one_games_played_bedwars', 0)
    solos_wins = data.get('eight_one_wins_bedwars', 0)
    solos_losses = data.get('eight_one_losses_bedwars', 0)
    solos_iron = data.get('eight_one_iron_resources_collected_bedwars', 0)
    solos_gold = data.get('eight_one_gold_resources_collected_bedwars', 0)
    solos_diamonds = data.get('eight_one_diamond_resources_collected_bedwars', 0)
    solos_emeralds = data.get('eight_one_emerald_resources_collected_bedwars', 0)
    solos_total_resources = solos_iron + solos_gold + solos_diamonds + solos_emeralds
    solos_purchases = data.get('eight_one_items_purchased_bedwars', 0)
    solos_permanent_purchases = data.get('eight_one_permanent _items_purchased_bedwars', 0)

    # # # Beds
    solos_beds_broken = data.get('eight_one_beds_lost_bedwars')
    solos_beds_lost = data.get('eight_one_beds_broken_bedwars')


# # # Per-Game Stats
    try:
        solos_fkdr = solos_final_kills / solos_final_deaths
    except ZeroDivisionError:
        solos_fkdr = solos_final_kills
    try:
        solos_kdr = solos_kills / solos_deaths
    except ZeroDivisionError:
        solos_kdr = solos_kills
    try:
        solos_wlr = solos_wins / solos_losses
    except ZeroDivisionError:
        solos_wlr = solos_wins
    try:
        solos_final_kills_per_star = solos_final_kills / stars
    except ZeroDivisionError:
        solos_final_kills_per_star = solos_final_kills
    try:
        solos_kills_per_star = solos_kills / stars
    except ZeroDivisionError:
        solos_kills_per_star = solos_kills
    try:
        solos_final_deaths_per_star = solos_final_kills / stars
    except ZeroDivisionError:
        solos_final_deaths_per_star = solos_final_kills
    try:
        solos_deaths_per_star = solos_kills / stars
    except ZeroDivisionError:
        solos_deaths_per_star = solos_kills
    try:
        solos_average_resources = solos_total_resources / solos_games_played
    except ZeroDivisionError:
        solos_average_resources = solos_total_resources
    try:
        solos_average_iron = solos_iron / solos_games_played
    except ZeroDivisionError:
        solos_average_iron = solos_iron
    try:
        solos_average_gold = solos_gold / solos_games_played
    except ZeroDivisionError:
        solos_average_gold = solos_gold
    try:
        solos_average_diamonds = solos_diamonds / solos_games_played
    except ZeroDivisionError:
        solos_average_diamonds = solos_diamonds
    try:
        solos_average_emeralds = solos_emeralds / solos_games_played
    except ZeroDivisionError:
        solos_average_emeralds = solos_emeralds
    try:
        solos_bblr = solos_beds_broken / solos_beds_lost
    except ZeroDivisionError:
        solos_bblr = solos_beds_broken
    try:
        solos_beds_broken_per_games_played = solos_beds_broken / solos_games_played
    except ZeroDivisionError:
        solos_beds_broken_per_games_played = solos_beds_broken
    try:
        solos_beds_lost_per_games_played = solos_beds_lost / solos_games_played
    except ZeroDivisionError:
        solos_beds_lost_per_games_played = solos_beds_lost
    try:
        solos_kills_per_game = solos_kills / solos_games_played
    except ZeroDivisionError:
        solos_kills_per_game = solos_kills
    try:
        solos_non_void_kills_per_game = solos_non_void_kills / solos_games_played
    except ZeroDivisionError:
        solos_non_void_kills_per_game = solos_non_void_kills
    try:
        solos_non_void_deaths_per_game = solos_non_void_deaths / solos_games_played
    except ZeroDivisionError:
        solos_non_void_deaths_per_game = solos_non_void_deaths
    try:
        solos_non_void_final_kills_per_game = solos_non_void_final_kills / solos_games_played
    except ZeroDivisionError:
        solos_non_void_final_kills_per_game = solos_non_void_final_kills
    try:
        solos_non_void_final_deaths_per_game = solos_non_void_final_deaths / solos_games_played
    except ZeroDivisionError:
        solos_non_void_final_deaths_per_game = solos_non_void_final_deaths
    try:
        solos_deaths_per_game = solos_deaths / solos_games_played
    except ZeroDivisionError:
        solos_deaths_per_game = solos_deaths
    try:
        solos_final_kills_per_game = solos_final_kills / solos_games_played
    except ZeroDivisionError:
        solos_final_kills_per_game = solos_final_kills
    try:
        solos_final_deaths_per_game = solos_final_deaths / solos_games_played
    except ZeroDivisionError:
        solos_final_deaths_per_game = solos_final_deaths
    try:
        solos_purchases_per_game = solos_purchases / solos_games_played
    except ZeroDivisionError:
        solos_purchases_per_game = solos_purchases
    try:
        solo_permanent_purchases_per_game = solos_permanent_purchases / solos_games_played
    except ZeroDivisionError:
        solos_permanent_purchases_per_game = solos_permanent_purchases


# # # This array is what is passed to the logger script
# # # It contains all the values you've chosen to log

    solo_stats = [
        stars,
        solos_final_kills_per_star,
        solos_final_deaths_per_star,
        solos_kills_per_star,
        solos_deaths_per_star,

        solos_fkdr,
        solos_kdr,
        solos_games_played,
        solos_wins,
        solos_losses,
        solos_wlr,


        solos_final_kills,
        solos_final_void_kills,
        solos_non_void_final_kills,
        solos_final_projectile_kills,
        solos_final_fall_kills,
        solos_final_explosion_kills,
        solos_final_magic_kills,
        solos_final_suffocation_kills,
        solos_final_kills_per_game,
        solos_non_void_final_kills_per_game,

        solos_final_deaths,
        solos_final_void_deaths,
        solos_non_void_final_deaths,
        solos_final_projectile_deaths,
        solos_final_fall_deaths,
        solos_final_explosion_deaths,
        solos_final_magic_deaths,
        solos_final_suffocation_deaths,
        solos_final_deaths_per_game,
        solos_non_void_final_deaths_per_game,

        solos_kills,
        solos_void_kills,
        solos_non_void_kills,
        solos_projectile_kills,
        solos_fall_kills,
        solos_explosion_kills,
        solos_magic_kills,
        solos_suffocation_kills,
        solos_kills_per_game,
        solos_non_void_kills_per_game,

        solos_deaths,
        solos_void_deaths,
        solos_non_void_deaths,
        solos_projectile_deaths,
        solos_fall_deaths,
        solos_explosion_deaths,
        solos_magic_deaths,
        solos_suffocation_deaths,
        solos_deaths_per_game,
        solos_non_void_deaths_per_game,

        solos_games_played,
        solos_wins,
        solos_losses,
        solos_iron,
        solos_gold,
        solos_diamonds,
        solos_emeralds,
        solos_total_resources,
        solos_purchases,
        solos_permanent_purchases,



    ]

    handlers.save_solos(uuid, solo_stats)








