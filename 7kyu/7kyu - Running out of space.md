## Running out of space - 7kyu

**Instructions**

- Write a function that removes the spaces from the values and returns an array showing the space decreasing.

- For example, running this function on the array `['i', 'have', 'no', 'space']` would produce `['i', 'ihave', 'ihaveno', 'ihavenospace']`.

---

#### Test cases

```python
print(spacey(['kevin', 'has','no','space']))
print(spacey(['this','cheese','has','no','holes']))
```

#### Output

```
['kevin', 'kevinhas', 'kevinhasno', 'kevinhasnospace']
['this', 'thischeese', 'thischeesehas', 'thischeesehasno', 'thischeesehasnoholes']
```

---

#### Solution

```python
from itertools import accumulate
def spacey(arr):
    return [*accumulate(arr)]
```

---

[Codewars link](https://www.codewars.com/kata/56576f82ab83ee8268000059)
