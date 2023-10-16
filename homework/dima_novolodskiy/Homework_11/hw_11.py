class Flower:

    def __init__(self, color, length, price, freshness):
        self.color = color
        self.length = length
        self.freshness = freshness
        self.price = price


class Rose(Flower):
    type = 'Rose'


class Peonies(Flower):
    type = 'Peonies'


class Tulips(Flower):
    type = 'Tulips'


class Bouquet:

    def __init__(self, *args: object):
        self.args = args

    def price_b(self):
        total = sum([price_unit.price for price_unit in self.args])
        return total

    def freshness_b(self):
        total_fresh = []
        for fresh_unit in self.args:
            total_fresh.append(fresh_unit.freshness)
        return f'{sum(total_fresh) / len(total_fresh)}'

    def sorted_price(self):
        price_dict = {price_u: price_u.price for price_u in self.args}
        sorted_price = sorted(price_dict.items(), key=lambda item: item[1])
        ret = [flower[0] for flower in sorted_price]
        return ret

    def sorted_color(self):
        color_dict = {color_u: color_u.color for color_u in self.args}
        sorted_color = sorted(color_dict.items(), key=lambda item: item[1])
        return [flower[0] for flower in sorted_color]

    def sorted_length(self):
        length_dict = {length_u: length_u.length for length_u in self.args}
        sorted_length = sorted(length_dict.items(), key=lambda item: item[1])
        return [flower[0] for flower in sorted_length]

    def sorted_freshness(self):
        freshness_dict = {freshness_u: freshness_u.freshness for freshness_u in self.args}
        sorted_freshness = sorted(freshness_dict.items(), key=lambda item: item[1])
        return [flower[0] for flower in sorted_freshness]

    def flower_search(self, param):
        return [flower_name for flower_name in self.args if
                flower_name.freshness == param]


rose_1 = Rose('red', 50, 120, 5)
rose_2 = Rose('yello', 40, 110, 4)
peonies_1 = Peonies('white', 40, 250, 5)
peonies_2 = Peonies('lilac', 40, 320, 5)
tulips_1 = Tulips('red', 50, 90, 3)
tulips_2 = Tulips('yello', 50, 90, 3)

bouquet_1 = Bouquet(rose_1, rose_2, peonies_1, peonies_2, tulips_1, tulips_2)

print(bouquet_1.price_b())
print(bouquet_1.sorted_price())
print(bouquet_1.sorted_color())
print(bouquet_1.sorted_length())
print(bouquet_1.sorted_freshness())
print(bouquet_1.flower_search(5))
