# Notes
# if and else are used to execute code based on a condition.
# if condition:
#     # code to execute if condition is true
# else:
#     # code to execute if condition is false
# *** make sure the code is indented properly, and colon after the condition

# comparsion operators
# == equal to
# != not equal to
# > greater than
# < less than
# >= greater than or equal to
# <= less than or equal to

#Modulo Operator
# % is the modulo operator

# Logical operators
# A and B, use and keyword to check if both A and B are true
# A or B, use or keyword to check if either A or B is true
# not A, use not keyword to check if A is false

# Treasure island project

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go?")
question1 = input("Type 'left' or 'right'\n")

if question1 == "left":
    print("You're now at a lake. Do you swim or wait?")
    question2 = input("Type 'swim' or 'wait'\n")
    if question2 == "swim":
        print("You made it to a room with 3 doors. Which do you pick?")
        question3 = input("Type 'red', 'blue', or 'yellow\n")
        if question3 == "yellow":
            print("You Win!")
        elif question3 == "red":
            print("Burned by fire. Game Over.")
        elif question3 == "blue":
            print("Eaten by beast. Game Over.")
        else:
            print("Game Over.")
    else:
        print("Attacked by a shark. Game Over.")
else:
    print("Fall into a hole. Game Over.")