class Flower:

    def __init__(self, color, length, price, freshness):
        self.color = color
        self.length = length
        self.freshness = freshness
        self.price = price


class Rose(Flower):
    name = 'Rose'


class Peonies(Flower):
    name = 'Peonies'


class Tulips(Flower):
    name = 'Tulips'


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

    def sorted_price(self):
        return sorted([price_u.price for price_u in self.args])

    def sorted_color(self):
        return sorted([color_u.color for color_u in self.args])

    def sorted_length(self):
        return sorted([length_u.length for length_u in self.args])

    def sorted_freshness(self):
        return sorted([freshness_u.freshness for freshness_u in self.args])

    def flower_search(self, param):
        return [f'{flower_name.name} {flower_name.color}' for flower_name in self.args if
                flower_name.freshness == param]


rose_1 = Rose('red', 50, 120, 5)
rose_2 = Rose('yello', 40, 110, 4)
rose_3 = Rose('white', 30, 100, 3)
peonies_1 = Peonies('white', 40, 250, 5)
peonies_2 = Peonies('lilac', 40, 320, 5)
peonies_3 = Peonies('pink', 40, 220, 5)
tulips_1 = Tulips('red', 50, 90, 3)
tulips_2 = Tulips('red', 50, 90, 3)
tulips_3 = Tulips('red', 50, 90, 3)

bouquet_1 = Bouquet(rose_1, rose_2, rose_3, peonies_1, peonies_2, peonies_3, tulips_1, tulips_2, tulips_3)

print(bouquet_1.total_price())
print(bouquet_1.total_freshness())
print(bouquet_1.sorted_price())
print(bouquet_1.sorted_freshness())
print(bouquet_1.sorted_color())
print(bouquet_1.sorted_length())
print(bouquet_1.flower_search(5))
