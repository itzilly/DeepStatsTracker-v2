from bin.scripts import handlers
from bin.scripts import utilz


def save(data, uuid, star):
    data = data
    date = utilz.date()
    stars = star

    # # # # # # # # # # # # #
    # Stats to log:
    # # # # # # # # # # # # #
#   stars
    experience = data.get('Experience', 0)
    coins = data.get('coins', 0)
#    loot_boxes = data.get('', 0)
    final_kills = data.get('eight_one_final_kills_bedwars', 0)
    final_void_kills = data.get('eight_one_void_final_kills_bedwars', 0)
    final_kills_non_void = data.get('eight_one_final_kills_bedwars', 0) - data.get('eight_one_void_final_kills_bedwars', 0)
    final_projectile_kills = data.get('eight_one_projectile_final_kills_bedwars', 0)
    final_fall_kills = data.get('eight_one_fall_final_kills_bedwars', 0)
    final_explosion_kills = data.get('eight_one_fire_tick_final_kills_bedwars', 0)
    final_magic_kills = data.get('eight_one_magic_final_kills_bedwars', 0)
    final_suffocation_kills = data.get('eight_one_suffocation_final_kills_bedwars', 0)
    final_deaths = data.get('eight_one_final_deaths_bedwars', 0)
    final_void_deaths = data.get('eight_one_void_final_deaths_bedwars', 0)
    final_deaths_non_void = data.get('eight_one_final_deaths_bedwars', 0) - data.get('eight_one_void_final_deaths_bedwars', 0)
    final_projectile_deaths = data.get('eight_one_projectile_final_deaths_bedwars', 0)
    final_fall_deaths = data.get('eight_one_fall_final_deaths_bedwars', 0)
    final_explosion_deaths = data.get('eight_one_fire_tick_final_deaths_bedwars', 0)
    final_magic_deaths = data.get('eight_one_magic_final_deaths_bedwars', 0)
    final_suffocation_deaths = data.get('eight_one_suffocation_final_deaths_bedwars', 0)
    kills = data.get('eight_one_kills_bedwars', 0)
    void_kills = data.get('eight_one_void_kills_bedwars', 0)
    kills_non_void = data.get('eight_one_kills_bedwars', 0) - data.get('eight_one_void_kills_bedwars', 0)
    projectile_kills = data.get('eight_one_projectile_kills_bedwars', 0)
    fall_kills = data.get('eight_one_fall_kills_bedwars', 0)
    explosion_kills = data.get('eight_one_fire_tick_kills_bedwars', 0)
    magic_kills = data.get('eight_one_magic_kills_bedwars', 0)
    suffocation_kills = data.get('eight_one_suffocation_kills_bedwars', 0)
    deaths = data.get('eight_one_deaths_bedwars', 0)
    void_deaths = data.get('eight_one_void_deaths_bedwars', 0)
    deaths_non_void = data.get('eight_one_deaths_bedwars', 0) - data.get('eight_one_void_deaths_bedwars', 0)
    projectile_deaths = data.get('eight_one_projectile_deaths_bedwars', 0)
    fall_deaths = data.get('eight_one_fall_deaths_bedwars', 0)
    explosion_deaths = data.get('eight_one_fire_tick_deaths_bedwars', 0)
    magic_deaths = data.get('eight_one_magic_deaths_bedwars', 0)
    suffocation_deaths = data.get('eight_one_suffocation_deaths_bedwars', 0)

    fkdr = data.get('eight_one_final_kills_bedwars', 0) / data.get('eight_one_final_deaths_bedwars', 1)
    kdr = data.get('eight_one_kills_bedwars', 0) / data.get('eight_one_deaths_bedwars', 1)

    # # # Game, Resources, and purchases Count
    games_played = data.get('eight_one_games_played_bedwars', 0)
    wins = data.get('eight_one_wins_bedwars', 0)
    losses = data.get('eight_one_losses_bedwars', 0)
    iron = data.get('eight_one_iron_resources_collected_bedwars', 0)
    gold = data.get('eight_one_gold_resources_collected_bedwars', 0)
    diamonds = data.get('eight_one_diamond_resources_collected_bedwars', 0)
    emeralds = data.get('eight_one_emerald_resources_collected_bedwars', 0)
    total_resources = data.get('eight_one_iron_resources_collected_bedwars', 0) + data.get('eight_one_gold_resources_collected_bedwars', 0) + data.get('eight_one_diamond_resources_collected_bedwars', 0) + data.get('eight_one_emerald_resources_collected_bedwars', 0)
    iron_per_game = data.get('eight_one_iron_resources_collected_bedwars', 0) / data.get('eight_one_games_played_bedwars', 1)
    gold_per_game = data.get('eight_one_gold_resources_collected_bedwars', 0) / data.get('eight_one_games_played_bedwars', 1)
    diamonds_per_game = data.get('eight_one_diamond_resources_collected_bedwars', 0) / data.get('eight_one_games_played_bedwars', 1)
    emeralds_per_game = data.get('eight_one_emerald_resources_collected_bedwars', 0) / data.get('eight_one_games_played_bedwars', 1)
    total_resources_per_game = (data.get('eight_one_iron_resources_collected_bedwars', 0) + data.get('eight_one_gold_resources_collected_bedwars', 0) + data.get('eight_one_diamond_resources_collected_bedwars', 0) + data.get('eight_one_emerald_resources_collected_bedwars', 0)) / data.get('eight_one_games_played_bedwars', 1)

    purchases = data.get('eight_one_items_purchased_bedwars', 0)
    permanent_purchases = data.get('eight_one_permanent _items_purchased_bedwars', 0)

    # # # Beds
    beds_broken = data.get('eight_one_beds_lost_bedwars', 0)
    beds_lost = data.get('eight_one_beds_broken_bedwars', 0)
    bblr = data.get('eight_one_beds_lost_bedwars', 0) / data.get('eight_one_beds_broken_bedwars', 1)
    beds_broken_per_game = data.get('eight_one_beds_broken_bedwars', 0) / data.get('eight_one_games_played_bedwars', 1)

    # # # This array is what is passed to the logger script
    # # # It contains all the values you've chosen to log
    solos_stats = [
        date,
        stars,
        experience,
        coins,
        # loot_boxes,
        final_kills,
        final_void_kills,
        final_kills_non_void,
        final_projectile_kills,
        final_fall_kills,
        final_explosion_kills,
        final_magic_kills,
        final_suffocation_kills,

        final_deaths,
        final_void_deaths,
        final_deaths_non_void,
        final_projectile_deaths,
        final_fall_deaths,
        final_explosion_deaths,
        final_magic_deaths,
        final_suffocation_deaths,

        kills,
        void_kills,
        kills_non_void,
        projectile_kills,
        fall_kills,
        explosion_kills,
        magic_kills,
        suffocation_kills,

        deaths,
        void_deaths,
        deaths_non_void,
        projectile_deaths,
        fall_deaths,
        explosion_deaths,
        magic_deaths,
        suffocation_deaths,

        fkdr,
        kdr,

        games_played,
        wins,
        losses,

        iron,
        gold,
        diamonds,
        emeralds,
        total_resources,
        iron_per_game,
        gold_per_game,
        diamonds_per_game,
        emeralds_per_game,
        total_resources_per_game,
        purchases,
        permanent_purchases,

        beds_broken,
        beds_lost,
        bblr,
        beds_broken_per_game
    ]

    handlers.save_solos(uuid, solos_stats)
