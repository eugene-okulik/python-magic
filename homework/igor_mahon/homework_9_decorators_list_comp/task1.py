# Задание на декораторы
# Напишите программу: Есть функция которая делает одну из арифметических операций с переданными ей числами
# (числа и операция передаются в аргументы функции). Функция выглядит примерно так:
#
# def calc(first, second, operation):
#     if opertaion == '+':
#     .....
# Программа спрашивает у пользователя 2 числа (вне функции)
#
# Создайте декоратор, который декорирует функцию calc и управляет тем какая операция будет произведена:
#
# если числа равны, то функция calc вызывается с операцией сложения этих чисел
# если первое больше второго, то происходит вычитание второго из певрого
# если второе больше первого - деление первого на второе
# если одно из чисел отрицательное - умножение


def choose_math_operator(func):

    def wrapper(arg1, arg2):
        if arg1 < 0 or arg2 < 0:
            return func(arg1, arg2, '*')
        else:
            if arg1 == arg2:
                return func(arg1, arg2, '+')
            elif arg1 > arg2:
                return func(arg1, arg2, '-')
            elif arg1 < arg2:
                return func(arg1, arg2, '/')

    return wrapper


@choose_math_operator
def calc(first, second, operation):
    if operation == '+':
        return print(first + second)
    elif operation == '-':
        return print(second - first)
    elif operation == '/':
        return print(first / second)
    elif operation == '*':
        return print(first * second)


number_one = int(input('Enter the first number = \n'))
number_two = int(input('Enter the second number = \n'))


calc(number_one, number_two)
