import os
from datetime import datetime, timedelta

my_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

new_path = os.path.join(my_path, 'eugene_okulik', 'hw_12', 'data.txt')

with open(new_path, 'r') as new_file:
     path = new_file.readline()
print(path)