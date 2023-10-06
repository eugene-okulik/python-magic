num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))


def cal(a, b):
    return a * b


result = cal(num1, num2)

if result > 20:
    print(cal(result, 2))
else:
    print(cal(result, 3))
