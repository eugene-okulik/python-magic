text = 'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at,' \
       'dignissim vitae libero.'

new_text = []

words = text.split()

print(words)
for word in words:
    if word[-1] in ('.', ','):
        word = word.replace(word[-1], 'ing' + word[-1])
        print(word)
        new_text.append(word)
    else:
        word = word + 'ing'
        new_text.append(word)
print(' '.join(new_text))