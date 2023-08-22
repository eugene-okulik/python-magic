text = 'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. ' \
       'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'


m_text = text.split()


s_text = []
for word in m_text:
    if ',' in word:
        word = word.replace(',', 'ing,')
    elif '.' in word:
        word = word.replace('.', 'ing.')
    else:
        word = word + 'ing'
    word = word + " "
    if word == 0:
        print(word)
    else:
        s_text.append(word)


str_text = ''.join(s_text)


print(str_text)
