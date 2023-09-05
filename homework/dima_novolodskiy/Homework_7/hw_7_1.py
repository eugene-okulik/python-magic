from random import randrange, choice


def salary_bonus(salarys):
    appruv = [True, False]
    bonus_appruv = choice(appruv)
    if bonus_appruv:
        return f"{salarys}, {bonus_appruv} - '${salarys + randrange(0, 100000)}'"
    else:
        return f"{salarys}, {bonus_appruv} - '${salarys}'"


salary = int(input('Enter salary:'))
print(salary_bonus(salary))
