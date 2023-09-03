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
        else:
            return func(num1, num2, '*')
    return wrapper


@calc_decorator
def calc(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '/':
        return num1 / num2
    elif operation == '*':
        return num1 * num2


def main():
    num1 = float(input("Введите первое число"))
    num2 = float(input("Введите второе число"))
    result = calc(num1, num2)
    print(result)


if __name__ == "__main__":
    main()

print(calc)
