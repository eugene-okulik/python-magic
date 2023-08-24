print('Enter number 1')
num1 = int(input())
print('Enter number 2')
num2 = int(input())


def multiply(n1, n2):
    num = num1 * num2
    if num > 20:
        num = num * 2
    else:
        num = num * 3
    return num


print(multiply(num1, num2))
