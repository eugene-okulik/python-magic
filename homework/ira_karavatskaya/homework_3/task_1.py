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































