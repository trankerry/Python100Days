# Notes
# Data types: strings, integers, floats, booleans

# Type conversion: str(), int(), float(), bool()

# Operators: + is addition, - is subtraction, * is multiplication, / is division, ** is exponentiation, // is integer division, % is modulo

# Number functions: 
# round(number you want to round, number of places you want it rounded to)

# Number manipulation:
# score += 1 is the same as score = score + 1
# score -= 1 is the same as score = score - 1
# score *= 1 is the same as score = score * 1
# score /= 1 is the same as score = score / 1

# f-strings:
# score = 0
# height = 1.8
# isWinning = True
# ex. print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}")

# Tip Caliculator Project
# We're going to build a tip calculator.
# If the bill was $153.45, split between 5 people, with 15% tip.
# Each person should pay:
# After formatting the result to 2 decimal places = 35.29


print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 or 15? "))
people = int(input("How many people to split the bill? "))

perPerson = round(((bill + (bill * (tip/100)))/people),2)
print(f"Each person should pay: ${perPerson}")