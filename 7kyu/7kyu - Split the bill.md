## Split the bill - 7kyu

**Instructions**

- It's tricky keeping track of who is owed what when spending money in a group.

- Write a function to balance the books.

- The function should take one parameter: a dict representing the members of the group and the amount spent by each.

- The function should return a dict with the same names, showing how much money the members should pay or receive.

- The values should be positive numbers if the person should receive money from the group, negative numbers if they owe money to the group.

- If value is a decimal, round to 2 decimal places.

---

#### Test cases

```python
print(split_the_bill({'A': 20, 'B': 15, 'C': 10}))
print(split_the_bill({'A': 40, 'B': 25, 'X': 10}))
```

#### Output 

```
{'A': 5.0, 'B': 0.0, 'C': -5.0}
{'A': 15.0, 'B': 0.0, 'X': -15.0}
```

---

#### Solution

```python
import numpy as np
def split_the_bill(x):
    amt = np.mean([*x.values()])
    return {k: round((v - amt), 2) for k, v in x.items()}
```

---

[Codewars link](https://www.codewars.com/kata/5641275f07335295f10000d0)
