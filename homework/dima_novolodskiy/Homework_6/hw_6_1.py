fis_param, sec_param = list(map(int, input().split()))


def pr_function(fist, second):
    rez = fist * second
    if rez > 20:
        rez *= 2
    else:
        rez *= 3
    return rez


print(pr_function(fis_param, sec_param))
