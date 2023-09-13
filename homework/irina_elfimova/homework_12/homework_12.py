import os
import datetime

path = '/Users/irinaelfimova/Documents/python-magic/untitled folder/homework/eugene_okulik/hw_12/data.txt'
main_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

#file_path = f'{main_path}/homework/eugene_okulik/hw_12/data.txt'
file_path = os.path.join(main_path, 'eugene_okulik', 'hw_12', 'data.txt')
print(file_path)

# file_path = os.path.join(main_path, 'homework', 'eugene-okulik', 'hw_12', 'data.txt')
#
# with open(file_path, 'r') as new_file:
#     print(new_file.read())
#
# new_file.close()

with open(file_path, 'r') as new_file:
    # for line in new_file.readlines():
    #     print(line)
    new_date_1 = new_file.readline()
    new_date_2 = new_file.readline()
    new_date_3 = new_file.readline()

first_date = new_date_1.rstrip('.-')
second_date = new_date_2.rstrip('.-')
third_date = new_date_.rstrip('.-')

    print(new_date_1)
    print(new_date_2)
    print(new_date_3)

date_time_obj = datetime.datetime.strptime(new_date_1, '%Y-%m-%d %H:%M:%S.%f')
print('Дата:', date_time_obj.date())
print('Время:', date_time_obj.time())
print('Дата и время:', date_time_obj)