import getpass

'''
Search by id
with open("accounts.txt", "r") as f:
    for line in f:
        id = line.split()
        if "9339" in id:
            print(line)

        if "str" in line:
            break
'''

class Admin:
    def __init__(self):
        getpass.getpass("Password:")
