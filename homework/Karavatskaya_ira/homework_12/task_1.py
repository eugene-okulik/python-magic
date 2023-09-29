import datetime
import os
from datetime import date


main_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
file_path = os.path.join(main_path, 'eugene_okulik', 'hw_12', 'data.txt')

with open(file_path, 'r') as new_file:
    new_date_1 = new_file.readline()
    new_date_2 = new_file.readline()
    new_date_3 = new_file.readline()


def new_data(data, time):
    dat = data.split('-')
    dat[0] = str(int(dat[0]) + 3)
    result = '-'.join(dat) + ' ' + time
    return result


def week_day(data):
    new_d = data.split('-')
    year = int(new_d[0])
    month = int(new_d[1])
    day = int(new_d[2])
    w_day = (datetime.datetime(year, month, day))
    return w_day.strftime('%A')


def day_before(data):
    today = date.today()
    before = date.fromisoformat(data)
    delta = abs(today - before)
    return delta.days


print('На три года позже:', new_data)
print('День недели:', week_day)
print('Cколько дней назад была эта дата:', day_before)
