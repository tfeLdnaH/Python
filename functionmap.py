income = [10, 30, 75]

def double_money(dollars):
    return dollars * 2

new_income = list(map(double_money, income)) # output result -> [20, 60, 150]

print(new_income)


