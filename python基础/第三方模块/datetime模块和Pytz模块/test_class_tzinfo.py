# -*- coding: utf-8 -*-

# utc时间：utc是利用原子钟计算出来，比GMT（格林时间更准确）
# 现在世界上不同时区的时间都是以UTC时间为准，比如北京时间= UTC时间 + 8小时

# tzinfo对象是用来表示该时区相对UTC时间差值，和该地区是否执行夏时令的对象。

# datetime中tzinfo对象，是一个抽象基类，我们不应该直接实例化一个tzinfo对象
# 而是定义一个子类继承tzinfo，然后实例化该子类，再可以使用。但是定义该子类的各种方法十分繁琐
# 幸好python第三方库pytz，里面包含各种国家/时区的tzinfo对象，我们可以直接使用

import pytz
from datetime import datetime

# http://pythonhosted.org/pytz/   pytz学习网站

utc = pytz.utc
print(utc.zone)
# UTC

eastern = pytz.timezone('US/Eastern')
print(eastern)
print(type(eastern)) # 是一个类，pytz.tzfile.US/Eastern
# US/Eastern

# 选好时区后，localize():将原生时间转成时区时间（有意识时间）
# eastern = pytz.timezone('US/Eastern')
fmt = "%Y-%m-%d %H:%M:%S %Z%z"
naive_dt = datetime(2017,9,4,12,55,0)
eastern = pytz.timezone('US/Eastern')
eas_dt = eastern.localize(naive_dt)
str_dt = eas_dt.strftime(fmt)
print(str_dt)
# 2017-09-04 12:26:44 EDT-0400

# astimezone()是将某个时区的时间，转换成另外一个时区的时间
# 下面的方法是将美国东部时间转成UTC时间

fmt = "%Y-%m-%d %H:%M:%S %Z%z"
eastern = pytz.timezone('US/Eastern')
loc_dt = eastern.localize(datetime.now())
print(loc_dt.strftime(fmt))
# 2017-09-04 12:32:16 EDT-0400 ：上面部分是将宿主计算机时间添加美国东部时间属性
utc_dt = loc_dt.astimezone(utc)
str_dt = utc_dt.strftime(fmt)
print(str_dt)
# 2017-09-04 16:30:32 UTC+0000

# datetime对象.astimezone(时区对象)实现不同时区的时间转换， 更改fmt格式为规范化格式pytz.utc.normalize，
# 其他时区也有这个方法,eastern.normalize(datetime对象)，最好不用

naive_dt = datetime(2017,9,4,12,53,22)
eastern = pytz.timezone('US/Eastern')
loc_dt = eastern.localize(naive_dt)
print(eastern.normalize(loc_dt))
# eastern.normalize()

# 不可以直接将datetime的tzinfo直接赋值，除了pytz.utc外
fmt = "%Y-%m-%d %H:%M:%S %Z%z"
utc_dt = datetime(2017,9,4,12,37,22, tzinfo=pytz.utc)
print(utc_dt.strftime(fmt))

# 记住一个原则： 时间的操作都是在utc上进行操作，只是最后转换成本地时区的时间
