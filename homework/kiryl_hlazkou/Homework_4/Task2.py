# a = 21 + 21
#
# b = 27 + 27
#
# print("Result is:", a)
#
# print("Result is:", b)
#
# c = [a, b]
#
# print(c)
#
# print(c[0] + 10)
#
# print(c[1] + 10)

result1 = 'Result is: 42'

result2 = 'Result is: 54'

word = 'is:'

len_word = len(word)

details_index = result1.index('is:') + len_word

print('Result 1 New:', int(result1[details_index:]) + 10)

print('Result 2 New:', int(result2[details_index:]) + 10)
