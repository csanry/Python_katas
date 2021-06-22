# vending machine - 6kyu

"""
In this simple Kata aimed at beginners your task is to recreate a vending machine.
You will have to make a class called VendingMachine with at least one method called vend.
On creation of a new instance of VendingMachine the items Array and Initial vending machine money is passed.
The vend method should take two arguments
1. Selection code of the item (not case sensitive)
2. Amount of money the user inserts into the machine.

Rules
1. If the money given to the machine is less than the item cost return "Not enough money!"
2. If the quantity is 0 for an item return "Item Name: Out of stock!". Where "Item Name" is the name of the item selected.
3. If an item is correctly selected return "Vending Item Name with 9.40 change.". Where "Item Name" is the name of the item and change if any given.
4. If an item is correctly selected and there is no change needed then return "Vending Item Name". Where "Item Name" is the name of the item.
5. If an invalid item is selected return "Invalid selection! : Money in vending machine = 11.20". Where 11.20 is the machines money float.
6. If a selection is successful then the quantity should be updated.
7. The vending machine never runs out of money for simplicity however you will need to keep track of the amount of money in the machine at anytime (this is not tested in any of the test cases)
8. Change is always given to 2 decimal places ie 7.00
"""

class VendingMachine():

    def __init__(self, items, money):
        self.items = items
        self.money = float(money)

    def vend(self, selection, item_money):
        for i in range(len(items)):
            if items[i]['code'] == selection:
                order = items[i]
                if item_money < order['price']:
                    return 'Not enough money!'
                if order['quantity'] < 1:
                    return f"{order['name']}: Out of stock!"
                self.money += order['price']
                order['quantity'] -= 1
                change = item_money - order['price']
                if change > 0:
                    return f"Vending {order['name']} with {change:.2f} change."
                else:
                    return f"Vending {order['name']}"
        return f"Invalid selection : Money in vending machine = {self.money:.2f}"

# test
items = [{'name': 'Smarties', 'code': 'A01', 'quantity': 10, 'price': 0.6},
         {'name': 'Caramac Bar', 'code': 'A02', 'quantity': 5, 'price': 0.6},
         {'name': 'Dairy Milk', 'code': 'A03', 'quantity': 1, 'price': 0.65},
         {'name': 'Freddo', 'code': 'A04', 'quantity': 1, 'price': 0.25},
         {'name': 'Crunchie', 'code': 'A05', 'quantity': 10, 'price': 0.7},
         {'name': 'Starbar', 'code': 'A06', 'quantity': 1, 'price': 0.99},
         {'name': 'Snickers', 'code': 'A07', 'quantity': 7, 'price': 0.89},
         {'name': 'Yorkie', 'code': 'A08', 'quantity': 20, 'price': 0.87},
         {'name': 'Toblerone', 'code': 'A09', 'quantity': 1, 'price': 1.99},
         {'name': 'Flake', 'code': 'A10', 'quantity': 10, 'price': 0.27},
         {'name': 'Ready Salted Crisps', 'code': 'B01', 'quantity': 7, 'price': 0.55},
         {'name': 'Sweet Chilli Crisps', 'code': 'B02', 'quantity': 12, 'price': 1.2},
         {'name': 'Smoky Barbecue Crisps', 'code': 'B03', 'quantity': 10, 'price': 0.65},
         {'name': 'Salt and Vinegar Crisps', 'code': 'B04', 'quantity': 5, 'price': 0.6},
         {'name': 'Roast Chicken Crisps', 'code': 'B05', 'quantity': 10, 'price': 0.59},
         {'name': 'Cheese and Onion Crisps', 'code': 'B06', 'quantity': 0, 'price': 0.67},
         {'name': 'Prawn Cocktail Crisps', 'code': 'B07', 'quantity': 10, 'price': 0.77},
         {'name': 'Thai Sweet Chicken Crisps', 'code': 'B08', 'quantity': 10, 'price': 0.88},
         {'name': 'Flamed Steak Crisps', 'code': 'B09', 'quantity': 10, 'price': 0.43},
         {'name': 'Coke', 'code': 'C02', 'quantity': 50, 'price': 0.75},
         {'name': 'Diet Coke', 'code': 'C03', 'quantity': 50, 'price': 0.75},
         {'name': 'Coke Zero', 'code': 'C04', 'quantity': 0, 'price': 0.75},
         {'name': 'Dandelion and Burdock', 'code': 'C05', 'quantity': 10, 'price': 0.68},
         {'name': 'Cream Soda', 'code': 'C06', 'quantity': 5, 'price': 0.69},
         {'name': 'Irn Bru', 'code': 'C07', 'quantity': 3, 'price': 0.79},
         {'name': 'Cherry Coke', 'code': 'C08', 'quantity': 1, 'price': 0.75},
         {'name': 'Orange Soda', 'code': 'C09', 'quantity': 10, 'price': 0.79},
         {'name': 'Parma Violets', 'code': 'D01', 'quantity': 10, 'price': 1.27},
         {'name': 'Refresher Chews', 'code': 'D02', 'quantity': 10, 'price': 4.27},
         {'name': 'Mini Love Hearts', 'code': 'D03', 'quantity': 10, 'price': 2.02},
         {'name': 'Popping Candy', 'code': 'D04', 'quantity': 10, 'price': 1.01},
         {'name': 'Drumstick Lollies', 'code': 'D05', 'quantity': 10, 'price': 5.12},
         {'name': 'Double Candy Lollies', 'code': 'D06', 'quantity': 10, 'price': 10.0},
         {'name': 'Wham Bars', 'code': 'D07', 'quantity': 10, 'price': 50.0},
         {'name': 'Double Dip', 'code': 'D08', 'quantity': 10, 'price': 1.04},
         {'name': 'Candy Sticks', 'code': 'D09', 'quantity': 10, 'price': 2.14},
         {'name': 'Jelly Cubes', 'code': 'D10', 'quantity': 10, 'price': 1.18}]

machine = VendingMachine(items = items, money = 10)
print(machine.vend("A01", 0.60))
print(machine.vend("A01", 10.0))
print(machine.vend("Z01", 0.41))
print(machine.vend("A02", 0.40))
print(machine.vend("B06", 4.60))