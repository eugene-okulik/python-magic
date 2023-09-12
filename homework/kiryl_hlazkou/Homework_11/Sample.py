class Flower:
    def __init__(self, name, color, stem_length, cost, average_lifetime):
        self.name = name
        self.color = color
        self.stem_length = stem_length
        self.cost = cost
        self.average_lifetime = average_lifetime

class Rose(Flower):
    def __init__(self, name, color, stem_length, cost, average_lifetime):
        super().__init__(name, color, stem_length, cost, average_lifetime)

class Lily(Flower):
    def __init__(self, color, stem_length, cost):
        super().__init__('Lily', color, stem_length, cost, 5)

class Tulip(Flower):
    def __init__(self, color, stem_length, cost):
        super().__init__('Tulip', color, stem_length, cost, 4)

class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def calculate_cost(self):
        return sum(flower.cost for flower in self.flowers)

    def calculate_wilting_time(self):
        if not self.flowers:
            return 0
        total_lifetime = sum(flower.average_lifetime for flower in self.flowers)
        return total_lifetime / len(self.flowers)

    def sort_by_freshness(self):
        self.flowers.sort(key=lambda flower: flower.average_lifetime, reverse=True)

    def sort_by_color(self):
        self.flowers.sort(key=lambda flower: flower.color)

    def sort_by_stem_length(self):
        self.flowers.sort(key=lambda flower: flower.stem_length, reverse=True)

    def sort_by_cost(self):
        self.flowers.sort(key=lambda flower: flower.cost, reverse=True)

    def search_by_lifetime(self, target_lifetime):
        return [flower for flower in self.flowers if flower.average_lifetime == target_lifetime]

# Create flower instances
rose1 = Rose('Rose', 'Red', 30, 5, 7)
rose2 = Rose('Rose', 'White', 25, 4, 7)
lily1 = Lily('Yellow', 35, 6)
lily2 = Lily('Pink', 40, 7)
tulip1 = Tulip('Red', 20, 3)

# Create a bouquet and add flowers
bouquet = Bouquet()
bouquet.add_flower(rose1)
bouquet.add_flower(rose2)
bouquet.add_flower(lily1)
bouquet.add_flower(lily2)
bouquet.add_flower(tulip1)

# Calculate bouquet cost and wilting time
print(f"Bouquet Cost: ${bouquet.calculate_cost()}")
print(f"Average Wilting Time: {bouquet.calculate_wilting_time()} days")

# Sort flowers by freshness and print
bouquet.sort_by_freshness()
print("Sorted by Freshness:")
for flower in bouquet.flowers:
    print(f"{flower.name} - Freshness: {flower.average_lifetime} days")

# Search for flowers with a specific lifetime
target_lifetime = 7
matching_flowers = bouquet.search_by_lifetime(target_lifetime)
print(f"Flowers with {target_lifetime} days of average lifetime:")
for flower in matching_flowers:
    print(f"{flower.name} - Freshness: {flower.average_lifetime} days")

for flower in bouquet.flowers:
    print(f'{flower.name}')

bouquet.sort_by_color()
print("Sorted by Color:")
for flower in bouquet.flowers:
    print(f"{flower.name} - Color: {flower.color}")