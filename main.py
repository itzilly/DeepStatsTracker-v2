from json import JSONDecodeError

from bin.scripts import getLogger
from bin.scripts import utilz


utilz.check_tracking_list()
targets = 'bin/tracking-list.txt'


def get_tracker_list():
    track = open(targets, "r")
    content = track.read()
    content_list = content.split(", ")
    track.close()
    return content_list


getLogger.new_instance()
utilz.check_api_key()
utilz.check_data_folder()

tracking = get_tracker_list()
getLogger.info(f"Reading {targets} for list of targets, found {tracking}")
length = len(tracking)
i = 0
while i < length:
    getLogger.info(f"Registered {tracking[i]}")
    try:
        utilz.identity_theft(tracking[i])
        i += 1
    except JSONDecodeError as error:
        getLogger.severe(f"Error reading player's from {targets}, please ensure you have properly formatted the "
                         f"target list!")
        getLogger.severe(error)
        getLogger.severe(f"{tracking[i]} is a malformed UUID! Please enter a valid username")
        exit()

getLogger.done()

