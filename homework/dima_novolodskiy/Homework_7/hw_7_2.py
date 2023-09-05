def fibonachi_func(number):
    a = 0
    b = 1
    count = 2
    while count != number:
        a, b = b, a + b
        count += 1
        if count == number:
            yield b


list_index_number = [5, 200, 1000, 100000]

for index_number in list_index_number:
    for result in fibonachi_func(index_number):
        print(result)
