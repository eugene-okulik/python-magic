# Задание №1
# Напишите программу, которая добавляет ‘ing’ к словам (к каждому слову) в тексте “Etiam tincidunt neque erat, quis
# molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, dignissim vitae libero”
# и после этого выводит получившийся текст на экран.

text = 'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, ' \
       'dignissim vitae libero.'

new_text = []

words = text.split()

for word in words:
    if word[-1] == ',':
        word = word.replace(word[-1], 'ing,')
        new_text.append(word)
    elif word[-1] == '.':
        word = word.replace(word[-1], 'ing.')
        new_text.append(word)
    else:
        word = word+'ing'
        new_text.append(word)

print(' '.join(new_text))
