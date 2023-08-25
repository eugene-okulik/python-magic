# Напишите функцию-генератор, которая генерирует список чисел фибоначчи.
# Распечатайте из этого списка пятое, двухсотое, тысячное и стотысячное число.

def fibonacci_list(f_num):
    f1 = 1
    f2 = 1
    for i in range(f_num):
        yield f1
        f1, f2 = f2, f1 + f2


fib_list = list(fibonacci_list(100000))

print(fib_list[4])
print(fib_list[199])
print(fib_list[999])
print(fib_list[99999])
