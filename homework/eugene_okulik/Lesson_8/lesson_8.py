text = (
    'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. '
    + 'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'
)


words = text.split()


new_text = []
for word in words:
    # if word[-1] in ',.':
    #     word = word.replace(word[-1], f'ing{word[-1]}')
    # else:
    #     word = word + 'ing'
    # new_text.append(word)
    letters = word.rstrip(',.')
    symbols = word[len(letters):]
    new_text.append(f'{letters}ing{symbols}')
    # print(letters)
    # print(symbols)

print(' '.join(new_text))


# text = 'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. '
# for x in text.split():
#     print(x.lstrip('ne'))
