num1 = int(input('Enter first number: '))

num2 = int(input('Enter second number: '))

res1 = num1 * num2


def calc(res2):
    if res2 <= 20:
        print(res2 * 3)
    else:
        print(res2 * 2)


calc(res1)
