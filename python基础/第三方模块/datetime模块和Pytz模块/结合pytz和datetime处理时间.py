from datetime import datetime, timedelta
import pytz

naive_dt = datetime(2014, 5, 1, 23, 33, 24)
eastern = pytz.timezone("US/Eastern")
eas_dt = eastern.localize(naive_dt)
eas_str = eastern.normalize(eas_dt)
print(eas_str)
# 2014-05-01 23:33:24-04:00  # -4:00表示比UTC慢4个钟
# 上面是得到了美国东部时间2014/05/01 23:33:24

# 如果我们已知美国东部时间，计算3小时后的中国时间，采用astimezone()，以及timedelta

eas_dt = eas_dt + timedelta(hours=3)
print(eastern.normalize(eas_dt))
ch_tz = pytz.timezone("Asia/Shanghai")
ch_dt = eas_dt.astimezone(ch_tz)
ch_str = ch_tz.normalize(ch_dt)
print(ch_str)




