import os
from datetime import datetime, timedelta

main_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

file_path = os.path.join(main_path, 'eugene_okulik', 'hw_12', 'data.txt')

with open(file_path, 'r') as file:
    data = file.read()
    print(data)
    lines = data.split('\n')

    lines_1 = data.split()[1] + ' ' + data.split()[2]
    first_date = datetime.strptime(lines_1, '%Y-%m-%d %H:%M:%S.%f')
    new_date = first_date + timedelta(days=3*365)
    print(f'Дата на три года позже', new_date)

    lines_2 = data.split(' ')[16]
    second_date = datetime.strptime(lines_2, "%Y-%m-%d")
    print(second_date)
    day_of_week = second_date.strftime("%A")
    print(day_of_week)

    lines_3 = lines[2].strip() + ' '
    print(lines_3)
    

    #date3 = datetime.strptime(lines_3, '%Y-%m-%d %H:%M:%S.%f')
    #print(date3)
    #today = datetime.now().date()
    #days_diff = (today - date3.date()).days
    #print("Дней назад:", days_diff)
    #today = datetime.now().date()
    #days_diff = (today - date3.date()).days
    #print("Дней назад:", days_diff)