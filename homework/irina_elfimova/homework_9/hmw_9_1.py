# def calc(first, second, operation):
#     if opertaion == '+':

# Программа спрашивает у пользователя 2 числа (вне функции)
#
# Создайте декоратор, который декорирует функцию calc и управляет тем какая операция будет произведена:
#
# если числа равны, то функция calc вызывается с операцией сложения этих чисел
# если первое больше второго, то происходит вычитание второго из певрого
# если второе больше первого - деление первого на второе
# если одно из чисел отрицательное - умножение

n1 = int(input("Number 1 = "))

n2 = int(input("Number 1 = "))


def calc(first, second, operation):
    if operation == '+':
        print(first + second)
    if operation == '-':
        print(second - first)
    if operation == '/':
        print(first / second)
    if operation == '*':
        print(first * second)


def operation(func):
    def wrapper(n1, n2):
        if n1 == n2:
            func(operation='+')
        if n1 > n2:
            func(operation='-')
        if n1 > n2:
            func(operation='/')
        if n1 < 0 or n2 < 0:
            func(operation='*')

    return wrapper


calc = operation(calc(n1, n2))

#
# def calc(first, second, operation=None):
#     if first == second:
#         operation == '+'
#         print(operation)
#     if first > second:
#         operation == '-'
#
#     if second > first:
#         operation == '/'
#     if first < 0 or second < 0:
#         operation == '*'
#
#
# def new_calc():
#     def wrapper(first, second, operation):
#         if operation == '+':
#             n3 = first + second
#         elif operation == '-':
#             n3 = second - first
#         elif operation == '/':
#             n3 = first / second
#         elif operation == '*':
#             n3 = first * second
#     return wrapper()
#
#
# oper(calc())
