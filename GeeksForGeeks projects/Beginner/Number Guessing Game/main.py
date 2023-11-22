#Number guessing game, where user has to guess system's number in the minimum number if tries.
import random
import math

def game():
    print("----- NUMBER GUESSING GAME -----")
    print("Please enter range below:")
    try:
        m = int(input("Minimum: "))
        mx = int(input("Maximum: "))
    except ValueError:
        print("Range must be given in integers!\n")
        game()

    number = random.randint(m, mx)

    guess = int(input("Try to guess my number: "))
    tries = 0

    minimum_tries = math.log2(mx - m + 1)

    while guess != number:
        tries += 1

        if guess > number:
            guess = int(input("Try again, your guess was too high: "))
        else:
            guess = int(input("Try again, your guess was too small: "))

    
    if tries <= minimum_tries:
        print("Congratulations, you guessed my number in minimum tries.")
    else:
        print("Better luck next time!")

    again = str(input("Wanna play again? (Y/N)\n")).upper()

    if again == "N":
        print("Alright, have a great day!")
    else:
        game()


game()
