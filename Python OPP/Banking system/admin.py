import getpass
import fileinput
from user import User

class Admin(User):
    def __init__(self):
        super().__init__()
        getpass.getpass("Password:")

        print("ADMIN")
        print("Choose from the options below!")
        print("1. Search by ID")
        print("2. See all accounts")
        print("3. Modify account")
        print("4. Delete account")
        choice = input()

        if choice == "1":
            self.id_search()
        elif choice == "2":
            self.see_all()
        elif choice == "3":
            self.modify()
        elif choice == "4":
            self.delete()
        else:
            print("Invalid choice!")
            Admin()

    def id_search(self):
        user_id = input("Enter ID: ")
        
        with open("accounts.txt", "r") as f:
            for line in f:
                id = line.split()
                if user_id in id:
                    print(line)

                if "str" in line:
                    break
        f.close()

    def see_all(self):
        with open("accounts.txt", "r") as f:
            for line in f:
                print(line)
                
        f.close()

    def modify(self):
        id = input("Enter ID: ")

        with open("accounts.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                l = line.split()
                if id in l:
                    target = l
                    print(line)
                    print("- - - - - - - - - - - ")
                    print("1. Change name")
                    print("2. Change password")
                    print("3. Change id")
                    choice = input()
                       
                    if choice == "1":
                        with open("accounts.txt", "w") as f:
                            for line in lines:
                                if line.split() != target:
                                    f.write(line)
                                else:
                                    print("Enter new name")
                                    name = input("> ")
                                    text = f"{name} | {self.password} | {self.id}\n"
                                    f.write(text)      


    def delete(self):
        id = input("Enter ID: ")

        with open("accounts.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                l = line.split()
                if id in l:
                    target = l

        with open("accounts.txt", "w") as f:
            for line in lines:
                if line.split() != target:
                    f.write(line)
        f.close()

Admin()
