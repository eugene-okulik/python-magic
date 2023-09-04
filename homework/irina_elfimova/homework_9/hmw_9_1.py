num1 = int(input("Number 1 = "))

num2 = int(input("Number 1 = "))


def operation(func):
    def wrapper(n1, n2):
        if n1 == n2:
            func(n1, n2, "+")
        else:
            if n1 > n2:
                func(n1, n2, "-")
            elif n2 > n1:
                func(n1, n2, '/')
            elif n1 < 0 or n2 < 0:
                func(n1, n2, '*')

    return wrapper


@operation
def calc(first, second, operation):
    if operation == '+':
        print(first + second)
    elif operation == '-':
        print(second - first)
    elif operation == '/':
        print(first / second)
    elif operation == '*':
        print(first * second)


calc(num1, num2)
