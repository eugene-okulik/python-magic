# Функция для умножения двух чисел
def multiply(a, b):
    return a * b


# Запрос на ввод двух чисел от пользователя
number_one = float(input("Введите первое число: "))
number_two = float(input("Введите второе число: "))

# Умножение чисел
result = multiply(number_one, number_two)

# Проверка условий и дополнительные действия
if result > 20:
    result = multiply(result, 2)
else:
    result = multiply(result, 3)

print("Результат: ", result)
