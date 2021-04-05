'''
Banking System 

User class:
- Holds details about the user
- Fuction to show user details

Bank class:
- Holds details about the account balance
- Functions to deposit/withdraw/view user balance
'''

class User():
    def __init__(self, name, gender, age, job):
        self.name = name
        self.gender = gender
        self.age = age
        self.job = job

    def show_details(self):
        print("User's details:")
        print("")
        print("Name:", self.name)
        print("Gender:",self.gender)
        print("Age:",self.age)
        print("Job:",self.job)

class Bank(User):
    def __init__(self, name, gender, age, job):
        super().__init__(name, gender, age, job)
        self.balance = 0

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + amount
        print("Account balance has been updated!")
        print("")
        print("New account balance is:", self.balance)

    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient Funds | Balance available:", self.balance)
        else:
            self.balance = self.balance - self.amount
            print("Account balance has been updated!")
            print("")
            print("New account balance is:",self.balance)

    def view_balance(self):
        self.show_details()
        print("User's balance is:", self.balance)

matt = Bank("Matthew", "Male", 18, "Programmer")
matt.deposit(100)
matt.withdraw(50)
matt.view_balance()
