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
        self.args = args
        self.total_price = total_price
    def list_flowers(self):
        lst = list(self.args)
        return lst



1. Создать классы цветов: общий класс для всех цветов и классы для нескольких видов. 
2. Создать экземпляры (объекты) цветов разных видов.
3. Собрать букет (букет - еще один класс) с определением его стоимости. 
    В букете цветы пусть хранятся в списке. 
    Это будет список объектов.
4. Для букета создать метод, который определяет время его увядания по среднему времени жизни всех цветов в букете.
5. Позволить сортировку цветов в букете на основе различных параметров (свежесть/цвет/длина стебля/стоимость)(это тоже методы)
6. Реализовать поиск цветов в букете по каким-нибудь параметрам (например, по среднему времени жизни) (и это тоже метод).


rose_1 = Rose('red', 50, 120, 5)
rose_2 = Rose('yello', 40, 110, 4)
rose_3 = Rose('white', 30, 100, 3)
peonies_1 = Peonies('white', 40, 250, 5)
peonies_2 = Peonies('lilac', 40, 320, 5)
peonies_3 = Peonies('pink', 40, 220, 5)
tulips_1 = Tulips('red', 50, 90, 2)
tulips_2 = Tulips('red', 50, 90, 2)
tulips_3 = Tulips('red', 50, 90, 2)

bouquet = Bouquet(rose_1, rose_2, rose_3, peonies_1, peonies_2, peonies_3, tulips_1, tulips_2, tulips_3)

print(bouquet.list_flowers()[0].color)
