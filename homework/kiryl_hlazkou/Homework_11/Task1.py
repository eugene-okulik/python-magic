class Flower:
    def __init__(self, name, color, stem_length, cost, average_lifetime):
        self.name = name
        self.color = color
        self.stem_length = stem_length
        self.cost = cost
        self.average_lifetime = average_lifetime


class Rose(Flower):
    def __init__(self, color, stem_length, cost):
        super().__init__('Rose', color, stem_length, cost, 7)


class Lily(Flower):
    def __init__(self, color, stem_length, cost):
        super().__init__('Lily', color, stem_length, cost, 5)


class Tulip(Flower):
    def __init__(self, color, stem_length, cost):
        super().__init__('Tulip', color, stem_length, cost, 4)


class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flow):
        self.flowers.append(flow)

    def calculate_cost(self):
        return sum(flow.cost for flow in self.flowers)

    def calculate_wilting_time(self):
        if not self.flowers:
            return 0
        total_lifetime = sum(flow.average_lifetime for flow in self.flowers)
        return total_lifetime / len(self.flowers)

    def sort_by_freshness(self):
        self.flowers.sort(key=lambda flow: flow.average_lifetime, reverse=True)

    def sort_by_color(self):
        self.flowers.sort(key=lambda flow: flow.color)

    def sort_by_stem_length(self):
        self.flowers.sort(key=lambda flow: flow.stem_length, reverse=True)

    def sort_by_cost(self):
        self.flowers.sort(key=lambda flow: flow.cost, reverse=True)

    def search_by_lifetime(self, lifetime):
        return [flow for flow in self.flowers if flow.average_lifetime == lifetime]


rose1 = Rose('Red', 30, 5)
rose2 = Rose('White', 25, 4)
lily1 = Lily('Yellow', 35, 6)
lily2 = Lily('Pink', 40, 7)
tulip1 = Tulip('Orange', 20, 3)

bouquet = Bouquet()
bouquet.add_flower(rose1)
bouquet.add_flower(rose2)
bouquet.add_flower(lily1)
bouquet.add_flower(lily2)
bouquet.add_flower(tulip1)

print(f"Bouquet Cost: ${bouquet.calculate_cost()}")
print(f"Average Wilting Time: {bouquet.calculate_wilting_time()} days")

bouquet.sort_by_freshness()
print("Sorted by Freshness:")
for flower in bouquet.flowers:
    print(f"{flower.name} - Freshness: {flower.average_lifetime} days")

target_lifetime = 7
matching_flowers = bouquet.search_by_lifetime(target_lifetime)
print(f"Flowers with {target_lifetime} days of average lifetime:")
for flower in matching_flowers:
    print(f"{flower.name} - Freshness: {flower.average_lifetime} days")

# Задание
# Создать классы цветов: общий класс для всех цветов и классы для нескольких видов. Создать экземпляры (объекты)
# цветов разных видов. Собрать букет (букет - еще один класс) с определением его стоимости. В букете цветы
# пусть хранятся в списке. Это будет список объектов.
#
# Для букета создать метод, который определяет время его увядания по среднему времени жизни всех цветов в
# букете.
#
# Позволить сортировку цветов в букете на основе различных параметров (свежесть/цвет/длина стебля/стоимость)
# (это тоже методы)

# Реализовать поиск цветов в букете по каким-нибудь параметрам (например, по среднему времени жизни)
# (и это тоже метод).
