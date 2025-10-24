"""
Number Guessing Game
- feature : asks the user for minimum and maximum value
"""

import random

minimum_value = int(input("Enter the minimum value : "))
maximum_value = int(input("Enter the Maximum value : "))
number_to_guess = random.randint(minimum_value, maximum_value)

total_attempts = 5
no_of_attempts = 0

while no_of_attempts<total_attempts:
    try:
        guess = int(input(f"Enter a number between {minimum_value} and {maximum_value} : "))
        if guess > number_to_guess:
            print("Too High !")
        elif guess < number_to_guess:
            print("Too low")
        else:
            print("Congratulations! you have guessed the number")
            break
            
        no_of_attempts+=1

    except ValueError:
        print("Enter the valid number")

print(f"Sorry you have ran out of guesses\nThe secret number was {number_to_guess}")