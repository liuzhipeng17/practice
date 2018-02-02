# -*- coding: utf-8 -*-

import datetime

now = datetime.datetime.now()
last = datetime.datetime(year=2016, month=9, day=3, hour=12)
delta = now - last
print(delta)
# 366 days, 0:07:38.303065

# delta表示一段时间，有days，时，分，秒，微秒属性
# 也可以将其初始化
import datetime
now = datetime.datetime.now()
print(now)
delta = datetime.timedelta(days=1, seconds=10, milliseconds=100, hours=2,)
future = now + delta
print(future)
# future表示1天2小时10.1秒后
