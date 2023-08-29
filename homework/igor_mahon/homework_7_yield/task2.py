# Задание 2
# Напишите функцию-генератор, которая генерирует список чисел фибоначчи
# Распечатайте из этого списка пятое число, двухсотое число, тысячное число, стотысячное число

import sys

sys.set_int_max_str_digits(0)  # This resolved the issue - ValueError: Exceeds the limit (4300) for integer string...


def list_fib():
    a = 0
    b = 1
    while True:
        yield a
        temp_var = a
        a = b
        b = temp_var + b


count = 1
for number in list_fib():
    if count in [5, 200, 1000, 100000]:
        print(number)
    if count > 100000:
        break
    count += 1
