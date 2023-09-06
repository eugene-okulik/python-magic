# Программа спрашивает у пользователя 2 числа (вне функции)
#
# Создайте декоратор, который декорирует функцию calc и управляет тем какая операция будет произведена:
#
# если числа равны, то функция calc вызывается с операцией сложения этих чисел
# если первое больше второго, то происходит вычитание второго из певрого
# если второе больше первого - деление первого на второе
# если одно из чисел отрицательное - умножение


def calc_decorator(func):
    def wrapper(num1, num2):
        if num1 == num2:
            return func(num1, num2, '+')
        elif num1 > num2:
            return func(num1, num2, '-')
        elif num1 < num2:
            return func(num1, num2, '/')
        elif num1 < 0 or num2 < 0:
            return func(num1, num2, '*')
    return wrapper


@calc_decorator
def calc(num1, num2, operation):
    if operation == '+':
        return print(num1 + num2)
    elif operation == '-':
        return print(num1 - num2)
    elif operation == '/':
        return print(num1 / num2)
    elif operation == '*':
        return print(num1 * num2)


num_1 = int(input("Введите первое число"))
num_2 = int(input("Введите второе число"))


calc(num_1, num_2)
