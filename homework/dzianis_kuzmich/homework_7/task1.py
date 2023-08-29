import random


# Function to decide whether to give a bonus or not. The decision is made randomly.
def get_bonus_status():
    return random.choice([True, False])


# Function to generate a random bonus amount based on the salary
def get_bonus_amount(salary):
    # Generate a random bonus amount between 1% to 10% of the salary and convert to integer
    return int(salary * random.uniform(0.01, 0.1))


# Ask the user for their salary and convert it to an integer
salary = int(input("Please enter your salary: "))

# Decide whether to give a bonus
bonus = get_bonus_status()

# Create a new variable to store the final salary
final_salary = salary

# If bonus is True, add a random bonus to the salary
if bonus:
    final_salary += get_bonus_amount(salary)

# Print the initial salary, bonus status, and final salary
print(f"{salary}, {bonus} - '${final_salary}'")
