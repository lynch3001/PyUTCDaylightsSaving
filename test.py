#!/usr/bin/env python
from datetime import datetime
import pytz # $ pip install pytz

year = int(input("What is year you want to check? "))
month = int(input("What is month you want to check? "))
day = int(input("What is day you want to check? "))

def is_summer_time(aware_dt):
    assert aware_dt.tzinfo is not None
    assert aware_dt.tzinfo.utcoffset(aware_dt) is not None
    return bool(aware_dt.dst())

naive = datetime(year, month, day)
pacific = pytz.timezone('America/Los_Angeles')
aware = pacific.localize(naive, is_dst=None) 


if (is_summer_time(aware)):
    result = ("Daylight savings time is in effect for this day")
    end = ("07:00 UTC")
else:
    result = ("Daylight savings time is not in effect for this day")
    end = ("08:00 UTC")

print("%s %s %s" % (result, naive, end))
wait = input("PRESS ENTER TO CONTINUE.")
