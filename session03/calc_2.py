# 1.
pi = 3.1415926
# pi = int(pi)
print((4 / 3) * pi * 5 ** 3)
# if int is added, the answer would be 500, which makes pi equal to 3
# when do we need int() and when not? the number assigned to variables is integer but the input must be string right?

# 2.
x = 60
print(24.95 * 0.6 * x + 3 + 0.75 * (x - 1))

# 3.
import datetime
movingtime= (8*60+15)*2+(7*60+12)*3
t=datetime.datetime(2021,9,8,6,52)
print (t)
h=movingtime//60
m=movingtime%60
print (h)
print (m)
print (t+datetime.timedelta(hours=h,minutes=m))

newt=t+datetime.timedelta(hours=h,minutes=m)
print(newt.time())

# 4.
percentageinnumber=(89-82)/82
percentage=percentageinnumber*100
print(f'{percentage:.1f}%')