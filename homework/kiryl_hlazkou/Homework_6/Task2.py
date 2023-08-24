words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}


def dictionary(new_dict):
    for key, value in new_dict.items():
        print(key * value)


dictionary(words)
