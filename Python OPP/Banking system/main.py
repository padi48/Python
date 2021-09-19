from user import User
from bank import Bank
from admin import Admin

def first():
    print("Welcome!")
    print("Choose from the options below:")
    print("1. Login")
    print("2. Register")
    print("- - - - - - - - - - - -")
    print("3. Login as admin")
    choice = input()

    if choice == "1":
        User().login()
    elif choice == "2":
        User().register()
    elif choice == "3":
        Admin()
    else:
        print("Invalid choice!")
        first()

def main():
    first()

if __name__ == '__main__':
    main()
