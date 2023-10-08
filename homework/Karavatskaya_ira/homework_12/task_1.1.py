import os
import datetime
from dateutil.relativedelta import relativedelta

now = datetime.datetime.now()
main_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
file_path = os.path.join(main_path, 'eugene_okulik', 'hw_12', 'data.txt')

with open(file_path, 'r') as new_file:
    data = new_file.read()
    list_file = data.splitlines()
    print(data)


def get_date(list_line):
    list_date = list_line.split()
    date = list_date[1] + ' ' + list_date[2]
    return datetime.datetime.fromisoformat(date)


# Добавляем три года к дате
first_date = get_date(list_file[0])
three_years_later = first_date + relativedelta(years=+ 3)
print(three_years_later)

# Получаем название дня недели
second_date = get_date(list_file[1])
print(second_date.strftime('%A'))

# Вычисляем разницу между текущей датой и указанной датой
date_3 = get_date(list_file[2])
days_ago = (now - date_3).days
print(days_ago)
