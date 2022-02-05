"""
Product Inventory Project - Create an application which manages an inventory of products. 
Products have a price, id, and quantity on hand. 
Then the inventory keeps track of various products and can sum up the inventory value.


Author: Máté Pados
Idea: github.com/karan
"""

import csv
import shutil
from products import *
from os import path
from tempfile import NamedTemporaryFile

file_exists = path.isfile("inventory.csv")

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = float(price)
        self.quantity = quantity

class Inventory(Product):
    def __init__(self, name=None, price=0, quantity=0):
        super().__init__(name, price, quantity)
        self.inventory = []
        self.onOrder = []

    #def print_item(self, item):

    def new_id(self):
        with open("inventory.csv", "r") as file:
            reader = csv.reader(file)
            reader_list = list(reader)

            return len(reader_list)

    def add_to_inventory(self, item):
        fieldnames = ["id", "name", "price", "quantity"]

        with open("inventory.csv", "a", newline="\n") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            next_id = self.new_id()

            #write header only once
            if not file_exists:
                writer.writeheader()

            writer.writerow({
                "id": next_id,
                "name": item.name,
                "price": item.price,
                "quantity": item.quantity,
            })


    def delete_from_inventory(self, item=None):
        print("Enter the name of the item you want to delete:")
        item = input("- ").lower()

        l = []
        with open("inventory.csv", "r") as readFile:
            reader = csv.reader(readFile)

            for row in reader:
                l.append(row)
                for name in row:
                    if item in name.lower():
                        l.remove(row)

        with open("inventory.csv", "w", newline="\n") as file:
            writer = csv.writer(file)
            writer.writerows(l)

    def list_inventory(self):
        print("Current stock:")

        with open("inventory.csv", "r") as file:
            reader = csv.reader(file)

            for item in reader:
                print(type(item))

    def find_item(self):
        print("What are you searching for?")
        name = input("- ").lower()

        with open("inventory.csv", "r") as file:
            reader = csv.reader(file)

            for row in reader:
                for item in row:
                    if name in item.lower():
                        print(item)

    def inventory_sum(self):
        all_quantity = 0
        all_price = 0
        with open("inventory.csv", "r") as file:
            reader = csv.reader(file)

            for row in reader:
                self.inventory.append(row)
        
        for i in self.inventory:
            print(i, end="\n")


        print(f"{all_quantity} items for ${int(all_price)} available at the moment")
                    
    def edit_item(self):
        temp_file = NamedTemporaryFile(delete=False)

        with open("inventory.csv", "rb") as csvfile, temp_file:
            reader = csv.DictReader(csvfile)
            writer = csv.DictWriter(temp_file)
            writer.writeheader()


    def order(self):
        self.list_inventory()
 
        with open("inventory.csv", "r") as file:
            reader = csv.reader(file)

            print()
            print("Enter order informations:")
            name = input("Name: ")
            for row in reader:
                if name.lower() in row[0].lower():
                    print(f"We already have {name} in stock!")
                    quit()

            quantity = input("Quantity: ")

            print(f"Are you sure you want to order {quantity} {name}?")
            a = input().lower()
            if a == "yes":
                item = Product(name=name, id=0, price=0, quantity=quantity)
                with open("inventory.csv", "a", newline="\n") as file:
                    writer = csv.writer(file, delimiter=" ", escapechar=" ", quoting=csv.QUOTE_NONE)
                    writer.writerow([item.name, "|", "Quantity:", item.quantity, "ON ORDER"])
                     
            
    def print_orderlist(self):
        print("Current order list:")
        for i in self.onOrder:
            print(i.name, i.quantity, end="\n")


if __name__ == '__main__':
    inv = Inventory()
