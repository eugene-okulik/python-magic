i = 0

while True:
    i += 1
    if i > 100:
        break
    if i % 3 == 0 and i % 5 == 0:
        c = 'FuzzBuzz'
        print(c)
        continue
    if i % 3 == 0:
        t = 'Fuzz'
        print(t)
        continue
    if i % 5 == 0:
        e = 'Buzz'
        print(e)
        continue
    else:
        print(i)
