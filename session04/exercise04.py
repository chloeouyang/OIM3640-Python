# 3.
# import datetime
# movingtime= (8*60+15)*2+(7*60+12)*3
# t=datetime.datetime(2021,9,8,6,52)
# print (t)
# h=movingtime//60
# m=movingtime%60
# print (h)
# print (m)
# print (t+datetime.timedelta(hours=h,minutes=m))

# newt=t+datetime.timedelta(hours=h,minutes=m)
# print(newt.time())

# # 4.
# percentageinnumber=(89-82)/82
# percentage=percentageinnumber*100
# print(f'{percentage:.1f}%')

import time
from typing import Mapping
print(time.time())
print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))
#or
sec_epoch=time.time()
min_epoch=sec_epoch//60
sec=sec_epoch%60+sec_epoch
hour_epoch=min_epoch//60
min=min_epoch%60+min_epoch
day_epoch=hour_epoch//24
hour=hour_epoch%24+hour_epoch
import datetime
t=datetime.datetime(1970,1,1,0,0)
print (t+datetime.timedelta(days=day_epoch,hours=hour,minutes=min,seconds=sec))