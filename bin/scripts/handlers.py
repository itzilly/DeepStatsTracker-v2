from openpyxl import Workbook
from bin.scripts import getLogger


def create_workbook(uuid, player_name):
    path = 'bin/PlayerData/' + uuid + '.xlsx'
    getLogger.info(f"Creating workbook for {player_name}: {path}")

    workbook = Workbook()

    sheet = workbook.active

    overall_sheet = workbook.create_sheet("Bedwars Overall")
    overall_sheet.title = "Bedwars Overall"
    overall_sheet = workbook.get_sheet_by_name("Bedwars Overall")
    overall_titles = ['Date', 'Stars', 'Experience', 'Final Kills', 'Final Deaths', 'FKDR', 'Kills', 'Deaths', 'KDR',
                        'Beds Broken', 'Beds Lost', 'BBLR', 'Games Played', 'Wins', 'Losses', 'WLR', 'Coins', 'Loot Boxes',
                        'Iron Collected', 'Gold Collected', 'Diamonds Collected', 'Emeralds Collected']
    overall_sheet.append(overall_titles)

    specific_titles = ['Date', 'Stars', 'Final Kills', 'Final Deaths', 'FKDR',
                    'Kills', 'Deaths', 'KDR', 'Beds Broken', 'Beds Lost', 'BBLR',
                    'Games Played', 'Wins', 'Losses', 'WLR',
                    'Iron Collected', 'Gold Collected', 'Diamonds Collected', 'Emeralds Collected']

    solo_sheet = workbook.create_sheet("Bedwars Solos")
    solo_sheet.title = "Bedwars Solos"
    solo_sheet = workbook.get_sheet_by_name("Bedwars Solos")
    solo_sheet.append(specific_titles)

    duo_sheet = workbook.create_sheet("Bedwars Duos")
    duo_sheet.title = "Bedwars Duos"
    duo_sheet = workbook.get_sheet_by_name("Bedwars Duos")
    duo_sheet.append(specific_titles)

    threes_sheet = workbook.create_sheet("Bedwars Threes")
    threes_sheet.title = "Bedwars Threes"
    threes_sheet = workbook.get_sheet_by_name("Bedwars Threes")
    threes_sheet.append(specific_titles)

    fours_sheet = workbook.create_sheet("Bedwars Fours")
    fours_sheet.title = "Bedwars Fours"
    fours_sheet = workbook.get_sheet_by_name("Bedwars Fours")
    fours_sheet.append(specific_titles)

    FoF_sheet = workbook.create_sheet("Bedwars FoF")
    FoF_sheet.title = "Bedwars FoF"
    FoF_sheet = workbook.get_sheet_by_name("Bedwars FoF")
    FoF_sheet.append(specific_titles)

    workbook.save(path)
    getLogger.info(f"Created and saved workbook for {player_name}: \'{uuid}\'")
