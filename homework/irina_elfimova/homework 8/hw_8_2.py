temperatures = [
    20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24,
    23
]

hot_days = list(filter(lambda hot_day: hot_day > 28, temperatures))

max_t = max(hot_days)

min_t = min(hot_days)

avg = sum(hot_days) / len(hot_days)

print('самая высокая температура', max_t)

print('самая низкая температура', min_t)

print('средняя температура', int(avg))
