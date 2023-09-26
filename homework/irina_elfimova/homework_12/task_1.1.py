import os
from datetime import datetime, timedelta

main_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

file_path = os.path.join(main_path, 'eugene_okulik', 'hw_12', 'data.txt')

with open(file_path, 'r') as file:
    lines = file.readlines()  # Читаем все строки из файла

    # Берем первую строку из списка и получаем дату на три года вперед
    line1 = lines[0].strip()
    date1 = datetime.strptime(line1, '%Y-%m-%d %H:%M:%S.%f')
    new_date1 = date1 + timedelta(days=3*365)
    print("Новая дата:", new_date1.strftime('%Y-%m-%d %H:%M:%S.%f'))

    # Берем вторую строку из списка и получаем день недели
    line2 = lines[1].strip()
    date2 = datetime.strptime(line2, '%Y-%m-%d %H:%M:%S.%f')
    weekday = date2.strftime('%A')
    print("День недели:", weekday)

    # Берем третью строку из списка и считаем количество дней сегодняшней даты до указанной даты
    line3 = lines[2].strip()
    date3 = datetime.strptime(line3, '%Y-%m-%d %H:%M:%S.%f')
    today = datetime.now().date()
    days_diff = (today - date3.date()).days
    print("Дней назад:", days_diff)
