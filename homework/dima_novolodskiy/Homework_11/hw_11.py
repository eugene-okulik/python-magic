class Flower:

    def __init__(self, color, length, price, freshness, name):
        self.color = color
        self.length = length
        self.freshness = freshness
        self.price = price
        self.name = name


class Rose(Flower):
    tipe = 'Rose'


class Peonies(Flower):
    tipe = 'Peonies'


class Tulips(Flower):
    tipe = 'Tulips'


class Bouquet:

    def __init__(self, *args: object):
        self.args = list(args)
        self.price = self.total_price()
        self.freshness = self.total_freshness()

    def total_price(self):
        return sum([price_unit.price for price_unit in self.args])

    def total_freshness(self):
        total_fresh = []
        for fresh_unit in self.args:
            total_fresh.append(fresh_unit.freshness)
        return sum(total_fresh) / len(total_fresh)

    @property
    def sorted_price(self):
        set_price = [{'name': price_u.name, 'price': price_u.price} for price_u in self.args]

        def get_name(dictionary):
            return dictionary['price']

        return set_price.sort(key=get_name(set_price))

    def sorted_color(self):
        set_color = {color_u.name: color_u.color for color_u in self.args}
        sorted_name = []
        sorted_color = ['red']
        for key, value in set_color.items():
            if value >= max(sorted_color):
                sorted_name.append(key)
                sorted_color.append(value)
            else:
                sorted_name = [key] + sorted_name
                sorted_color.append(value)
        return sorted_name

    # def sorted_length(self):
    #     set_length = {length_u.name: length_u.length for length_u in self.args}
    #     sorted_name_length = []
    #     sorted_length = ['red']
    #     for key, value in set_length.items():
    #         if value >= max(sorted_length):
    #             sorted_name_length.append(key)
    #             sorted_length.append(value)
    #         else:
    #             sorted_name_length = [key] + sort
    #             sorted_length.append(value)
    #     return sort

    def sorted_freshness(self):
        return sorted([freshness_u.freshness for freshness_u in self.args])

    def flower_search(self, param):
        return [f'{flower_name.name} {flower_name.color}' for flower_name in self.args if
                flower_name.freshness == param]


rose_1 = Rose('red', 50, 120, 5, 'Красная роза 1')
rose_2 = Rose('yello', 40, 110, 4, 'Желтая роза 1')
rose_3 = Rose('white', 30, 100, 3, 'Белая роза 1')
peonies_1 = Peonies('white', 40, 250, 5, 'Белый пион 1')
peonies_2 = Peonies('lilac', 40, 320, 5, 'Лиловый пион 1')
peonies_3 = Peonies('pink', 40, 220, 5, 'Розовый пион 1')
tulips_1 = Tulips('red', 50, 90, 3, 'Красный тюльпан 1')
tulips_2 = Tulips('red', 50, 90, 3, 'Красный тюльпан 2')
tulips_3 = Tulips('red', 50, 90, 3, 'Красный тюльпан 3')

bouquet_1 = Bouquet(rose_1, rose_2, rose_3, peonies_1, peonies_2, peonies_3, tulips_1, tulips_2, tulips_3)

# print(bouquet_1.total_price())
# print(bouquet_1.total_freshness())
print(bouquet_1.sorted_price)
# print(bouquet_1.sorted_color())
# print(bouquet_1.sorted_length())
# print(bouquet_1.sorted_freshness())
# print(bouquet_1.flower_search(5))
