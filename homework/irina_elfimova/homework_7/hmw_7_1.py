import random


def your_salary():
    salary = int(input("Enter your current salary "))
    bonus = random.choice([True, False])

    if bonus == True:
        full_salary = salary + random.randint(50, 10000)
        print("Your full salary is ", full_salary)

    else:
        print("Your full salary is ", salary)


your_salary()
