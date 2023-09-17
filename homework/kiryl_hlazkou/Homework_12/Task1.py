import requests

import datetime

from dateutil.relativedelta import relativedelta

github_url = 'https://raw.githubusercontent.com/eugene-okulik/python-magic/main/homework/eugene_okulik/hw_12/data.txt'

response = requests.get(github_url)

data_list = response.text.splitlines()

first_date = data_list[0].split(' - ')[0].split('. ')[1]

second_date = data_list[1].split(' - ')[0].split('. ')[1]

third_date = data_list[2].split(' - ')[0].split('. ')[1]

first_date_time = datetime.datetime.strptime(first_date, '%Y-%m-%d %H:%M:%S.%f')

second_date_time = datetime.datetime.strptime(second_date, '%Y-%m-%d %H:%M:%S.%f')

third_date_time = datetime.datetime.strptime(third_date, '%Y-%m-%d %H:%M:%S.%f')

# 1.2022-05-14 20:34:13.212967 - распечатать эту дату, но на три года позже. Должно быть 2025-05-14 20:34:13.212967

new_date = first_date_time + relativedelta(years=3)

print('1) Updated Date:', new_date.strftime('%Y-%m-%d %H:%M:%S.%f'))

# 2. 2023-07-15 18:25:10.121473 - распечатать какой это будет день недели

day_of_week = second_date_time.strftime('%A')

print('2) Day of the Week:', day_of_week)

# 3. 2023-06-12 15:23:45.312167 - распечатать сколько дней назад была эта дата

today = datetime.datetime.now()

days_ago = (today - third_date_time).days

print('3) Days Ago:', days_ago)
