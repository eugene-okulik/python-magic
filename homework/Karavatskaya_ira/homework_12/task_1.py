import os
from datetime import datetime, timedelta
import calendar

main_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
file_path = os.path.join(main_path, 'eugene_okulik', 'hw_12', 'data.txt')

with open(file_path, 'r') as new_file:
    data = new_file.read()
    print(data)

lines = data.split('\n')

date_parts_1 = lines[0].split(' ')[1].split(' - ')
original_date_1 = ' '.join(date_parts_1)
data_1 = datetime.strptime(original_date_1, '%Y-%m-%d')
# Добавляем три года к дате
three_years_later = data_1 + timedelta(days=1096)
print(three_years_later)

date_parts_2 = lines[1].split(' ')[1].split(' - ')
original_date_2 = ' '.join(date_parts_2)
data_2 = datetime.strptime(original_date_1, '%Y-%m-%d')
weekday = data_2.weekday()
# Получаем название дня недели
weekday_name = calendar.day_name[weekday]
print(weekday_name)

date_parts_3 = lines[2].split('. ')[1].split(' -')[0]
print(date_parts_3)
date_3 = datetime.strptime(date_parts_3, '%Y-%m-%d %H:%M:%S.%f')
print(date_3)
current_date = datetime.now()
# Вычисляем разницу между текущей датой и указанной датой
days_ago = (current_date - date_3).days
print(days_ago)
