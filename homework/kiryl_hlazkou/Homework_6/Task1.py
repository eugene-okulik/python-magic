num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))


def cal():
    result = num1 * num2
    if result > 20:
        result *= 2
    else:
        result *= 3
    return result


final_result = cal()

print("The final result is:", final_result)
