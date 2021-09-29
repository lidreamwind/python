from datetime import datetime, timedelta
import time

# 返回当前时间的datetime对象
now = datetime.now()
print(now)
print(type(now))
# 1970-1-1 00:00:00 截止到目前的时间（秒）
print(now.timestamp())

print(now.strftime('%H:%M:%S %Y/%m/%d'))
print(now.year, now.month, now.day)

# 去年的今天
last_year = now.replace(year=2019)
print(last_year.strftime('%Y-%m-%d %H:%M:%S'))
delta = now - last_year
print(type(delta))
print(delta.days, delta.seconds)
# 明年的今天
print(now + delta)
# 20天以后的时间
print(now + timedelta(days=20))
# 两个半小时之前的时间
print(now - timedelta(hours=2, minutes=30))

print(time.time())
print(time.strftime('%Y-%m-%d %H:%M:%S'))

print("好累呀，我要休息3秒钟")
time.sleep(3)
print("好啦，我又元气满满了")