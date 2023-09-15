# Создайте такую программу:
# пользователь вводит два числа.
# Программа умножает одно число на другое.
# Если результат этого умножения больше 20, то этот результат умножается на 2.
# Если результат изначального умножения меньше или равно 20, то он умножается на 3.


def multiply_numbers(numb_1, numb_2):
    return numb_1 * numb_2


def resalt(numb_3, numb_4):
    if multiply_numbers(numb_3, numb_4) > 20:
        return print(multiply_numbers(numb_3, numb_4) * 2)
    else:
        return print(multiply_numbers(numb_3, numb_4) * 3)


a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))


resalt(a, b)
