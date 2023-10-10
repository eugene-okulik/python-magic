import os
import datetime
from dateutil.relativedelta import relativedelta

homework_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
ok_path = os.path.join(homework_path, 'homework', 'eugene_okulik', 'hw_12', 'data.txt')

with open(ok_path, 'r') as hw_file:
    data = hw_file.read()

data_list = data.splitlines()

date_times = []
for item in data_list:
    date_str = item.split(' - ')[0].split('. ')[1]
    date_time = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S.%f')
    date_times.append(date_time)

# 1.2022-05-14 20:34:13.212967 - распечатать эту дату, но на три года позже. Должно быть 2025-05-14 20:34:13.212967

new_date = date_times[0] + relativedelta(years=3)
print('1) Updated Date:', new_date.strftime('%Y-%m-%d %H:%M:%S.%f'))

# 2. 2023-07-15 18:25:10.121473 - распечатать какой это будет день недели

day_of_week = date_times[1].strftime('%A')
print('2) Day of the Week:', day_of_week)

# 3. 2023-06-12 15:23:45.312167 - распечатать сколько дней назад была эта дата

today = datetime.datetime.now()
days_ago = (today - date_times[2]).days
print('3) Days Ago:', days_ago)
