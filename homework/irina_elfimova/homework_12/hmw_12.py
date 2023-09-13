import os
import datetime

path = '/Users/irinaelfimova/Documents/python-magic/untitled folder/homework/eugene_okulik/hw_12/data.txt'
main_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))


file_path = os.path.join(main_path, 'eugene_okulik', 'hw_12', 'data.txt')
print(file_path)


with open(file_path, 'r') as new_file:
    # for line in new_file.readlines():
    #     print(line)
    new_date_1 = new_file.readline()
    new_date_2 = new_file.readline()
    new_date_3 = new_file.readline()

    print(new_date_1)
    print(new_date_2)
    print(new_date_3)
