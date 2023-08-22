i = 12

e = int(input('Welcome to "УГАДАЙКА!" please, enter your number: '))

while True:
    if i != e:
        print('попробуйте снова')
        e = int(input('your number: '))

    if i == e:
        print('Поздравляю! Вы угадали!')
        break
