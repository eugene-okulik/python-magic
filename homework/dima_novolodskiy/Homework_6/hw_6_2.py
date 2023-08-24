words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}


def dict_word(dict_in: object):
    for key, values in dict_in.items():
        print(key * values)


dict_word(words)
