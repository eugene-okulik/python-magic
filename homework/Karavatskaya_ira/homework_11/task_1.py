# Создать классы цветов:
# общий класс для всех цветов и классы для нескольких видов.
# Создать экземпляры (объекты) цветов разных видов.
# Собрать букет (букет - еще один класс) с определением его стоимости.
# В букете цветы пусть хранятся в списке. Это будет список объектов.
# Для букета создать метод, который определяет время его увядания по среднему времени жизни всех цветов в букете.
# Позволить сортировку цветов в букете на основе различных параметров
# (свежесть/цвет/длина стебля/стоимость)(это тоже методы)
# Реализовать поиск цветов в букете по каким-нибудь параметрам
# (например, по среднему времени жизни) (и это тоже метод).


class Flower:
    def __init__(self, name, freshness, color, stem_length, price):
        self.name = name
        self.freshness = freshness
        self.color = color
        self.stem_length = stem_length
        self.price = price


class Rose(Flower):
    def __init__(self, freshness, color, stem_length, price):
        super().__init__("Rose", freshness, color, stem_length, price)


class Lily(Flower):
    def __init__(self, freshness, color, stem_length, price):
        super().__init__("Lily", freshness, color, stem_length, price)


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

    def average_lifespan(self):
        total_lifespan = 0
        for flower in self.flowers:
            total_lifespan += flower.freshness
        return total_lifespan / len(self.flowers)

    def sort_by_freshness(self):
        self.flowers.sort(key=lambda flower: flower.freshness)

    def sort_by_color(self):
        self.flowers.sort(key=lambda flower: flower.color)

    def sort_by_stem_length(self):
        self.flowers.sort(key=lambda flower: flower.stem_length)

    def sort_by_price(self):
        self.flowers.sort(key=lambda flower: flower.price)

    def search_by_lifespan(self, lifespan):
        result = []
        for flower in self.flowers:
            if flower.freshness >= lifespan:
                result.append(flower)
        return result


# Пример использования:
rose1 = Rose(5, "Red", 10, 25)
rose2 = Rose(3, "Pink", 12, 20)
lily1 = Lily(4, "White", 15, 30)

bouquet = Bouquet()
bouquet.add_flower(rose1)
bouquet.add_flower(rose2)
bouquet.add_flower(lily1)

print("Bouquet cost:", bouquet.calculate_cost())

average_lifespan = bouquet.average_lifespan()
print("Average lifespan:", average_lifespan)

bouquet.sort_by_freshness()
print("Sorted by freshness:", [flower.name for flower in bouquet.flowers])

bouquet.sort_by_color()
print("Sorted by color:", [flower.name for flower in bouquet.flowers])

bouquet.sort_by_stem_length()
print("Sorted by stem length:", [flower.name for flower in bouquet.flowers])

bouquet.sort_by_price()
print("Sorted by price:", [flower.name for flower in bouquet.flowers])

search_result = bouquet.search_by_lifespan(4)
print("Search result (lifespan >= 4):", [flower.name for flower in search_result])
