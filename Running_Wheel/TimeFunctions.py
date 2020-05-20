import datetime
import time

def GetDate():
    now=datetime.datetime.now()
    date = now.strftime("%m_%d_%Y")
    seconds_since_midnight = (now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()
    timepoint = str(date) + ' ' + str(seconds_since_midnight)

    return date,timepoint

def now():
    now = time.time()
    return now

def clock():
    clock = time.strftime("%H:%M:%S", time.localtime())
    print(clock)
    