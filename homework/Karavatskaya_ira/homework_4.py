# Задание 1:
# Дан список: person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
# С помощью распаковки создайте из этого списка переменные, содержащие соответствующие данные:
# name, last_name, city, phone, country

person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person
print(person)


# Задание 2:
# Допустим, какая-то программа возвращает результат своей работы в таком виде:
# результат операции: 42
# результат операции: 54
# С помощью срезов и метода index получите из каждой строки с результатом число, прибавьте к полученному числу 10,
# результат сложения распечатайте.

result_one = "результат операции: 42"
result_two = "результат операции: 54"

phrase = "операции: "
len_phrase = len(phrase)

details_result_index1 = result_one.lower().index("операции: ") + len_phrase
details_result_index2 = result_two.lower().index("операции: ") + len_phrase

print(int(result_one[details_result_index1:]) + 10)
print(int(result_two[details_result_index2:]) + 10)


# Задание 3:
# Даны такие списки:
# students = ['Ivanov', 'Petrov', 'Sidorov']
# subjects = ['math', 'biology', 'geography']
# Распечатайте текст, который будет использовать данные из этих списков. Текст в итоге должен выглядеть так:
# Students Ivanov, Petrov, Sidorov study these subjects: math, biology, geograpy

students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']

print("Students", ", ".join(students), "study these subjects:", ", ".join(subjects))
