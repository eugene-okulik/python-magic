fis_param, sec_param = list(map(int, input().split()))


def mply(a, b):
    return a * b


result = mply(fis_param, sec_param)

if result > 20:
    print(mply(result, 2))
else:
    print(mply(result, 3))
