# Дан такой список:

person = ['John', 'Doe', 'New York', '+1372829383739', 'US']

# С помощью распаковки создайте из этого списка переменные, содержащие соответствующие данные:

# name, last_name, city, phone, country#
name, last_name, city, phone, country = person

print(name)
print(last_name)
print(city)
print(phone)
print(country)


# Допустим, какая-то программа возвращает результат своей работы в таком виде:
#
# результат операции: 42
#
# результат операции: 54
#
# С помощью срезов и метода index получите из каждой строки с результатом число,
# прибавьте к полученному числу 10, результат сложения распечатайте.

msg_1 = 'результат операции: 42'
msg_2 = 'результат операции: 54'
word = 'операции:'
len_word = len(word) + 1

details_index = msg_1.lower().index(word) + len_word
print(msg_1[details_index:])
new_num_1 = int(msg_1[details_index:]) + 10
print(new_num_1)


details_index = msg_2.lower().index(word) + len_word
print(msg_2[details_index:])
new_num_2 = int(msg_2[details_index:]) + 10
print(new_num_2)

# Даны такие списки:

students = ['Ivanov', 'Petrov', 'Sidorov']

subjects = ['math', 'biology', 'geography']

# Распечатайте текст, который будет использовать данные из этих списков. Текст в итоге должен выглядеть так:

# Students Ivanov, Petrov, Sidorov study these subjects: math, biology, geograpy

print(f'Students {", ".join(students)}', f'study these subjects: {", ".join(subjects)}')
