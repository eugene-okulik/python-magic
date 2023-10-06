# Напишите функцию-генератор, которая генерирует список чисел фибоначчи
# Распечатайте из этого списка пятое число, двухсотое число, тысячное число, стотысячное число
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def fib_num(n):
    fib_gen = fib()
    fib_number = 0  # Initialize fib_number before the loop
    for _ in range(n):
        fib_number = next(fib_gen)
    return fib_number


print(fib_num(5))
print(fib_num(200))
print(fib_num(1000))
