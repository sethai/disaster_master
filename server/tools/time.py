from datetime import datetime

def timefrommiliseconds(timestamp):
    time = int(timestamp) / 1e3
    time = datetime.fromtimestamp(time)
    time = time.strftime("%H:%M, %m/%d/%Y")
    return time