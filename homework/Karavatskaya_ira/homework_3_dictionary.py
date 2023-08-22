my_dict = {'tuple': (2, 5, 8, None, 'text', True), 'list': [5, 6, False, 4.35, None], 'dict': {'key1': 'one',
                                                                                               'key2': '3',
                                                                                               'key3': 'True',
                                                                                               'key4': '5',
                                                                                               'key5': 'two'},
           'set': {5, 8, 6, True, None}}

print('Full dictionary:', my_dict)

# выводим последний элемент кортежа my tuple


print(my_dict['tuple'][-1])

# добавляем в конец списка 'list' элемент None

my_dict['list'].append(None)
print('add element "None" to the end of the list:', my_dict['list'])

# удаляем второй элемент списка 'list'

my_dict['list'].pop((1))
print(my_dict['list'])

# добавляем элемент с ключом 'i am a tuple' любым значением

my_dict["dict"][('i am a tuple',)] = "any_value"
my_dict["dict"].pop("key1")

# удаляем элемент

print(my_dict.items())

# добавляем новый элемент 'True' во множество 'set'

my_dict['set'].add(33)
print(my_dict['set'])

# удаляем элемент '5' из множества 'set'

my_dict['set']. remove(5)
print(my_dict['set'])

# выводим на экран весь словарь


print('my_dict')
