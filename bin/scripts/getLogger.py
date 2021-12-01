from bin.scripts.utilz import time, date

logger = 'bin/logger.txt'


def info(data):
    print(f"[INFO] {data}")
    with open(logger, 'a') as log:
        log.write(f" [ INFO ] " + date() + " " + time() + " : " + data + "\n")
        log.close()


def warn(data):
    print(f"[WARNING] {data}")
    with open(logger, 'a') as log:
        log.write(f" [ WARNING ] " + date() + " " + time() + " : " + data + "\n")
        log.close()


def severe(data):
    print(f"[ERROR] {data}")
    with open(logger, 'a') as log:
        log.write(f" [ ERROR ] " + date() + " " + time() + " : " + data + "\n")
        log.close()


def new_instance():
    with open(logger, 'a') as log:
        log.write('\n')
        log.close()
