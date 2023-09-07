import random


class Flowers:
    def __int__(self, name, stem_length, color, price, lifetime):
        self.name = name
        self.stem_length = stem_length
        self.color = color
        self.price = price
        self.lifetime = lifetime


class Rose(Flowers):

    def __init__(
            self, name, stem_length, color, price, lifetime, luxury
    ):
        super().__init__(name, stem_length, color, price, lifetime)
        self.luxury = luxury


class Chamomile(Flowers):
    def __init__(
            self, name, stem_length, color, price, lifetime, flavour
    ):
        super().__init__(name, stem_length, color, price, lifetime)
        self.flavour = flavour


class Tulip(Flowers):
    def __init__(
            self, name, stem_length, color, price, lifetime, subspecies
    ):
        super().__init__(name, stem_length, color, price, lifetime)
        self.subspecies = subspecies


flower_1 = Rose('Vine Rose', '20 cm', 'Red', 1000, 7, 'High Luxury')
flower_2 = Chamomile('Bride White', '18 cm', 'White', 800, 5, 'Bride')
flower_3 = Rose('Dark Rose', '21 cm', 'Dark Red', 1500, 6, 'High Luxury')
flower_4 = Tulip('Amsterdam', '15 cm', 'Orange', 900, 5, 'Amsterdam Tulip')
flower_5 = Tulip('Purple Prince', '16 cm', 'Purple', 1200, 7, 'Early Tulips')
flower_6 = Chamomile('Cladanthus mixtus', '15 cm', 'White', 900, 5, 'Moroccan chamomile')

class Bouquet(Flowers):
    def __init__(
            self, name, stem_length, color, price, lifetime,
    ):
        super().__init__(name, stem_length, color, price, lifetime)
    flowers = [flower_1, flower_2, flower_3, flower_4, flower_5, flower_6]
    n = 3
    custom_bouquet = random.choice(flowers, n)
    def lifetime_sort(self):
        avg_lifetime = flowers.lifetime / 6



