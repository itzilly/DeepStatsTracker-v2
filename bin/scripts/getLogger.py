from bin.scripts import utilz

logger = 'bin/logger.txt'
mytime = str(utilz.time)
mydate = str(utilz.date)

def info(data):
    print(data)
    with open(logger, 'a') as log:
        log.write("[ INFO ] " + mydate + " " + mytime + " : " + data + "\n")
        log.close()


def warn(data):
    print(data)
    with open(logger, 'a') as log:
        log.write(" [WARNING ] " + mydate + " " + mytime + " : " + data + "\n")
        log.close()


def severe(data):
    print(data)
    with open(logger, 'a') as log:
        log.write("[ ERROR ] " + mydate + " " + mytime + " : " + data + "\n")
        log.close()


def new_instance():
    with open(logger, 'a') as log:
        log.write('\n')
        log.close()
