
my_dict = {'tuple': (1, 2, 3, 4, 5), 'list': ['a', 'b', 'c', 'd', 'e'],
           'dict': {'A': 'aa', 'B': 'ab', 'C': 'ac', 'D': 'ad', 'E': 'ae'}, 'set': {9, 8, 7, 6, 77}}


# ‘tuple’. Для того, что хранится под ключом ‘tuple’:
# выведите на экран последний элемент

my_tuple = my_dict['tuple']
print(my_tuple[-1])

# ‘list’ добавьте в конец списка еще один элемент
# удалите второй элемент списка

my_list = my_dict['list']
my_list.append('f')
print(my_list)
pooped = my_list.pop(1)
print(my_list)

# ‘dict’ добавьте элемент с ключом ('i am a tuple',) и любым значением
# удалите какой-нибудь элемент

dict_my = my_dict['dict']
dict_my['i am a tuple'] = 'af'
print(dict_my)
dict_my.pop('D')
print(dict_my)

# ‘set’ добавьте новый элемент в множество
# удалите элемент из множества

my_set = my_dict['set']
my_set.add(88)
print(my_set)
my_set.discard(77)
print(my_set)



