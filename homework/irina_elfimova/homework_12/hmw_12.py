import os
import datetime
from datetime import date


main_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

file_path = os.path.join(main_path, 'eugene_okulik', 'hw_12', 'data.txt')

with open(file_path, 'r') as new_file:
    new_date_1 = new_file.readline()
    new_date_2 = new_file.readline()
    new_date_3 = new_file.readline()


n1, date_1, time_1, *z = new_date_1.split(' ')

n2, date_2, time_2, *z1 = new_date_2.split(' ')

n3, date_3, time_3, *z2 = new_date_3.split(' ')


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
    w_day = (datetime.datetime(year, month, day)).weekday()
    if w_day == 0:
        return 'Понедельник'
    elif w_day == 1:
        return 'Вторник'
    elif w_day == 2:
        return 'Среда'
    elif w_day == 3:
        return 'Четверг'
    elif w_day == 4:
        return 'Пятница'
    elif w_day == 5:
        return 'Суббота'
    elif w_day == 6:
        return 'Воскресенье'


def day_before(data):
    today = date.today()
    before = date.fromisoformat(data)
    delta = abs(today - before)
    return delta.days


print('На три года позже:', new_data(date_1, time_1))
print('День недели:', week_day(date_2))
print('Cколько дней назад была эта дата:', day_before(date_3))
