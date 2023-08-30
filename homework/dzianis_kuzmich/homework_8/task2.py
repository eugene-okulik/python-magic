# List of temperatures
temperatures = [
    20, 15, 32, 34, 21, 19, 25, 27, 30, 32,
    34, 30, 29, 25, 27, 22, 22, 23, 25, 29,
    29, 31, 33, 31, 30, 32, 30, 28, 24, 23
]

# Filter out hot days using filter function
hot_days = list(filter(lambda x: x > 28, temperatures))

# Print the results
print(f"Список жарких дней: {hot_days}")
print(f"Максимальная температура: {max(hot_days)}")
print(f"Минимальная температура: {min(hot_days)}")
print(f"Средняя температура: {sum(hot_days) / len(hot_days)}")
