## Smallest product - 7kyu

**Instructions**

- Given a non-empty array of non-empty integer arrays, multiply the contents of each nested array and return the smallest total.

```
input = [
  [1, 5],
  [2],
  [-1, -3]
]

result = 2
```

---

#### Test cases

```python
print(smallest_product([[3, 2], [1, 2, 1], [7, 8]]))
print(smallest_product([[10], [3, 0], [-1, -6, 2]]))
```

#### Output 

```
2
0
```

---

#### Solution

```python
from math import prod

def smallest_product(arr):
    return min(map(prod, arr))
```

---

[Codewars link](https://www.codewars.com/kata/5b6b128783d648c4c4000129)
