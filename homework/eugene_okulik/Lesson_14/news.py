# while True:
#     user_input = input('Say something: ')
#     if user_input == '':
#         break
#     else:
#         print(user_input)


while (user_input := input('say something: ')) != '':
    match user_input:
        case 'hello':
            print('hi')
        case 'bye':
            print('good bye')
        case _:
            print('Hi or bye?')

    # if user_input == 'hello':
    #     print('hi')
    # elif user_input == 'bye':
    #     print('good bye')
    # else:
    #     print('Hi or bye?')
