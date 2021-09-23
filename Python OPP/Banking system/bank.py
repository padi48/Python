import time
from user import User

file = open("accounts.txt", "a+")
for line in file:
    line.split()

class Bank(User):
    def __init__(self):
        super().__init__() 
        self.balance = 0
        self.id = id

        print("***PADi BANK***")
        print("Hey, welcome to our new bank!")
        time.sleep(2)

        print("***CHOICES***")
        print("1. Deposit money")
        print("2. Withdraw money")
        print("3. Get a loan")
        print("4. View account details")

        choices = ['1', '2', '3', '4']
        choice = input("How can we help you? ")
        while choice not in choices:
            choice = input("How can we help you? ")

        if choice == '1':
            self.deposit()
        elif choice == '2':
            self.withdraw()
        elif choice == '3':
            self.loan()
        elif choice == '4':
            self.show_details()

    def show_details(self):
        file = open("accounts.txt", "r")
        print(file.readlines())

        print()
        print("Name: ", self.firstname, self.lastname)
        print("Account number: ", self.id)
        print("Balance: ", self.balance)
        file.close()

    def deposit(self):
        print("DEPOSIT")
        print("Your current balance is ${}".format(self.balance))
        time.sleep(2)

        deposit_amount = int(input('How much would you like to deposit?\n'))
        self.balance = self.balance + deposit_amount
        print("Transaction successful! Your balance is ${} now!".format(self.balance))


    def withdraw(self):
        print("WITHDRAW")
        print("Your current balance is {}".format(self.balance))
        time.sleep(2)

        withdraw_amount = int(input("How much would you like to withdraw?\n"))
        self.balance = self.balance - withdraw_amount
        print("Transaction successful! Your balance is ${}!".format(self.balance))

        if withdraw_amount > self.balance:
            print("Insufficient Funds | Balance available: ${}".format(self.balance))
            withdraw_amount = int(input("How much would you like to withdraw?\n"))


    def loan(self):
        print("LOAN")
        print("Your current balance is ${}".format(self.balance))
        time.sleep(2)

        loan_amount = int(input("How much would you like to loan?\n"))
        self.balance = self.balance + loan_amount
        print("Transaction successful! Your balance is ${}!".format(self.balance))

        if loan_amount <= self.balance:
            print("You already have that much, current account balance is ${}!".format(self.balance))
            withdraw = input("Would you like to withdraw ${}?".format(loan_amount))
            
            if withdraw == 'yes':
                self.balance = self.balance - withdraw
                print("Transaction successful! Your balance is ${}!".format(self.balance))
            
        
