cifr = 9
t_r = 0
while t_r != 1:
    vvod = int(input('Угадай цифру:'))
    if vvod != cifr:
        print('попробуй снова')
    else:
        t_r = 1
        print('Поздравляю! Вы угадали!')
