# Создайте такую программу:
# пользователь вводит два числа.
# Программа умножает одно число на другое.
# Если результат этого умножения больше 20, то этот результат умножается на 2.
# Если результат изначального умножения меньше или равно 20, то он умножается на 3.


numb_1 = int(input('Введите первое число: '))
print(type(numb_1))

numb_2 = int(input('Введите второе число: '))
print(type(numb_2))

main_numb = numb_1 * numb_2
print(('Произведение введенных чисел:', numb_1 * numb_2))


def multiply(main_numb):
    if main_numb > 20:
        print(main_numb * 2)
    elif main_numb <= 20:
        print(main_numb * 3)


multiply(main_numb)
