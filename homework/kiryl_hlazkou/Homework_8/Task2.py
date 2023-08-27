from statistics import mean

temperature = (
    [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, +
     30, 28, 24, 23]
)

#
# new_temp = []
#
# for t in temperature:
#     if t >= 28:
#         new_temp.append(t)
#
# print(new_temp)


def high(t):
    return t >= 28


new_temp = list(filter(high, temperature))

print(min(new_temp))

print(max(new_temp))

print(round(mean(new_temp)))

# С помощью функции map или filter создайте из этого списка новый список с жаркими днями. Будем считать жарким всё,
# что выше 28.
# Распечатайте из нового списка самую высокую температуру самую низкую и среднюю.
