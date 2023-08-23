number = 13

while True:
    user_number = int(input('Input number:'))
    if number == user_number:
        print('Congrats')
        break
    if number != user_number:
        print('Try again')
