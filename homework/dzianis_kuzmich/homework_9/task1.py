def operation_manager(func):
    def wrapper(first, second):
        if first < 0 or second < 0:
            return func(first, second, '*')
        elif first == second:
            return func(first, second, '+')
        elif first > second:
            return func(first, second, '-')
        elif first < second:
            return func(first, second, '/')
    return wrapper


@operation_manager
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return first / second if second != 0 else "Cannot divide by zero"
    elif operation == '*':
        return first * second


# Get user input
first = float(input("Enter the first number: "))
second = float(input("Enter the second number: "))

result = calc(first, second)
print(f"Result: {result}")
