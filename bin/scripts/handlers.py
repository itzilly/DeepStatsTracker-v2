from openpyxl import Workbook, load_workbook
from bin.scripts import getLogger


def create_workbook(uuid, player_name):
    path = 'bin/PlayerData/' + uuid + '.xlsx'
    getLogger.info(f"Creating workbook for {player_name}: {path}")
    individual_titles = [
        'Date', 'Stars', 'Experience', 'Coins',
        # 'Loot Boxes',
        'Final Kills', 'Final Void Kills', 'Final Kills Non Void', 'Final Projectile Kills',
        'Final Fall Kills', 'Final Explosion Kills', 'Final Magic Kills', 'Final Suffocation Kills',
        'Final Deaths', 'Final Void Deaths', 'Final Deaths Non World', 'Final Projectile Deaths',
        'Final Fall Deaths', 'Final Explosions Deaths', 'Final Magic Deaths', 'Final Suffocation Deaths',
        'Kills', 'Void Kills', 'Kills Non Void', 'Projectile Kills', 'Fall Kills', 'Explosion Kills',
        'Magic Kills', 'Suffocation Kills', 'deaths', 'Void Deaths', 'Deaths Non Void', 'Projectile Deaths',
        'Fall Deaths', 'Explosion Deaths', 'Magic Deaths', 'Suffocation Deaths', 'FKDR', 'KDR', 'Games Played',
        'Wins', 'Losses', 'Iron', 'Gold', 'Diamonds', 'Emeralds', 'Total Resources', 'Iron Per Game', 'Gold Per Game',
        'Diamonds Per Game', 'Emeralds Per Game', 'Total Resources Per Game', 'Purchases', 'Permanent Purchases',
        'Beds Broken', 'Beds Lost', 'BBLR', 'Beds Broken Per Game'
    ]

    workbook = Workbook()

    sheet = workbook.active

    overall_sheet = workbook.create_sheet("Bedwars Overall")
    overall_sheet.title = "Bedwars Overall"
    overall_sheet = workbook.get_sheet_by_name("Bedwars Overall")
    overall_sheet.append(individual_titles)

    solo_sheet = workbook.create_sheet("Bedwars Solos")
    solo_sheet.title = "Bedwars Solos"
    solo_sheet = workbook.get_sheet_by_name("Bedwars Solos")

    normals_titles = [
        'Date', 'Stars', 'Final Kills', 'Final Void Kills', 'Final Kills Non Void', 'Final Projectile Kills',
        'Final Fall Kills', 'Final Explosion Kills', 'Final Magic Kills', 'Final Suffocation Kills',
        'Final Deaths', 'Final Void Deaths', 'Final Deaths Non World', 'Final Projectile Deaths',
        'Final Fall Deaths', 'Final Explosions Deaths', 'Final Magic Deaths', 'Final Suffocation Deaths',
        'Kills', 'Void Kills', 'Kills Non Void', 'Projectile Kills', 'Fall Kills', 'Explosion Kills',
        'Magic Kills', 'Suffocation Kills', 'deaths', 'Void Deaths', 'Deaths Non Void', 'Projectile Deaths',
        'Fall Deaths', 'Explosion Deaths', 'Magic Deaths', 'Suffocation Deaths', 'FKDR', 'KDR', 'Games Played',
        'Wins', 'Losses', 'Iron', 'Gold', 'Diamonds', 'Emeralds', 'Total Resources', 'Iron Per Game', 'Gold Per Game',
        'Diamonds Per Game', 'Emeralds Per Game', 'Total Resources Per Game', 'Purchases', 'Permanent Purchases',
        'Beds Broken', 'Beds Lost', 'BBLR', 'Beds Broken Per Game'
    ]

    solo_sheet.append(normals_titles)

    duo_sheet = workbook.create_sheet("Bedwars Duos")
    duo_sheet.title = "Bedwars Duos"
    duo_sheet = workbook.get_sheet_by_name("Bedwars Duos")
    duo_sheet.append(normals_titles)

    threes_sheet = workbook.create_sheet("Bedwars Threes")
    threes_sheet.title = "Bedwars Threes"
    threes_sheet = workbook.get_sheet_by_name("Bedwars Threes")
    threes_sheet.append(normals_titles)

    fours_sheet = workbook.create_sheet("Bedwars Fours")
    fours_sheet.title = "Bedwars Fours"
    fours_sheet = workbook.get_sheet_by_name("Bedwars Fours")
    fours_sheet.append(normals_titles)
    
    FoF_sheet = workbook.create_sheet("Bedwars FoF")
    FoF_sheet.title = "Bedwars FoF"
    FoF_sheet = workbook.get_sheet_by_name("Bedwars FoF")
    FoF_sheet.append(normals_titles)

    duo_ult_sheet = workbook.create_sheet("Bedwars Duos Ultimates")
    duo_ult_sheet.title = "Bedwars Duos Ultimates"
    duo_ult_sheet = workbook.get_sheet_by_name("Bedwars Duos Ultimates")
    duo_ult_sheet.append(normals_titles)

    four_ult_sheet = workbook.create_sheet("Bedwars Fours Ultimates")
    four_ult_sheet.title = "Bedwars Fours Ultimates"
    four_ult_sheet = workbook.get_sheet_by_name("Bedwars Fours Ultimates")
    four_ult_sheet.append(normals_titles)
    
    duo_rush_sheet = workbook.create_sheet("Bedwars Duos Rush")
    duo_rush_sheet.title = "Bedwars Duos Rush"
    duo_rush_sheet = workbook.get_sheet_by_name("Bedwars Duos Rush")
    duo_rush_sheet.append(normals_titles)

    four_rush_sheet = workbook.create_sheet("Bedwars Fours rushimates")
    four_rush_sheet.title = "Bedwars Fours rushimates"
    four_rush_sheet = workbook.get_sheet_by_name("Bedwars Fours rushimates")
    four_rush_sheet.append(normals_titles)
    
    duo_no_void_sheet = workbook.create_sheet("Bedwars Duos Voidless")
    duo_no_void_sheet.title = "Bedwars Duos Voidless"
    duo_no_void_sheet = workbook.get_sheet_by_name("Bedwars Duos Voidless")
    duo_no_void_sheet.append(normals_titles)

    four_no_void_sheet = workbook.create_sheet("Bedwars Fours Voidless")
    four_no_void_sheet.title = "Bedwars Fours Voidless"
    four_no_void_sheet = workbook.get_sheet_by_name("Bedwars Fours Voidless")
    four_no_void_sheet.append(normals_titles)
    
    duo_armed_sheet = workbook.create_sheet("Bedwars Duos Armed")
    duo_armed_sheet.title = "Bedwars Duos Armed"
    duo_armed_sheet = workbook.get_sheet_by_name("Bedwars Duos Armed")
    duo_armed_sheet.append(normals_titles)

    four_armed_sheet = workbook.create_sheet("Bedwars Fours Armed")
    four_armed_sheet.title = "Bedwars Fours Armed"
    four_armed_sheet = workbook.get_sheet_by_name("Bedwars Fours Armed")
    four_armed_sheet.append(normals_titles)
    
    duo_luck_sheet = workbook.create_sheet("Bedwars Duos Lucky")
    duo_luck_sheet.title = "Bedwars Duos Lucky"
    duo_luck_sheet = workbook.get_sheet_by_name("Bedwars Duos Lucky")
    duo_luck_sheet.append(normals_titles)

    four_luck_sheet = workbook.create_sheet("Bedwars Fours Lucky")
    four_luck_sheet.title = "Bedwars Fours Lucky"
    four_luck_sheet = workbook.get_sheet_by_name("Bedwars Fours Lucky")
    four_luck_sheet.append(normals_titles)
    
    castle_sheet = workbook.create_sheet("Bedwars Castle")
    castle_sheet.title = "Bedwars Castle"
    castle_sheet = workbook.get_sheet_by_name("Bedwars Castle")
    castle_sheet.append(normals_titles)

    workbook.remove_sheet(sheet)
    workbook.save(path)

    getLogger.info(f"Created and saved workbook for {player_name}: \'{uuid}\'")


