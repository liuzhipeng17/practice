# -*- coding: utf-8 -*-

#strftime是将struct time转化成字符串time(人能读时间）

import time

time_format = '%x' # 小写的x表示年月日date日期
local_tuple = time.localtime()
print(time.strftime(time_format, local_tuple))

time_format = '%X' # 大写的X表示时分秒time
local_tuple = time.localtime()
print(time.strftime(time_format, local_tuple))

time_format = '%Y' #大写的Y表示年，包含世纪（1989），小写的y不包含世纪(89)
time_format = '%m' #小写的m表示月（01-12），大写的M表示分00-59
time_format = "%d" # 小写d 表示日（01-31）
time_format = "%H" #大写的H表示时(00-23)
time_format = "%S" #大写S表示秒

time_format = "%Y-%m-%d %H:%M:%S"
time_tuple = time.localtime()
time_str = time.strftime(time_format, time_tuple)
print(time_str)