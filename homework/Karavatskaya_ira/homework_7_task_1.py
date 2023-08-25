# напишите программу. Есть две переменные: salary и bonus.
# Salary  - int, bonus - bool.
# Спросите у пользователя salary, а bonus пусть назначается рандомом.
# Если bonus - True, то к salary должен быть добавлен рандомный бонус.


import random


def your_salary():
    salary = int(input('Введите значение зарплаты'))
    bonus = bool(random.getrandbits(1))
    print(bonus)
    if bonus:
        bonus_value = random.randint(1, 1000)
        nuw_salary = salary + bonus_value
        print(salary, ',', bonus, '-', '`', '$', nuw_salary, '`')
    else:
        salary = salary
        print(salary, ',', bonus, '-', '`', '$' + str(salary) + '`')


print(your_salary())
