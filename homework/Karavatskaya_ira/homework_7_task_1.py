# напишите программу. Есть две переменные: salary и bonus.
# Salary  - int, bonus - bool.
# Спросите у пользователя salary, а bonus пусть назначается рандомом.
# Если bonus - True, то к salary должен быть добавлен рандомный бонус.


import random


def apply_bonus(your_salary, bonus_n):
    if bonus_n:
        bonus_amount = random.randint(0, 100)
        your_salary += bonus_amount
    return your_salary


salary = int(input("Введите значение зарплаты: "))
bonus = random.choice([True, False])
final_salary = apply_bonus(salary, bonus)

print(salary, bonus, '-', "`", '$', final_salary, '`')
