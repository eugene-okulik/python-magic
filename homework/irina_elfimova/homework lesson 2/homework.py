from math import sqrt


# Даны 2 действительных числа a и b. Получить их сумму, разность и произведение

a = 5
b = 6
ab = a+b
ab2 = a-b
ab3 = a*b
print('Данны два числа, где a = 5, b = 6.', 'Сумма чисел:', ab, 'Разность чисел:', ab2, 'Произведение чисел:', ab3)


# Даны действительные числа x и y. Получить x − y / 1 + xy

x = 9
y = 11
z = x-y/1+x*y
print('Даны действительные числа x = 9 и y = 11', 'Решение: x − y / 1 + xy =', z)


# Даны два действительных числа. Найти среднее арифметическое и среднее геометрическое этих чисел

q = 15
w = 19
avr_arithm = (q+w)/2
avr_geomtr = sqrt(q*w)
print('Даны два числа 15 и 19, среднее арифметическое', avr_arithm, 'среднее геометрическое', avr_geomtr)


# Даны катеты прямоугольного треугольника. Найти его гипотенузу и площадь

a1 = 5
b1 = 6
c1 = sqrt(a1**2+b1**2)
S = 0.5*a1*b1
print('Даны катеты прямоугольного треугольника A = 5, B = 6.')
print('Гипотенуза равна:', c1, 'Площадь равна:', S)
