import sys

# Increase the limit for integer string conversion.
sys.set_int_max_str_digits(500000)  # A large enough value to handle the 100000th Fibonacci number.

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def get_fibonacci_number(n):
    fib_gen = fibonacci_generator()
    for _ in range(n):
        fib_number = next(fib_gen)
    return fib_number

# Get the 5th Fibonacci number
print("5th Fibonacci number:", get_fibonacci_number(5))

# Get the 200th Fibonacci number
print("200th Fibonacci number:", get_fibonacci_number(200))

# Get the 1000th Fibonacci number
print("1000th Fibonacci number:", get_fibonacci_number(1000))

# Get the 100000th Fibonacci number
print("100000th Fibonacci number:", get_fibonacci_number(100000))
