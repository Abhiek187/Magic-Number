# This is a simple program that tests one's skills in using loops and random numbers.
import random


class MagicNumber:
    guess = 0
    random_number = 1

    while guess != random_number:
        random_number = random.randint(0, 9)  # generates a random number between 0 and 9
        guess = int(input("I'm thinking of a number between 0 and 9. What is it? "))

        if guess == random_number:
            break
        else:
            print("Sorry, try again.")

    print("Correct! You win!")
