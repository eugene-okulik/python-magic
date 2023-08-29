import datetime

my_time = "Jan 15, 2023 - 12:05:33"

python_my_time = datetime.datetime.strptime(my_time, '%b %d, %Y - %H:%M:%S')

print(datetime.datetime.strftime(python_my_time, '%B'))

print(datetime.datetime.strftime(python_my_time, '%d.%m.%Y, %H:%M'))
