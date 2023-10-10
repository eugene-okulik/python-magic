# Создать классы цветов: общий класс для всех цветов и классы для нескольких видов.
# Создать экземпляры (объекты) цветов разных видов.
# Собрать букет (букет - еще один класс) с определением его стоимости. В букете цветы пусть хранятся в списке.
# Это будет список объектов.
# Для букета создать метод, который определяет время его увядания по среднему времени жизни всех цветов в букете.
# Позволить сортировку цветов в букете на основе различных параметров (свежесть/цвет/длина стебля/стоимость)
# (это тоже методы)
# Реализовать поиск цветов в букете по каким-нибудь параметрам (например, по среднему времени жизни)(и это тоже метод).


class Flower:
    def __init__(self, name, avg_life, freshness, color, length, price):
        self.name = name
        self.avg_life = avg_life  # in days
        self.freshness = freshness  # 'A' - fresh, 'B' - normal, 'C' - not fresh
        self.color = color
        self.length = length
        self.price = price  # in $


class Tulip(Flower):
    def __init__(self, avg_life, freshness, color, length, price):
        super().__init__("Tulip", avg_life, freshness, color, length, price)


class Rose(Flower):
    def __init__(self, avg_life, freshness, color, length, price):
        super().__init__("Rose", avg_life, freshness, color, length, price)


class Lily(Flower):
    def __init__(self, avg_life, freshness, color, length, price):
        super().__init__("Lily", avg_life, freshness, color, length, price)


class Cactus(Flower):
    def __init__(self, avg_life, freshness, color, length, price):
        super().__init__("Cactus", avg_life, freshness, color, length, price)


tulip = Tulip(10, 'A', 'orange', 30, 3)
tulip2 = Tulip(32, 'C', 'orange', 100, 15)
rose = Rose(20, 'B', 'scarlet', 30, 5)
rose2 = Rose(20, 'A', 'scarlet', 60, 10)
lily = Lily(2, 'C', 'scarlet', 20, 1)
lily2 = Lily(11, 'B', 'white', 23, 4)
cactus = Cactus(1000, 'A', 'green', 200, 201)


class Bouquet:
    def __init__(self, *flowers):
        self.flowers = list(flowers)  # цветы в букете хранятся в списке

    # Определение стоимости букета
    def price_bouquet(self):
        total_price = 0
        for flower0 in self.flowers:
            total_price += flower0.price
        print(f'The price of the bouquet is {total_price}$.')

    # Для букета создать метод, который определяет время его увядания по среднему времени жизни всех цветов в букете.
    def expiration_day(self):
        expire_in_days = []
        for flower1 in self.flowers:
            expire_in_days.append(flower1.avg_life)
        print(f'This bouquet will expire in {round(sum(expire_in_days) / len(expire_in_days))} days.')

    # Позволить сортировку цветов в букете на основе различных параметров - cвежесть
    def sort_by_freshness(self):
        #  The lambda function takes an 'item' as an argument
        #  and returns its 'freshness' attribute, which is used to compare the objects for sorting.
        #  The resulting sorted list is reordered in place,
        #  meaning the original list is updated with the new sorted order.
        self.flowers.sort(key=lambda item: item.freshness)
        return self.flowers

    # Позволить сортировку цветов в букете на основе различных параметров - цвет
    def sort_by_color(self):
        self.flowers.sort(key=lambda item: item.color)
        print('The colors are sorted in the alphabetic order:')
        for flower4 in self.flowers:
            print(f' - The FLOWER {flower4.name} has the {flower4.color} color in the bouquet')

    # Позволить сортировку цветов в букете на основе различных параметров - длина
    def sort_by_length(self):
        self.flowers.sort(key=lambda item: item.length)
        print('The lengths are sorted in the ASC order:')
        for flower3 in self.flowers:
            print(f' - The flower {flower3.name} has the length equals to {flower3.length} inches in the bouquet')

    # Позволить сортировку цветов в букете на основе различных параметров - цена
    def sort_by_price(self):
        self.flowers.sort(key=lambda item: item.price)
        print('The prices are sorted in the ASC order:')
        for flower2 in self.flowers:
            print(f' - The flower {flower2.name} has the price of {flower2.price}$ in the bouquet')

    # Реализовать поиск цветов в букете по каким-нибудь параметрам - цвет
    def search_by_any_parametr(self, word):
        matches = []
        for flower1 in self.flowers:
            if word in [flower1.color, flower1.length, flower1.avg_life, flower1.price]:
                matches.append(flower1.name)
        return matches


bouquet1 = Bouquet(tulip, lily, rose, lily2, rose2, tulip2, cactus)

bouquet1.price_bouquet()
bouquet1.expiration_day()
for flower in bouquet1.sort_by_freshness():
    print(f'{flower.name} has freshness = {flower.freshness}')
bouquet1.sort_by_color()
bouquet1.sort_by_length()
bouquet1.sort_by_price()
print(bouquet1.search_by_any_parametr(10))
