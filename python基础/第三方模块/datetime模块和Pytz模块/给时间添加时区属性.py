# -*- coding: utf-8 -*-

import datetime

now = datetime.datetime(2014,8,10,18,18,30)
print(now.tzinfo)
now_utc = now.replace(tzinfo=datetime.timezone.utc)
now_local = now_utc.astimezone()
print(now_local)

# datetime.datetime()有以下几个属性：
#Attributes: year, month, day, hour, minute, second, microsecond, and tzinfo.