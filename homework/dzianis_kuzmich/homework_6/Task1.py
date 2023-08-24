# Запрос на ввод двух чисел от пользователя
number1 = float(input("Введите первое число: "))
number2 = float(input("Введите второе число: "))

# Умножение чисел
result = number1 * number2

# Проверка условий и дополнительные действия
if result > 20:
    result *= 2
else:
    result *= 3

# Вывод результата
print("Результат: ", result)
