#pokemon card game
import random
import json

pokemons = open('pokemons.json')
card_names = json.loads(pokemons.read())

class User:
    def __init__(self):
        self.user = input('Do you want to choose your card? (Y/N) ')
        if self.user == 'Y':
            self.user = input('Your card: ')
            while self.user not in card_names:
                print('Wrong name!')
                self.user = input('Try a Pokemon name: ')

        elif self.user == 'N':
            self.user = random.choice(card_names)
            print('Your card has been randomly chosen: {}'.format(self.user))

class Pokemon(User):
    def __init__(self):
        super().__init__()
        self.user = self.user
        self.user_hp = random.randint(0,320) #according to google, the highest HP a card has is 320
        self.computer = random.choice(card_names)
        self.computer_hp = random.randint(0,320)

    def choose(self):
        choice = input('Do you want to battle(B), compare cards(C)? ')
        while choice != 'B' or 'C':
            if choice == 'B':
                self.battle()
            if choice == 'C':
                self.compare()
            break

    def battle(self):
        print()
        print('FIGHT BEGINS!')
        print('You have: {} and {} HP!'.format(self.user, self.user_hp))
        print('Your opponent has: {} and {} HP!'.format(self.computer, self.computer_hp))

        while self.user_hp >= 0 or self.computer_hp >= 0:
            damage = random.randint(1, 50) #damage limited, so it's not that easy to win

            self.user_hp = self.user_hp - damage
            print('Opponent damages {}, your hp is now {}'.format(damage, self.user_hp))
            
            damage = random.randint(1, 50)#damage limited, so it's not that easy to win

            self.computer_hp = self.computer_hp - damage
            print('You damage {}, opponent\'s hp is now {}'.format(damage, self.computer_hp))

            if self.computer_hp <= 0 or self.user_hp <= 0:
                break

        if self.user_hp > self.computer_hp:
            print('YOU WON!')
        elif self.computer_hp > self.user_hp:
            print('OPPONENT WON!')

    def compare(self):
        print()
        print('COMPARING BEGINS NOW!')

        if self.user_hp > self.computer_hp:
            print('YOU WIN!')
            print('You have {}, {}HP \nOpponent has {}, {}HP'.format(self.user, self.user_hp, self.computer, self.computer_hp))
        elif self.computer_hp > self.user_hp:
            print('OPPONENT WINS!')
            print('You have {}, {}HP \nOpponent has {}, {}HP'.format(self.user, self.user_hp, self.computer, self.computer_hp))
        else:
            print('TIE!')
            print('You have {}, {}HP \nOpponent has {}, {}HP'.format(self.user, self.user_hp, self.computer, self.computer_hp))

Pokemon().choose()
