import random
import getpass

class User(object):
    def __init__(self):
        print()

    def register(self):
        print("***REGISTER***")
        file = open("accounts.txt", "a+")

        self.firstname = input("Enter your first name: ")
        self.lastname = input("Enter your last name: ")
        self.password = getpass.getpass(prompt="Enter password: ")

        self.id = random.randint(1000,9999)

        for line in file:
            line.split()
            if self.id in file:
                self.id = random.randint(1000,9999)


        print()
        print("Successful registration!")
        print("Your details:")
        print("First name:", self.firstname)
        print("Last name:", self.lastname)
        print("Account ID:", self.id)

        text = f"{self.firstname} {self.lastname} | {self.password} | {self.id}\n"
        file.write(text)
        file.close()

    def login(self):
        print("Enter your ID: ")
        id = input()

        with open("accounts.txt", "r") as file:
            for line in file:
                line.split()
                if id in line:
                    print("Logged in as:")
                    print(line)

        file.close()
