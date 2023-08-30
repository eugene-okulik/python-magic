print('Enter number 1')
num1 = int(input())
print('Enter number 2')
num2 = int(input())


def multiply(n1, n2):
    return n1 * n2


num3 = multiply(num1, num2)

if num3 > 20:
    print(num3 * 2)
else:
    print(num3 * 3)
