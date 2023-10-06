# Задание 1
# Напишите программу. Есть две переменные, salary и bonus. Salary - int, bonus - bool. Спросите у пользователя salary.
# А bonus пусть назначается рандомом.
#
# Если bonus - true, то к salary должен быть добавлен рандомный бонус.
#
# Примеры результатов:
#
# 10000, True - '$10255'
# 25000, False - '$25000'
# 600, True - '$3785'

import random

salary = int(input('Your salary: '))

bonus = bool(random.choice([True, False]))

print(bonus)

discount = random.randint(100, 1000)

print(discount)

if bonus is True:
    print(salary, ',', bonus, '-', '$', salary + discount)
else:
    print(salary, ',', bonus, '-', '$', salary)
