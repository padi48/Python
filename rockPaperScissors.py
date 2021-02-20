from random import randint

choices = ["rock", "paper", "scissors"]

computer = choices[randint(0,2)]

player = False

while player == False:
    player = input("Rock, Paper, Scissors? ")

    if player == computer:
        print("Tie!")
    elif player == "rock":
        if computer == "scissors":
            print("You win! Rock beats Scissors!")
        else:
            print("You lose! Paper beats Rock!")
    elif player == "paper":
        if computer == "rock":
            print("You win! Paper beats Rock!")
        else: 
            print("You lose! Scissors beats Paper!")
    elif player == "scissors":
        if computer == "paper":
            print("You win! Scissors beats Paper!")
        else:
            print("You lose! Rock beats Scissors!")
