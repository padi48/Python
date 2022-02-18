"""
Product Inventory Project - Create an application which manages an inventory of products. 
Products have a price, id, and quantity on hand. 
Then the inventory keeps track of various products and can sum up the inventory value.


Author: Máté Pados
Idea: github.com/karan
"""

from asyncore import write
import csv
import shutil
from products import *
from tempfile import NamedTemporaryFile
from os import path

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

    def print_item(self, item):
        print(f"{item[1]}")

    def find_item(self, item_name):
        with open("inventory.csv", "r") as file:
            reader = csv.DictReader(file)

            for rows in reader:
                if rows["name"].lower() == item_name.lower():
                    print(rows)

            return -1

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

    def create_new_product(self):
        name = str(input("Enter new item's name: "))
        price = float(input("Enter new item's price: "))
        quantity = int(input("Enter new item's quantity: "))

        new_item = Product(name, price, quantity)
        self.add_to_inventory(new_item)

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
                print(f"{item[0]} | {item[1]} | ${item[2]} | {item[3]} ")

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
        print("EDIT ITEM PANEL")
        self.list_inventory()
        l = []
        row_id = input("Enter ID of row you want to edit: ")

        with open("inventory.csv", "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                l.append(row)
            
        for item in l:
            if row_id == item["id"]:
                print("Choose from the options below:")
                choice = input("1. Name\n2. Price\n3. Quantity\n- ")
                
                if choice == "1":
                    new_name = input("Enter new name: ")
                    item["name"] = new_name
                if choice == "2":
                    new_price = input("Enter new price: $")
                    item["price"] = new_price
                if choice == "3":
                    new_quantity = input("Enter new quantity: ")
                    item["quantity"] = new_quantity

        with open("inventory.csv", "w", newline="\n") as file:
            fieldnames = ["id", "name", "price", "quantity"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            next_id = self.new_id()
        
            writer.writeheader()
            for item in l:
                writer.writerow({
                    "id": next_id,
                    "name": item["name"],
                    "price": item["price"],
                    "quantity": item["quantity"],
                })

if __name__ == '__main__':
    inv = Inventory()
    inv.add_to_inventory(apple)
