"""
Product Inventory Project - Create an application which manages an inventory of products. 
Products have a price, id, and quantity on hand. 
Then the inventory keeps track of various products and can sum up the inventory value.


Author: Máté Pados
Idea: github.com/karan
"""

import csv
from products import *
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

    #generates next id for item
    def new_id(self):
        with open("inventory.csv", "r") as file:
            reader = csv.DictReader(file)
            reader_list = list(reader)

            return len(reader_list)

    #adds new item to the csv file
    def add_to_inventory(self, item):
        fieldnames = ["id", "name", "price", "quantity"]

        with open("inventory.csv", "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                if item.name in row:
                    self.add_to_existing(item.quantity)

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

    def add_to_existing(self, new_quantity):
        l = []

        with open("inventory.csv", "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                l.append(row)

        with open("inventory.csv", "w") as file:
            writer = csv.DictWriter(file)

            for item in l:
                writer.writerow({
                    "id": item["id"],
                    "name": item["name"],
                    "price": item["price"],
                    "quantity": item["quantity"] + new_quantity 
                })

    #generates a new product
    def create_new_product(self):
        name = str(input("Enter new item's name: "))
        price = float(input("Enter new item's price: "))
        quantity = int(input("Enter new item's quantity: "))

        new_item = Product(name, price, quantity)
        self.add_to_inventory(new_item)

    #deletes item from the csv file
    def delete_from_inventory(self, item=None):
        self.list_inventory()
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
                        print("Item successfully deleted!")


        with open("inventory.csv", "w", newline="\n") as file:
            writer = csv.writer(file)
            writer.writerows(l)

    #prints out the whole inventory
    def list_inventory(self):
        print("Current stock:")

        with open("inventory.csv", "r") as file:
            reader = csv.reader(file)
            
            for item in reader:
                print(f"{item[0]} | {item[1]} | ${item[2]} | {item[3]} ")

    #prints sum of price, quantity for given item
    def item_sum(self):
        item_name = input("Name of item you want to see: ")
        l = []
        with open("inventory.csv", "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                l.append(row)
        
        for i in l:
            if i["name"] == item_name:
                print(i["quantity"], i["name"], "available for $", (float(i["price"]) * int(i["quantity"])))

    #prints sum of inventory
    def inventory_sum(self):
        with open("inventory.csv", "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                print(row["quantity"], row["name"], "available for $", (float(row["price"])) * int(row["quantity"]))

    #edit item in the csv file
    #reads all items from the csv file and then re-writes them
    #so the order doesn't change
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

            writer.writeheader()
            for item in l:
                writer.writerow({
                    "id": item["id"],
                    "name": item["name"],
                    "price": item["price"],
                    "quantity": item["quantity"],
                })

        self.list_inventory()

if __name__ == '__main__':
    inv = Inventory()
