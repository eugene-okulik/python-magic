words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}


def new_dict(new):

    for k, v in new.items():
        print(k * v)


new_dict(words)
