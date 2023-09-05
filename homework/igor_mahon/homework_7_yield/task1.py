# Задание 1
# Напишите программу. Есть две переменные, salary и bonus. Salary - int, bonus - bool.
# Спросите у пользователя salary. А bonus пусть назначается рандомом.
# Если bonus - true, то к salary должен быть добавлен рандомный бонус.
# Примеры результатов:
# 10000, True - '$10255'
# 25000, False - '$25000'
# 600, True - '$3785'

import random


def rand_bonus(salary: int):
    bonus = random.choice([True, False])
    if bonus:
        new_salary = salary + random.randint(1, 10000)
    else:
        new_salary = salary
    return print(salary, ", ", bonus, " - '$" + str(new_salary) + "'", sep="")


my_little_salary = int(input('Your salary: \n'))

rand_bonus(my_little_salary)
