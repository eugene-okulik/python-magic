my_dict = {
    'tuple': (1, 2.4, True, 'Hello', [1, 2, 4]),
    'list': [1, 2.4, True, 'Hello', (1, 2, 3)],
    'dict': {1: True, 2: False, 3: 'Hello', 4: 5.4, 5: {1, 2, 3}},
    'set': {1, 2.4, True, 'Hello', (1, 2, 3)}
}
print(my_dict['tuple'][-1])
my_dict['list'].append(0.005)
my_dict['list'].pop(1)
my_dict['dict'][('i am a tuple',)] = True
del my_dict['dict'][2]
my_dict['set'].add(285)
my_dict['set'].remove(1)

print(my_dict)