def save_overall(uuid, stats):
    path = 'bin/playerData/' + uuid + '.xlsx'
    workbook = load_workbook(path)
    overall_sheet = workbook["Bedwars Overall"]
    overall_sheet.append(stats)
    workbook.save(path)

    getLogger.info("Saving player data to " + path + " BEDWARS OVERALL")


def save_solos(uuid, solo_stats):
    path = 'bin/playerData/' + uuid + '.xlsx'
    workbook = load_workbook(path)
    solos_sheet = workbook["Bedwars Solos"]
    solos_sheet.append(solo_stats)
    workbook.save(path)

    getLogger.info("Saving player data to " + path + " BEDWARS SOLOS")


def save_duos(uuid, stats):
    path = 'bin/playerData/' + uuid + '.xlsx'
    workbook = load_workbook(path)
    solos_sheet = workbook["Bedwars Duos"]
    solos_sheet.append(stats)
    workbook.save(path)

    getLogger.info("Saving player data to " + path + " BEDWARS DUOS")


def save_threes(uuid, stats):
    path = 'bin/playerData/' + uuid + '.xlsx'
    workbook = load_workbook(path)
    solos_sheet = workbook["Bedwars Threes"]
    solos_sheet.append(stats)
    workbook.save(path)

    getLogger.info("Saving player data to " + path + " BEDWARS SOLOS")


def save_fours(uuid, stats):
    path = 'bin/playerData/' + uuid + '.xlsx'
    workbook = load_workbook(path)
    solos_sheet = workbook["Bedwars Fours"]
    solos_sheet.append(stats)
    workbook.save(path)

    getLogger.info("Saving player data to " + path + " BEDWARS Fours")


def save_FoF(uuid, stats):
    path = 'bin/playerData/' + uuid + '.xlsx'
    workbook = load_workbook(path)
    solos_sheet = workbook["Bedwars FoF"]
    solos_sheet.append(stats)
    workbook.save(path)

    getLogger.info("Saving player data to " + path + " BEDWARS FoF")


def save_duo_ult(uuid, stats):
    path = 'bin/playerData/' + uuid + '.xlsx'
    workbook = load_workbook(path)
    solos_sheet = workbook["Bedwars Duos Ultimates"]
    solos_sheet.append(stats)
    workbook.save(path)

    getLogger.info("Saving player data to " + path + " BEDWARS Duos Ultimates")


def save_four_ult(uuid, stats):
    path = 'bin/playerData/' + uuid + '.xlsx'
    workbook = load_workbook(path)
    solos_sheet = workbook["Bedwars Fours Ultimates"]
    solos_sheet.append(stats)
    workbook.save(path)

    getLogger.info("Saving player data to " + path + " BEDWARS Fours Ultimates")
