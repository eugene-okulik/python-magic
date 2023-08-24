# Задание 2
# Напишите функцию-генератор, которая генерирует список чисел фибоначчи
# Распечатайте из этого списка пятое число, двухсотое число, тысячное число, стотысячное число

def list_fib():
    a = 0
    b = 1
    while True:
        yield a
        temp_var = a
        a = b
        b = temp_var + b


count = 0
for number in list_fib():
    if count == 4 or count == 199 or count == 999 or count == 99999:
        print(number)
    if count > 100000:
        break
    count += 1
