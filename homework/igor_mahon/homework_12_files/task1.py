import os
import datetime

# Нужно прочитать файлик, который лежит в репозитории в моей папке.
# Здесь: homework/eugene_okulik/hw_12/data.txt
homework_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
okulik_path = os.path.join(homework_path, 'homework', 'eugene_okulik', 'hw_12', 'data.txt')

with open(okulik_path, 'r') as hw_file:
    data = hw_file.read()

date_collector = []
for word in data.split():
    if (word.startswith('2') or word.startswith('1')) and len(word) > 2:
        date_collector.append(word)

# распечатать дату, но на три года позже
date1 = " ".join([date_collector[0], date_collector[1]])
python_date1 = datetime.datetime.strptime(date1, "%Y-%m-%d %H:%M:%S.%f")
three_years_later = python_date1 + datetime.timedelta(days=1096)
print(three_years_later)

# распечатать какой это будет день недели
python_date2 = datetime.datetime.strptime(date_collector[4], "%Y-%m-%d")
day_of_week = python_date2.strftime("%A")
print(f'It is {day_of_week}')

# распечатать сколько дней назад была эта дата
python_date3 = datetime.datetime.strptime(date_collector[6], "%Y-%m-%d")
day_passed_since_date3 = (datetime.datetime.now() - python_date3).days
print(f'{day_passed_since_date3} days passed')
