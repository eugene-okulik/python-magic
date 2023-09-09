import os
import json


data_file = open('data.txt', 'r')
data = data_file.read()
try:
    data = json.loads(data)
except json.JSONDecodeError:
    pass
data_file.close()

print(data)
print(len(data))

with open('data.txt', 'w') as data_file:
    data = data_file.write('\nnew line')

print(data)

# path = '/home/eugene/projects/python-magic/homework/kiryl_hlazkou/example.txt'
#  C:\users\eugene\projects\python-magic\homework\kiryl_hlazkou\example.txt
my_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
new_path = os.path.join(my_path, 'kiryl_hlazkou', 'example.txt')
# print(my_path)
# print(new_path)

with open(new_path, 'r') as new_file:
    print(new_file.read())
