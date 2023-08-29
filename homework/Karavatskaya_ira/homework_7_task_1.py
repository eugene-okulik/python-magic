# напишите программу. Есть две переменные: salary и bonus.
# Salary  - int, bonus - bool.
# Спросите у пользователя salary, а bonus пусть назначается рандомом.
# Если bonus - True, то к salary должен быть добавлен рандомный бонус.


import random


def your_salary():
    salary = int(input('Введите значение зарплаты'))
    bonus = random.choice([True, False])

    if bonus:
        bonus_value = random.randint(1, 1000)
        nuw_salary = salary + bonus_value
        print(salary, ',', bonus, '-', '`', '$', nuw_salary, '`')
    else:
        print(salary, ',', bonus, '-', '`', '$' + str(salary) + '`')


your_salary()
