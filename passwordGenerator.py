import string
import random

a = string.digits
b = string.ascii_letters
c = "!@#$%^&*()"

letters = []
for i in string.printable:
    letters.append(i)

length = int(input("Enter password length: "))

def make_password():
    password = []
    temp = 0

    digits = int(input("Enter how many digits you want: "))
    
    temp += digits
    if temp > length:
        print("INVALID")
        return
    print("You have", str(length-temp), "characters left")

    lett = int(input("Enter how many letters you want: "))
    temp += lett
    if temp > length:
        print("INVALID")
        return
    print("You have", str(length-temp), "characters left")

    char = int(input("Enter how many special characters you want: "))
    temp += char
    if temp > length:
        print("INVALID")
        return

    

    for i in range(digits):
        i = random.choice(a)
        password.append(i)

    for i in range(lett):
        i = random.choice(b)
        password.append(i)

    for i in range(char):
        i = random.choice(c)
        password.append(i)

    random.shuffle(password)

    print("Your new password is: ")
    for i in password:
        print(i, end="")

make_password()
