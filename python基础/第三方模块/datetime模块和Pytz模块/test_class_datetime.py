# -*- coding: utf-8 -*-

# 构造函数
from datetime import datetime, timezone
# datetime.datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None)¶
dt = datetime(year=2017, month=2, day=25)

# 类方法，datetime.today()
# 返回本地时间宿主计算机上的时间
print(dt.today())
# 2017-09-04 11:37:25.219690

# 类方法now()
print(dt.now())
# 和dt.today（）等效

# 类方法utcnow()
print(dt.utcnow())
# 返回utc的当前时间

# 字符串实例化一个datetime对象
dt = datetime.strptime("2017:06:04 11:37:15", "%Y:%m:%d %H:%M:%S")
print(dt)
# 2017-06-04 11:37:15

# datetime.timetuple（）获取时间属性元组
tt = dt.timetuple()
for it in tt:
    # print(it)
    pass

# 将时间转换成字符串strftime(format)
#     pass

# 将时间按照不同时区转换(更新时区）datetime.astimezone()
# 从一个datetime对象，添加一个时区：使用方法： dt.replace(tzinfo=tz)
# 当然tz必须是tzinfo对象
# 如果想从一个datetime对象，删除时区，dt.replace(tzinfo=None)

dt = datetime(2017,9,4,11,55,00)
dt_utc = dt.replace(tzinfo=timezone.utc)

print(dt_utc.tzinfo)
