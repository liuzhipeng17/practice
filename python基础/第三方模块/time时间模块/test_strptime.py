# -*- coding: utf-8 -*-

# strptime是将字符串时间转成struct time

import time

time_format = "%Y-%m-%d %H:%M:%S"
time_str = "2017-09-04 10:38:20"
time_tuple = time.strptime(time_str, time_format)
print(time_tuple)