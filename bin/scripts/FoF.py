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
    final_kills = data.get('two_four_final_kills_bedwars', 0)
    final_void_kills = data.get('two_four_void_final_kills_bedwars', 0)
    final_kills_non_void = data.get('two_four_final_kills_bedwars', 0) - data.get('two_four_void_final_kills_bedwars', 0)
    final_projectile_kills = data.get('two_four_projectile_final_kills_bedwars', 0)
    final_fall_kills = data.get('two_four_fall_final_kills_bedwars', 0)
    final_explosion_kills = data.get('two_four_fire_tick_final_kills_bedwars', 0)
    final_magic_kills = data.get('two_four_magic_final_kills_bedwars', 0)
    final_suffocation_kills = data.get('two_four_suffocation_final_kills_bedwars', 0)
    final_deaths = data.get('two_four_final_deaths_bedwars', 0)
    final_void_deaths = data.get('two_four_void_final_deaths_bedwars', 0)
    final_deaths_non_void = data.get('two_four_final_deaths_bedwars', 0) - data.get('two_four_void_final_deaths_bedwars', 0)
    final_projectile_deaths = data.get('two_four_projectile_final_deaths_bedwars', 0)
    final_fall_deaths = data.get('two_four_fall_final_deaths_bedwars', 0)
    final_explosion_deaths = data.get('two_four_fire_tick_final_deaths_bedwars', 0)
    final_magic_deaths = data.get('two_four_magic_final_deaths_bedwars', 0)
    final_suffocation_deaths = data.get('two_four_suffocation_final_deaths_bedwars', 0)
    kills = data.get('two_four_kills_bedwars', 0)
    void_kills = data.get('two_four_void_kills_bedwars', 0)
    kills_non_void = data.get('two_four_kills_bedwars', 0) - data.get('two_four_void_kills_bedwars', 0)
    projectile_kills = data.get('two_four_projectile_kills_bedwars', 0)
    fall_kills = data.get('two_four_fall_kills_bedwars', 0)
    explosion_kills = data.get('two_four_fire_tick_kills_bedwars', 0)
    magic_kills = data.get('two_four_magic_kills_bedwars', 0)
    suffocation_kills = data.get('two_four_suffocation_kills_bedwars', 0)
    deaths = data.get('two_four_deaths_bedwars', 0)
    void_deaths = data.get('two_four_void_deaths_bedwars', 0)
    deaths_non_void = data.get('two_four_deaths_bedwars', 0) - data.get('two_four_void_deaths_bedwars', 0)
    projectile_deaths = data.get('two_four_projectile_deaths_bedwars', 0)
    fall_deaths = data.get('two_four_fall_deaths_bedwars', 0)
    explosion_deaths = data.get('two_four_fire_tick_deaths_bedwars', 0)
    magic_deaths = data.get('two_four_magic_deaths_bedwars', 0)
    suffocation_deaths = data.get('two_four_suffocation_deaths_bedwars', 0)

    fkdr = data.get('two_four_final_kills_bedwars', 0) / data.get('two_four_final_deaths_bedwars', 1)
    kdr = data.get('two_four_kills_bedwars', 0) / data.get('two_four_deaths_bedwars', 1)

    # # # Game, Resources, and purchases Count
    games_played = data.get('two_four_games_played_bedwars', 0)
    wins = data.get('two_four_wins_bedwars', 0)
    losses = data.get('two_four_losses_bedwars', 0)
    iron = data.get('two_four_iron_resources_collected_bedwars', 0)
    gold = data.get('two_four_gold_resources_collected_bedwars', 0)
    diamonds = data.get('two_four_diamond_resources_collected_bedwars', 0)
    emeralds = data.get('two_four_emerald_resources_collected_bedwars', 0)
    total_resources = data.get('two_four_iron_resources_collected_bedwars', 0) + data.get(
        'two_four_gold_resources_collected_bedwars', 0) + data.get('two_four_diamond_resources_collected_bedwars',
                                                                    0) + data.get(
        'two_four_emerald_resources_collected_bedwars', 0)
    iron_per_game = data.get('two_four_iron_resources_collected_bedwars', 0) / data.get(
        'two_four_games_played_bedwars', 1)
    gold_per_game = data.get('two_four_gold_resources_collected_bedwars', 0) / data.get(
        'two_four_games_played_bedwars', 1)
    diamonds_per_game = data.get('two_four_diamond_resources_collected_bedwars', 0) / data.get(
        'two_four_games_played_bedwars', 1)
    emeralds_per_game = data.get('two_four_emerald_resources_collected_bedwars', 0) / data.get(
        'two_four_games_played_bedwars', 1)
    total_resources_per_game = (data.get('two_four_iron_resources_collected_bedwars', 0) + data.get(
        'two_four_gold_resources_collected_bedwars', 0) + data.get('two_four_diamond_resources_collected_bedwars',
                                                                    0) + data.get(
        'two_four_emerald_resources_collected_bedwars', 0)) / data.get('two_four_games_played_bedwars', 1)

    purchases = data.get('two_four_items_purchased_bedwars', 0)
    permanent_purchases = data.get('two_four_permanent _items_purchased_bedwars', 0)

    # # # Beds
    beds_broken = data.get('two_four_beds_lost_bedwars', 0)
    beds_lost = data.get('two_four_beds_broken_bedwars', 0)
    bblr = data.get('two_four_beds_lost_bedwars', 0) / data.get('two_four_beds_broken_bedwars', 1)
    beds_broken_per_game = data.get('two_four_beds_broken_bedwars', 0) / data.get('two_four_games_played_bedwars', 1)

    # # # This array is what is passed to the logger script
    # # # It contains all the values you've chosen to log
    FoF_stats = [
        date,
        stars,
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

    handlers.save_FoF(uuid, FoF_stats)
