import sys
def febonachu_gen(f_num):
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def fibonacci_number(n):
    fib_gen = febonachu_gen()
    for _ in range(n):
        fib_number = next(fib_gen)
    return fib_number

print(fibonacci_number(5))
print(fibonacci_number(200))
print(fibonacci_number(1000))
print(fibonacci_number(100000))

