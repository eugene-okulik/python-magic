import datetime
from dateutil.relativedelta import relativedelta
import os

now = datetime.datetime.now()
my_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
new_path = os.path.join(my_path, 'eugene_okulik', 'hw_12', 'data.txt')

with open(new_path, 'r') as new_file:
    data = new_file.read()
    list_file = data.splitlines()
    print(data)


def get_date(list_line):
    list_date = list_line.split()
    date = list_date[1] + ' ' + list_date[2]
    return datetime.datetime.fromisoformat(date)


date_1 = get_date(list_file[0])
dt_future = date_1 + relativedelta(years=+ 3)
print(dt_future)

date_2 = get_date(list_file[1])
print(date_2.strftime('%A'))

date_3 = get_date(list_file[2])
print((now - date_3).days)
