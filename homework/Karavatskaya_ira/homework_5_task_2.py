# нужно создать такую программу: Программа хранит какую-либо цифру в переменной.
# программа просит пользователя угадать какую-либо цифру
# пользователь вводит цифру
# программа сравнивает цифру с той, что храниться в переменной
# если цифры не равны - программа пишет "попробуй снова" и снова просит пользователя угадать цифру
# если пользователь угадывает цифру - программа пишет "Поздравляю! Вы угадали!" и завершается
# т.е. программа не завершится пока пользователь не угадает цифру


import random
random_value = random.randrange(0, 10)
print("Программа загадала число от 0 до 10")
print(random_value)

while True:
    choise = int(input("Введите число: "))
    if choise == random_value:
        print(input("Поздравляю! Вы угадали!"))
        break
    else:
        print("Попробуй снова")
