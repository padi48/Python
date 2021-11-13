"""
Product Inventory Project - Create an application which manages an inventory of products. 
Create a product class which has a price, id, and quantity on hand. 
Then create an inventory class which keeps track of various products and can sum up the inventory value.

Author: Máté Pados
Idea: github.com/karan
"""
import csv
from product import *

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

    def print_item(self, i):
        print(f"{i.name} {i.id} | ${i.price} | Quantity: {i.quantity}")


    def add_to_inventory(self, item):
        self.inventory.append(item)
        print(f"Item \"{item.name}\" added to inventory!")

    def delete_from_inventory(self, item):
        self.inventory.remove(item)

    def list_inventory(self):
        print("Inventory:")

        for i in self.inventory:
            self.print_item(i)

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

    def save(self):
        with open("inventory.csv", "w", newline="") as file:
            writer = csv.writer(file, delimiter=" ")
            for i in self.inventory:
                writer.writerows([i.name], [i.id], ["|"], ["$"], [i.price], ["|"], ["Quantity:"], [i.quantity])

    

if __name__ == '__main__':
    inv = Inventory()
    inv.add_to_inventory(apple)
    inv.add_to_inventory(cherry)
    inv.add_to_inventory(milk)
    inv.find_item()
    inv.save()
