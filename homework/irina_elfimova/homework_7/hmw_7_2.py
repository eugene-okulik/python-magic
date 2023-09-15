def febonachu_gen():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def febonachu_number(n):
    fib_gen = febonachu_gen()
    for _ in range(n):
        fib_number = next(fib_gen)
    return fib_number


print(febonachu_number(5))
print(febonachu_number(200))
print(febonachu_number(1000))
print(febonachu_number(100000))
