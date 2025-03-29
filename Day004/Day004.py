# Notes
# random is the Python standard library for generating random numbers.
# import random
# random.randint(a, b) returns a random integer N such that a <= N <= b.
# random.random() returns a random float N such that 0 <= N < 1.
# random.float(a, b) returns a random float N such that a <= N <= b.
# random.choice(seq) returns a randomly selected element from the non-empty sequence seq.

# list
# list is a built-in Python data type that is used to store a collection of items.
# list.append(x) adds an item x to the end of the list.
# list.insert(i, x) inserts an item x at a given position i in the list.
# list.remove(x) removes the first item from the list whose value is equal to x.
# list.pop(i) removes the item at the given position i in the list, and returns it.

# My solution
# import random

# friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
# winner = random.randint(0,len(friends)-1)
# print(friends[winner])

# Better solution
# import random
# friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
# print(random.choice(friends))

# Rock, Paper, Scissors Project

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
computer_choice = random.randint(0,2)

options = [rock, paper, scissors]
if choice >= 3 or  choice < 0:
    print("Invalid choice, play again.")
else:
    print(options[choice])
    print("Computer choose: ")
    print(options[computer_choice])

    if (choice == 0 and computer_choice == 2) or (choice == 1 and computer_choice == 0) or (
            choice == 2 and computer_choice == 1):
        print('You Win!')
    elif (choice == 0 and computer_choice == 0) or (choice == 1 and computer_choice == 1) or (
            choice == 2 and computer_choice == 2):
        print("Draw")
    else:
        print("You Lose!")