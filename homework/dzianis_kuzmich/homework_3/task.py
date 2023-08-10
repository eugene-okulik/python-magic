my_dict = {
    'tuple': (1, 2, 3, 4, 5),
    'list': [10, 20, 30, 40, 50],
    'dict': {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5
    },
    'set': {100, 200, 300, 400, 500}
}
# Для кортежа
print(my_dict['tuple'][-1])

# Для списка
my_dict['list'].append(60)
del my_dict['list'][1]

# Для словаря
my_dict['dict'][('i am a tuple',)] = 'value'
del my_dict['dict']['a']

# Для множества
my_dict['set'].add(600)
my_dict['set'].remove(100)

print(my_dict)
