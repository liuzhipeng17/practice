# -*- coding: utf-8 -*-


import time
import calendar
# 时间戳---UTC struct time   time.gmtime(时间戳)
print(time.gmtime(0))
print(time.gmtime()) #是在UTC时区，tm_hour可以看出相差8小时，中国的快了8小时

# 时间戳---Local struct time  time.localtime(时间戳)
print(time.localtime()) # 宿主计算机所在地的时区
print(time.localtime(0))


#UTC struct time ---时间戳 calendar.timegm()
s = (1970, 1, 1, 0, 0, 0,3, 1, 0) #元组形式
print(calendar.timegm(s))

#当地时区struct time --->时间戳 time.mktime()
print(time.mktime(time.localtime()))

# struct time (tuple time）---字符串时间  time.strftime(format，t)
# struct time通常是由gmtime, localtime获得，通过格式化成字符串
# format是必要参数，t是可选参数，如果没有t,则默认t = time.localtime()
time_format = '%x' # 小写的x表示年月日date日期
local_tuple = time.localtime()
print(time.strftime(time_format, local_tuple))

# 字符串时间转成struct time  time.strptime(time_str, time_format)
