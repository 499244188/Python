# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 14:06:18 2017

@author: Z
"""

from datetime import datetime
now = datetime.now()
print(now)
print(type(now))

#指定时间日期

dt = datetime(2017,5,4,23,1)
print(dt)
dt.timestamp()#把datatime转为timestamp


t = 3600*24*360*48-3600*24*11
print(datetime.fromtimestamp(t))

t = 1493910060.0
print(datetime.fromtimestamp(t))#本地时间
print(datetime.utcfromtimestamp(t))#UTC时间


#str转为datetime
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)

#datetime转为str
now=datetime.now()
print(now.strftime('%A,%b %d %H:%M'))
     

#datetime 加减
from datetime import datetime,timedelta
now = datetime.now()

now+timedelta(hours=10)

now-timedelta(days = 19)

now + timedelta(days=2,hours=13)

#本地时间转UTC时间
from datetime import timezone
tz_utc_8 = timezone(timedelta(hours=8))
now = datetime.now()

dt = now.replace(tzinfo=tz_utc_8) #强制设置为UTC+8:00


#时区转换
#拿到utc时间，并强制设置时区为utc+0:00
utc_td = datetime.utcnow().replace(tzinfo=timezone.utc)

#astimezone()将时区转换为北京时间
bj_dt = utc_td.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)

#astimezone 将时区转为东京时间：
tokyo_dt = utc_td.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)

#astimezone（） 将北京时区换位东京时间
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
















