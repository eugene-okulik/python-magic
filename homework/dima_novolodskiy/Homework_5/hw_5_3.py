for chislo in range(1, 101):
    if chislo % 3 == 0 and chislo % 5 == 0:
        print('FuzzBuzz')
    elif chislo % 5 == 0:
        print('Buzz')
    elif chislo % 3 == 0:
        print('Fuzz')
    else:
        print(chislo)