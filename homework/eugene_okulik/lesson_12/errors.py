def calc(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        # print('lkasdhfksjdhkjhsdf')
        return None


def calc2(x):
    if x:
        return x * 2
    else:
        return 'Error happened'


for a, b in [(2, 8), (3, 5), (1, 0), (7, 2)]:
    result1 = calc(a, b)
    print(calc2(result1))
