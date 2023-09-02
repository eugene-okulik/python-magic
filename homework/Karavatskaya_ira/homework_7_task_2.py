# Напишите функцию-генератор, которая генерирует список чисел фибоначчи.
# Распечатайте из этого списка пятое, двухсотое, тысячное и стотысячное число.


def fibonacci_generator():
    a, b = 0, 1

    while True:
        yield a
        a, b = b, a + b


fibonacci_numbers = []
generator = fibonacci_generator()
for i in range(100001):
    fibonacci_numbers.append(next(generator))

print(fibonacci_numbers[4])
print(fibonacci_numbers[199])
print(fibonacci_numbers[999])
print(fibonacci_numbers[99999])
