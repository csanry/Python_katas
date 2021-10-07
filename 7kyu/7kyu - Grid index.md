## Grid index - 7kyu

**Instructions**

- You are given an n by n ( square ) grid of characters, for example:

```python
[['m', 'y', 'e'], 
 ['x', 'a', 'm'], 
 ['p', 'l', 'e']]
```

- You are also given a list of integers as input, for example:

```python
[1, 3, 5, 8]
```

- Find the characters in these indexes of the grid if you think of the indexes as:

```python
[[1, 2, 3], 
 [4, 5, 6], 
 [7, 8, 9]]
```

- Indexes start from 1 and not 0.

- Output a string, for eg. `"meal"`

---

#### Test cases

```python
print(grid_index([['m', 'y', 'e'], ['x', 'a', 'm'], ['p', 'l', 'e']], [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(grid_index([['m', 'y', 'e'], ['x', 'a', 'm'], ['p', 'l', 'e']], [1, 5, 6]))
print(grid_index([['m', 'y', 'e'], ['x', 'a', 'm'], ['p', 'l', 'e']], [1, 3, 7, 8]))
print(grid_index([['h', 'e', 'l', 'l'], ['o', 'c', 'o', 'd'], ['e', 'w', 'a', 'r'], ['r', 'i', 'o', 'r']],
                      [5, 7, 9, 3, 6, 6, 8, 8, 16, 13]))
```

#### Output 

```
myexample
mam
mepl
ooelccddrr
```

---

#### Solution

```python
from itertools import chain
def grid_index(grid, indexes):
    d = {k: v for k, v in enumerate(chain.from_iterable(grid), 1)}
    return ''.join(d.get(i) for i in indexes)
```

---

[Codewars link](https://www.codewars.com/kata/5f5802bf4c2cc4001a6f859e)
