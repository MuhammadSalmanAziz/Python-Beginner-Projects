"""
Rolling the Dice Game.
Ask from user how much times they want to play
Count the number of times when user roll the dice

"""

import random

Guesses = int(input("How many dice you want to roll ? : "))
count = 0
i = 1
while i <= Guesses:
    choice = input("Roll the Dice ? (y / n) : ").lower()
    if choice == "y":
        deil1 = random.randint(1, 6)
        deil2 = random.randint(1, 6)
        count += 1
        print(f"({deil1},{deil2})")
    elif choice == "n":
        print("Thanks for Playing")
        break
    else:
        print("Invalid Choice")
    i += 1
print(f"User has rolled the dice {count} time")
