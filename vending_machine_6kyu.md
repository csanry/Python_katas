## Vending Machine - 6kyu

**Instructions**

- In this simple Kata aimed at beginners your task is to recreate a vending machine.

- You will have to make a class called `VendingMachine` with at least one method called `vend`.

- On creation of a new instance of `VendingMachine` the `items` array and initial vending machine `money` is passed.

- The `vend` method should take two arguments
    - Selection code of the item (not case sensitive)
    - Amount of money the user inserts into the machine.

**Rules**
1. If the money given to the machine is less than the item cost return `"Not enough money!"`

2. If the quantity is 0 for an item return `"Item Name: Out of stock!"`. Where `"Item Name"` is the name of the item selected.

3. If an item is correctly selected return `"Vending Item Name with 9.40 change."`. Where `"Item Name"` is the name of the item and change if any given.

4. If an item is correctly selected and there is no change needed then return `"Vending Item Name"`. Where `"Item Name"` is the name of the item.

5. If an invalid item is selected return `"Invalid selection! : Money in vending machine = 11.20"`. Where 11.20 is the machines money float.

6. If a selection is successful then the quantity should be updated.

7. The vending machine never runs out of money for simplicity however you will need to keep track of the amount of money in the machine at anytime (this is not tested in any of the test cases)

8. Change is always given to 2 decimal places ie 7.00

---

#### Test cases

```Python
machine = VendingMachine(items = items, money = 10)
print(machine.vend("A01", 0.60))
print(machine.vend("A01", 10.0))
print(machine.vend("Z01", 0.41))
print(machine.vend("A02", 0.40))
print(machine.vend("B06", 4.60))
```

#### Output 
```
Vending Smarties
Vending Smarties with 9.40 change.
Invalid selection : Money in vending machine = 11.20
Not enough money!
Cheese and Onion Crisps: Out of stock!
```

---

#### Solution

```python
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
```

---


[Codewars link](https://www.codewars.com/kata/586e6d4cb98de09e3800014f)
