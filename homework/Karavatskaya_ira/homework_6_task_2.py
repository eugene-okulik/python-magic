# Дан такой словарь:
# words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}
# Выведите на экран каждый ключ столько раз, сколько указано в значении.
# Т.е. как-то так:
# III
# lovelovelovelove
# Cделайте так, чтобы каждый ключ печатался в одной строке (как в примере)


words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}


def dict_new(variable):
    for key, value in variable.items():
        print(key * value)


dict_new(words)
