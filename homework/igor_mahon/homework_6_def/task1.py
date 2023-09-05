# Задание 1
# Создайте такую программу:
# Пользователь вводит два числа
# Программа умножает одно число на другое
# Если результат этого умножения больше 20, то этот результат умножается на 2.
# А если результат изначального умножения меньше или равно 20, то он умножается на 3


def multiplier(int1, int2):
    return int1 * int2


def number_handler(int3, int4):
    if multiplier(int3, int4) > 20:
        return print(multiplier(int3, int4) * 2)
    else:
        return print(multiplier(int3, int4) * 3)


a = int(input('Введите первое число: \n'))
b = int(input('Введите второе число: \n'))

number_handler(a, b)
