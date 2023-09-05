# Напишите функцию-генератор, которая генерирует список чисел фибоначчи.
# Распечатайте из этого списка пятое, двухсотое, тысячное и стотысячное число.


def fibonacci(limit):
    a, b = 0, 1
    yield a
    yield b
    count = 2
    while count < limit:
        a, b = b, a + b
        yield b
        count += 1


fib = fibonacci(100001)
fib_list = list(fib)

print(fib_list[4])
print(fib_list[199])
print(fib_list[999])
print(fib_list[99999])
