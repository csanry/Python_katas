## Cost of my ride - 7kyu

**Instructions**

- Create a function that computes the cost of renting a car. 

- The function takes 3 arguments: the age of the renter, the size of the car, and the number days for the rental. 

- Return an integer number of the calculated total cost of the rental.

- Age (integer) : There is a daily charge of $10 if the driver is under 25

- Car Size (string) : There may be an additional daily charge based on the car size:

```
"economy": $0 surcharge
"medium": $10 surcharge
"full-size": $15 surcharge
```

- Rental Days (integer) : There is a base daily charge of $50 for renting a car. Simply multiply the one day cost by the number of days the car is rented in order to get the full cost.

- Negative rental days should return 0 cost.

- Any other car size not listed should come with the same surcharge as full-size: $15

---

#### Test cases

```python
print((insurance(18, "medium", 7))
print((insurance(30, "full-size", 30))
print((insurance(21, "economy", -10))
print((insurance(42, "my custom car", 7))
```

#### Output 
```
490
1950
0
455
```

---

#### Solution

```python
def insurance(age, size, num_of_days):
    surge = {"economy": 0, "medium": 10}
    return max(0, num_of_days) * (50 + surge.get(size, 15) + (10 if age < 25 else 0))
```

---

[Codewars link](https://www.codewars.com/kata/586430a5b3a675296a000395)
