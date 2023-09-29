# Создайте такую программу:
# пользователь вводит два числа.
# Программа умножает одно число на другое.
# Если результат этого умножения больше 20, то этот результат умножается на 2.
# Если результат изначального умножения меньше или равно 20, то он умножается на 3.


def multiply_numbers(numb_1, numb_2):
    return numb_1 * numb_2


def resalt(numb_3, numb_4):
    first_result = multiply_numbers(numb_3, numb_4)
    if first_result > 20:
        print(multiply_numbers(first_result, 2))
    else:
        print(multiply_numbers(first_result, 3))

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))


resalt(a, b)
