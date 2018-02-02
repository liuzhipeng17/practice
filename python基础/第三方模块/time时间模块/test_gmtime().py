# -*- coding: utf-8 -*-

import time

print(time.time()) # 返回当地时间
print(time.gmtime(time.time()))
print(time.gmtime())

# time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)
# time.gmtime(seconds)
# gmtime是将时间戳转化成utc struct time
# 它的逆函数是calendar.timegm()
# 如果seconds没有提供，默认seconds = time.time()
# time.time(）返回的是utc时间 当前时间