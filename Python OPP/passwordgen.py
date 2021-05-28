import string
import random

class User:
    def __init__(self,name):
        self.name = name
        self.pw_length = int(input("Lenght of your password: "))

class Password(User):
    def __init__(self, name):
        super().__init__(name)
        self.password = ''

        while len(self.password) != self.pw_length:
            random_char = random.choice(string.printable)
            self.password = self.password + random_char


    def get_pw_of(self):
        print('Password of {} is: {}'.format(self.name, self.password))

if __name__ == '__main__':
    Password('Matthew').get_pw_of()
