import time
'''
The time module provides a function, also named time, that returns the current
Greenwich Mean Time in “the epoch”, which is an arbitrary time used as a reference
point. On UNIX systems, the epoch is 1 January 1970.
1437746094.5735958
Write a script that reads the current time and converts it to a time of day in hours,
minutes, and seconds, plus the number of days since the epoch.
'''


t = time.time()
print(t)


def convert(tm):

    days = tm/365
    hours = tm/60
    minutes = tm/60*60
    seconds = tm/3600*60
    print("days:", days, "Hours:", hours, "Minutes:", minutes, "Seconds:", seconds)


convert(t)
