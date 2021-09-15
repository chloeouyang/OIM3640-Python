import time
from typing import Mapping

print(time.time())
print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))
# or
sec_epoch = time.time()
min_epoch = sec_epoch // 60
sec = sec_epoch % 60 + sec_epoch
hour_epoch = min_epoch // 60
min = min_epoch % 60 + min_epoch
day_epoch = hour_epoch // 24
hour = hour_epoch % 24 + hour_epoch
import datetime

t = datetime.datetime(1970, 1, 1, 0, 0)
#print(t + datetime.timedelta(days=day_epoch, hours=hour, minutes=min, seconds=sec))
print(datetime.timedelta(days=day_epoch,hours=hour,minutes=min,seconds=sec))