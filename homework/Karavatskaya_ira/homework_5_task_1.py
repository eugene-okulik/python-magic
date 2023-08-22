# напишите программу, которая добавляет 'ing' к словам (к каждому слову) в тексте:
# "Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, fasilisis vitae semper at,
# dignissim vitae libero" и после этого выводит получившийся текст на экран


my_str = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, fasilisis vitae semper '
          'at, dignissim vitae libero')
list_from_text = my_str.split()

word = list_from_text
print(word)

fin_text = []
for word in my_str.split():
    if word[-1] in ('.', ','):
        word = word.replace(word[-1], 'ing' + word[-1])
        fin_text.append(word)
    else:
        word = word.replace(word[-1], 'ing')
        fin_text.append(word)
new_str = ' '.join(fin_text)
print(new_str)
