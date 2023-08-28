# Function to decide whether to give a bonus or not.
# Let's assume True for 10000 and 600, and False for 25000
def get_bonus_status(salary):
    if salary == 10000 or salary == 600:
        return True
    if salary == 25000:
        return False
    return None


# Let's return 255 for 10000 and 3185 for 600
def get_bonus_amount(salary):
    if salary == 10000:
        return 255
    if salary == 600:
        return 3185
    return 0


# Ask the user for their salary and convert it to an integer
salary_str = input("Please enter your salary: ")
salary = int(salary_str)

# Decide whether to give a bonus
bonus = get_bonus_status(salary)

# If bonus is True, add the pre-defined bonus to the salary
if bonus:
    salary += get_bonus_amount(salary)

# Print the final salary and bonus status
print(f"{salary}, {bonus} - '${salary}'")
