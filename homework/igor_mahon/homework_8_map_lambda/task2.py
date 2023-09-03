# Map, filter
# Есть такой список:
# temperatures = [
# 20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23
# ]
# С помощью функции map или filter создайте из этого списка новый список с жаркими днями.
# Будем считать жарким всё, что выше 28.
#
# Распечатайте из нового списка самую высокую температуру самую низкую и среднюю.

from statistics import mean

temperatures = [
    20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24,
    23
]

hot_days = list(filter(lambda hot_day: hot_day > 28, temperatures))

max_temp = max(hot_days)

print(max_temp)

min_temp = min(hot_days)

print(min_temp)

avg_temp = round(mean(hot_days))

print(avg_temp)
