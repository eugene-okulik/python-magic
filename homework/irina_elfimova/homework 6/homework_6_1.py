
print('Enter number 1')
num1 = int(input())
print('Enter number 2')
num2 = int(input())

num = num1 * num2


def multiply(new_num):
    if num > 20:
        numb = num * 2
        return numb
    elif num <= 20:
        numb1 = num * 3
        return numb1


print(multiply(num))
