words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}

# Проходим по всем парам ключ-значение в словаре
for key, value in words.items():
    # Печатаем каждый ключ столько раз, сколько указано в его значении
    print(key * value)