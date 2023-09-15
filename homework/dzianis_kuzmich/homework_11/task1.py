# Step 1: Create a general Flower class
class Flower:
    def __init__(self, name, color, cost, life_time):
        self.name = name
        self.color = color
        self.cost = cost
        self.life_time = life_time  # in days


# Step 2: Create specific flower classes
class Rose(Flower):
    def __init__(self, color):
        super().__init__("Rose", color, 50, 7)


class Tulip(Flower):
    def __init__(self, color):
        super().__init__("Tulip", color, 35, 5)


class Daisy(Flower):
    def __init__(self, color):
        super().__init__("Daisy", color, 20, 4)


# Step 3: Create a Bouquet class
class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def total_cost(self):
        return sum(f.cost for f in self.flowers)

    def average_life_time(self):
        return sum(f.life_time for f in self.flowers) / len(self.flowers) if self.flowers else 0

    def find_by_life_time(self, life_time):
        return [f for f in self.flowers if f.life_time == life_time]


# Create some flower instances
rose = Rose("Red")
tulip = Tulip("Yellow")
daisy = Daisy("White")

# Create a Bouquet and add flowers to it
my_bouquet = Bouquet()
my_bouquet.add_flower(rose)
my_bouquet.add_flower(tulip)
my_bouquet.add_flower(daisy)

# Calculate the total cost and average lifetime of the bouquet
print("Total cost of bouquet:", my_bouquet.total_cost())
print("Average life time of bouquet:", my_bouquet.average_life_time(), "days")

# Find flowers by lifetime
print("Flowers with 5 days life time:", [f.name for f in my_bouquet.find_by_life_time(5)])
