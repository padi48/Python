import time 
import random

name = input("What is your name? ")

print("\nHello " + name+ "\nTime to play hangman!\n")
time.sleep(1)

print("Start guessing...\nHint:It is a fruit")
time.sleep(1)

someWords = '''mango apple banana strawberry pineapple orange lemon watermelon peach 
coconut cherry papaya grape berry blackberry'''

someWords = someWords.split(' ')
word = random.choice(someWords)

guesses = ''

turns = 5

while turns > 0:
    failed = 0

    for char in word:
        if char in guesses:
            print(char, end = ' ')
        else:
            print("_", end = ' ')
            failed += 1
    
    if failed == 0:
        print("\nYou won!")
        break
    print

    guess = input("\nGuess a character: ")

    if not guess.isalpha():
        print("Enter only a LETTER")
        continue
    elif len(guess) > 1:
        print("Enter only a SINGLE letter")
    elif guess in guesses:
        print("You've already guessed that letter")
        continue

    guesses += guess

    if guess not in word:
        turns -= 1
        print("\nWrong")
        print("You have", + turns, 'more guesses\n')

        if turns == 0:
            print("You lose!")
