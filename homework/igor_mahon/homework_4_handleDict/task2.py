# Задание 2
# Допустим, какая-то программа возвращает результат своей работы в таком виде:
# результат операции: 42
# результат операции: 54
# С помощью срезов и метода index получите из каждой строки с результатом число, прибавьте к полученному числу 10,
# результат сложения распечатайте.

result_one = "результат операции: 42"
result_two = "результат операции: 54"

phrase = "операции: "
len_phrase = len(phrase)

details_result_index1 = result_one.lower().index("операции: ") + len_phrase
details_result_index2 = result_two.lower().index("операции: ") + len_phrase

print(int(result_one[details_result_index1:]) + 10)
print(int(result_two[details_result_index2:]) + 10)
