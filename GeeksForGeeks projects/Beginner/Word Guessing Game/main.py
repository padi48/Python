#Word guessing game
# https://www.geeksforgeeks.org/python-program-for-word-guessing-game/?ref=lbp

import random

def game():
    words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']
    tries = 0

    print("----- GUESS THE WORD -----")
    name = str(input("Enter your name: "))

    word = random.choice(words)
    guessed = []

    print(f"I have my word, good luck {name}!")
    print("_"*len(word))

    while tries < 12:
        print()
        tries += 1
        guess = str(input("Guess a character: "))

        if len(guess) > 1:
            print("Guess only one character!")
            quit()

        if guess in word:
            guessed.append(guess)
            
        for i in word:
            if i in guessed:
                print(i, end="")
            else:
                print("_", end="")

        if len(guessed) == len(word):
            print()
            print(f"Congratulations {name}, you guessed my word in {tries} tries!")
            quit()

    print()
    print(f"You lose! My word was '{word}'")

game()
