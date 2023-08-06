my_dict = {'tuple': (7, None, 'text', False, 2.42), 'list': [8, None, 'text', True, 3.42],
           'dict': {'key1': '9', 'key2': 'None', 'key3': 'text', 'key4': 'False', 'key5': '4.42'},
           'set': {10, None, 'text', True, 5.42}}

print('Full dictionary:', my_dict)

print('Last element in tuple:', my_dict['tuple'][4])

my_dict['list'].append(5)

print('Add element "5" to the end of the list:', my_dict['list'])

my_dict['list'].pop(1)

print('Remove second element from the list:', my_dict['list'])

my_dict['dict']['i am a tuple'] = 'False'

print('Add element "i am a tuple":', my_dict['dict'])

my_dict['dict'].pop('key1')

print('Remove element key1:', my_dict['dict'])

my_dict['set'].add('Hello World')

print('Add new element to the set:', my_dict['set'])

my_dict['set'].remove('text')

print('Remove element from set:', my_dict['set'])

print('Full dictionary with all changes applied:', my_dict)
