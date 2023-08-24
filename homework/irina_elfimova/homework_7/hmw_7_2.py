def febonachu_num(f_num):
    a, b = 0, 1
    for i in range(f_num):
        yield a
        a, b = b, a + b


c = list(febonachu_num(100000))

print(c[4])
print(c[199])
print(c[999])
print(c[99999])
