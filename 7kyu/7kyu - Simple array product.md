## Simple array product - 7kyu

**Instructions**

- In this Kata, you will be given a multi-dimensional array containing 2 or more sub-arrays of integers.

- Your task is to find the maximum product that can be formed by taking any one element from each sub-array.

---

#### Test cases

```python
print(solve([[1, 2],[3, 4]]))
print(solve([[10,-15],[-1,-3]]))
print(solve([[-1,2,-3,4],[1,-2,3,-4]]))
print(solve([[-11,-6],[-20,-20],[18,-4],[-20, 1]]))
print(solve([[14,2],[0,-16],[-12,-16]]))
print(solve([[-3,-4],[1,2,-3]]))
```

#### Output

```
8
45
12
17600
3584
12
```

---

#### Solution

```python
from itertools import product
from functools import reduce
from operator import mul

def solve(arr):
    return max(reduce(mul, prod) for prod in product(*arr))
```

---

[Codewars link](https://www.codewars.com/kata/5d0365accfd09600130a00c9)
