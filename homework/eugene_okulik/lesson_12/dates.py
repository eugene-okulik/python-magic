import datetime
from time import sleep


now = datetime.datetime.now()
print(now)
today_midnight = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
print(today_midnight)
print(now - today_midnight)
expiration_period = datetime.timedelta(hours=10)
expiration_time = now + expiration_period
print(expiration_time)


start = datetime.datetime.now()
sleep(3)
finish = datetime.datetime.now()
elapsed_time = finish - start
print(elapsed_time.seconds)
