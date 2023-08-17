value_a = 'результат операции: 42'
value_b = 'результат операции: 54'
word = 'результат операции: '
len_word = len(word)
index_true_a = value_a.index('результат операции: ') + len_word
index_true_b = value_b.index('результат операции: ') + len_word
print(int(value_a[index_true_a:]) + 10)
print(int(value_b[index_true_b:]) + 10)

# Мой вариант
# print(int(value_a.split()[value_a.split().index('42')]) + 10)
# print(int(value_b.split()[value_b.split().index('54')]) + 10)
