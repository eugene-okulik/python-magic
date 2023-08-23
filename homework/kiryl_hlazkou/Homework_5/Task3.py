i = 0

while i < 100:
    i += 1
    if i % 3 == 0 and i % 5 == 0:
        print('FuzzBuzz')
    elif i % 3 == 0:
        print('Fuzz')
        continue
    elif i % 5 == 0:
        print('Buzz')
        continue
    else:
        print(i)
