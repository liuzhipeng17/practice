# -*- coding: utf-8 -*-

import datetime
import time

# 实例化datetime.date类，必须传递三个参数，year, month, day
# 三个参数都必须是整数，而且有范围要求：超出范围，抛出异常ValueError
# 1 <= year <=9999
# 1 <= month <= 12
# 1 <= day <= 最大值：根据month而定，可能是29，可能是30，可能是31
d = datetime.date(year=2017, month=9, day=4)

# 类函数datetime.date.today()
print(datetime.date.today())
# 2017-09-04
# 返回的是local（宿主计算机上）年月日（当然是utc)

#类函数date.fromtimestamp(时间戳）
#将时间戳转成date格式
print(datetime.date.fromtimestamp(time.time()))
# 等效datetime.date.today()
# 2017-09-04

# d = date(2002, 12, 31),
# d.replace(day=26) 等于date(2002, 12, 26).
# 对象函数date.replace(year, month, day)

s = d.replace(day=22) # d并没有改变
print(s)
# 2017-09-22

# 对象函数date.timetuple()
# 将date转换成结构化时间
print(d.timetuple())
# time.struct_time(tm_year=2017, tm_mon=9, tm_mday=4, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=0, tm_yday=247, tm_isdst=-1)

# 对象函数date.ctime()
# 将日期按照特定格式，转成字符串
print(d.ctime())
# Mon Sep  4 00:00:00 2017

# 对象函数date.strftime(format) 和time一样
time_format = "%Y_%m_%d"
print(d.strftime(time_format))
# 2017_09_04

# date支持的操作
# date2 = date1 + timedelta
# date2 = date1 - timedelta
# timedelta = date1 - date2
# date1 < date2 （如果date1比date2早）

