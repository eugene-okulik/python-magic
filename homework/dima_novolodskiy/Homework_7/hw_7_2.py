import sys

sys.set_int_max_str_digits(100000)


def fibonachi_func(number):
    list_number_fibonachi = [0, 1]
    # cycle_infinite = True
    while len(list_number_fibonachi) < number:
        list_number_fibonachi.append(list_number_fibonachi[-2] + list_number_fibonachi[-1])
        if len(list_number_fibonachi) == number:
            yield list_number_fibonachi[number - 1]


list_index_number = [5, 200, 1000, 100000]

for index_number in list_index_number:
    for result in fibonachi_func(index_number):
        print(result)
