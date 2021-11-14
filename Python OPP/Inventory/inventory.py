"""
Product Inventory Project - Create an application which manages an inventory of products. 
Create a product class which has a price, id, and quantity on hand. 
Then create an inventory class which keeps track of various products and can sum up the inventory value.

Author: Máté Pados
Idea: github.com/karan
"""
import csv
from os import sep, write
from products import *

#Inventory: on-order

class Product:
    def __init__(self, name, id, price, quantity):
        self.name = name
        self.id = id
        self.price = float(price)
        self.quantity = quantity

class Inventory(Product):
    def __init__(self, name=None, id=0, price=0, quantity=0):
        super().__init__(name, id, price, quantity)
        self.inventory = []
        self.onOrder = []

    def print_item(self, i):
        print(f"{i.name} {i.id} | ${i.price} | Quantity: {i.quantity}")


    def add_to_inventory(self, item):
        with open("inventory.csv", "a", newline="\n") as file:
            writer = csv.writer(file, delimiter=" ")
            writer.writerow([item.name, item.id, "|", "$", item.price, "|", "Quantity:", item.quantity])


    def delete_from_inventory(self, item):
        with open("inventory.csv", "r") as file:
            reader = csv.reader(file)

            for row in reader:
                if item in row:
                    print("here")

    def list_inventory(self):
        print("Current stock:")

        with open("inventory.csv", "r") as file:
            reader = csv.reader(file)

            for row in reader:
                print(row[0])

    def find_item(self):
        print("What are you searching for?")
        name = input("-")

        for i in self.inventory:
            if i.name.lower() == name.lower():
                self.print_item(i)

    def inventory_sum(self):
        all_quantity = 0
        all_price = 0
        for item in self.inventory:
            all_quantity += item.quantity
            all_price += item.price * item.quantity

        print(f"{all_quantity} items for ${int(all_price)} available at the moment")
                    
    def edit_item(self, itemId):
        for i in self.inventory:
            if i.id == itemId:
                print("Editing:", i.name)
                print("Please choose from options:")
                print("1. Edit name")
                print("2. Edit id")
                print("3. Edit price")
                print("4. Edit quantity")
                x = int(input("Choice: "))

                if x == 1:
                    print("Enter new name:")
                    new_name = input()
                    i.name = new_name

                    print("Item edited successfully!")
                    self.print_item(i)

                if x == 2:
                    print("Enter new id:")
                    new_id = input()
                    i.id = new_id

                    print("Item edited successfully!")
                    self.print_item(i)

                if x == 3:
                    print("Enter new price:")
                    new_price = input()
                    i.price = new_price

                    print("Item edited successfully!")
                    self.print_item(i)

                if x == 4:
                    print("Enter quantity:")
                    new_quantity = input()
                    i.quantity = new_quantity

                    print("Item edited successfully!")
                    self.print_item(i)
        
    def order(self):
        print("Current stock:")
        for i in self.inventory:
            print(i.quantity, i.name, end="\n",)

        print()
        print("Enter order informations:")
        name = input("Name: ")
        for i in self.inventory:
            if name.lower() == i.name.lower():
                print(f"We already have {name} in stock!")
                print("Would you like to see current orders?")
                a = input().lower()
                if a == "yes":  
                    self.print_orderlist()
                quit()

        quantity = input("Quantity: ")

        print(f"Are you sure you want to order {quantity} {name}?")
        a = input().lower()
        if a == "yes":
            item = Product(name=name, id=0, price=0, quantity=quantity)
            self.onOrder.append(item)  
            print(f"{quantity} {name} ordered!")
            
            
    def print_orderlist(self):
        print("Current order list:")
        for i in self.onOrder:
            print(i.name, i.quantity, end="\n")

    def save(self):
        with open("inventory.csv", "w+", newline="") as file:
            writer = csv.writer(file, delimiter=" ", escapechar=" ", quoting=csv.QUOTE_NONE)
            
            #items on stock
            for i in self.inventory:
                writer.writerow([i.name, i.id, "|", "$", i.price, "|", "Quantity:", i.quantity])
            
            #3 empty rows
            for i in range(3):
                writer.writerow([])
            
            #items on order
            for i in self.onOrder:
                writer.writerow(["ON ORDER:"])
                writer.writerow([i.name, i.quantity, "pcs"])


if __name__ == '__main__':
    inv = Inventory()  
