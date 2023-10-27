class Flowers:
    def __init__(self, name, stem_length, color, price, lifetime):
        self.name = name
        self.lifetime = lifetime
        self.color = color
        self.stem_length = stem_length
        self.price = price


class Rose(Flowers):
    def __init__(self, stem_length, color, price, lifetime):
        super().__init__('Роза', stem_length, color, price, lifetime)


class Tulip(Flowers):
    def __init__(self, stem_length, color, price, lifetime):
        super().__init__('Тюльпан', stem_length, color, price, lifetime)


class Chamomile(Flowers):
    def __init__(self, stem_length, color, price, lifetime):
        super().__init__('Ромашка', stem_length, color, price, lifetime)


flower_1 = Rose(20, 'red', 1000, 7)
flower_2 = Chamomile(18, 'white', 800, 5)
flower_3 = Rose(21, 'red', 1500, 6)
flower_4 = Tulip(15, 'orange', 900, 5)
flower_5 = Tulip(16, 'purple', 1200, 7)
flower_6 = Chamomile(15, 'white', 900, 5)
flowers = [flower_1, flower_2, flower_3, flower_4, flower_5, flower_6]


class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def calculate_cost(self):
        cost = 0
        for flower in self.flowers:
            cost += flower.price
        return cost

    def average_lifetime(self):
        total_lifetime = 0
        for flower in self.flowers:
            total_lifetime += flower.lifetime
        return total_lifetime / len(self.flowers)

    def sort_by_lifetime(self):
        self.flowers.sort(key=lambda flower: flower.lifetime)

    def sort_by_color(self):
        self.flowers.sort(key=lambda flower: flower.color)

    def sort_by_stem_length(self):
        self.flowers.sort(key=lambda flower: flower.stem_length)

    def sort_by_price(self):
        self.flowers.sort(key=lambda flower: flower.price)

    def search_colors(self, word):
        matches = []
        for flower1 in self.flowers:
            if word in [flower1.color, flower1.stem_length, flower1.lifetime, flower1.price]:
                matches.append(flower1.name)
        return matches


bouquet = Bouquet()
bouquet.add_flower(flower_1)
bouquet.add_flower(flower_5)
bouquet.add_flower(flower_6)


print("Стоимость букета:", bouquet.calculate_cost())

print("Среднее время жизни букета:", int(bouquet.average_lifetime()), 'дней')

print('Сортировка:')

bouquet.sort_by_lifetime()
print("По свежести:", [flower.name for flower in bouquet.flowers])

bouquet.sort_by_color()
print("По цвету:", [flower.name for flower in bouquet.flowers])

bouquet.sort_by_stem_length()
print("По длине стебля:", [flower.name for flower in bouquet.flowers])

bouquet.sort_by_price()
print("По цене:", [flower.name for flower in bouquet.flowers])

print(bouquet.search_colors('purple'))
