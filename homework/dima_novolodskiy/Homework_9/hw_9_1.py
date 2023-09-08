def convert(func):
    def wrapper(*args):
        c = ''
        if a == b:
            c = '+'
        elif a > b:
            c = '-'
        elif a < b:
            c = '/'
        elif a < 0 or b < 0:
            c = '*'
        return func(a, b, c)

    return wrapper


@convert
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return first / second
    else:
        return first * second


a, b = map(int, input().split())

print(calc(a, b))
