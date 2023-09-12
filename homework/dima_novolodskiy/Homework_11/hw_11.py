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
        self.args = args
        self.price_b = self.price_b()
        self.freshness_b = self.freshness_b()
        self.sorted_price = self.sorted_price_flower()
        self.sorted_color = self.sorted_color_flower
        self.sorted_length = self.sorted_length_flower
        self.sorted_freshness = self.sorted_freshness_flower

    def price_b(self):
        total = sum([price_unit.price for price_unit in self.args])
        return total

    def freshness_b(self):
        total_fresh = []
        for fresh_unit in self.args:
            total_fresh.append(fresh_unit.freshness)
        return f'{sum(total_fresh) / len(total_fresh)}'

    def sorted_price_flower(self):
        price_dict = {price_u.name: price_u.price for price_u in self.args}
        sorted_p = dict(sorted(price_dict.items(), key=lambda item: item[1]))
        return [flower for flower in sorted_p]

    def sorted_color_flower(self):
        color_dict = {color_u.name: color_u.color for color_u in self.args}
        sorted_color = dict(sorted(color_dict.items(), key=lambda item: item[1]))
        return [flower for flower in sorted_color]

    def sorted_length_flower(self):
        length_dict = {length_u.name: length_u.length for length_u in self.args}
        sorted_length = dict(sorted(length_dict.items(), key=lambda item: item[1]))
        return [flower for flower in sorted_length]

    def sorted_freshness_flower(self):
        freshness_dict = {freshness_u.name: freshness_u.freshness for freshness_u in self.args}
        sorted_freshness = dict(sorted(freshness_dict.items(), key=lambda item: item[1]))
        return [flower for flower in sorted_freshness]

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

print(bouquet_1.sorted_price)
print(bouquet_1.sorted_color())
print(bouquet_1.sorted_length())
print(bouquet_1.sorted_freshness())
print(bouquet_1.flower_search(5))
