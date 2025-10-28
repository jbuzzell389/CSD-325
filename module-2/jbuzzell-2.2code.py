# James Buzzell
# 10/27/2025
# 2.2 Assignment Code

import random

MIN = 1
MAX = 5

def rand_num():
    number_guess = int(input("\nGuess a whole number between 1 and 5: "))

    target_number = random.randint(MIN, MAX)

    if number_guess == target_number:
        print("\nMy number is " + str(target_number) + "\n\nYou guessed the correct number!\n")
    else:
        print("\nMy number is " + str(target_number) + "\n\nYou did not guess the correct number!\n")

rand_num()