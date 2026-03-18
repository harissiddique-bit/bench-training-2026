name = "Haris"
age = 25
drinks_coffee = True
salary = 120000

if drinks_coffee:
    coffee_text = "I drink coffee"
else:
    coffee_text = "I do not drink coffee"

print(f"My name is {name}, I am {age} years old, {coffee_text}, and my salary is Rs. {salary} per month.")

retirement_age = 60
years_until_retirement = retirement_age - age
print(f"Years until retirement: {years_until_retirement}")

cups_per_day = 3
coffee_price_per_cup = 150
days_per_week = 7

if drinks_coffee:
    weekly_coffee_budget = cups_per_day * coffee_price_per_cup * days_per_week
    print(f"Weekly coffee budget: Rs. {weekly_coffee_budget}")
else:
    print("No coffee budget, I don't drink coffee.")