import time
from datetime import datetime, timedelta

dt1 = datetime(2020, 1, 14)
dt2 = datetime.now()
dt = datetime.strptime("2022/1/14", "%Y/%m/%d")
dt = datetime.fromtimestamp(time.time())
print(f"Date: {dt.day}/{dt.month}/{dt.year} \nTime: {dt.time()}")

duration = dt2 - dt1
print(duration)
print(f"Days: {duration.days} Seconds: {duration.seconds} Total seconds: {duration.total_seconds()}")

