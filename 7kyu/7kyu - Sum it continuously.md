## Sum it continuously - 7kyu

**Instructions**

- Write a function that will be able to sum elements of list continuously and return a new list of sums.

```
add [1,2,3,4,5] == [1, 3, 6, 10, 15], because it's calculated like
this : [1, 1 + 2, 1 + 2 + 3, 1 + 2 + 3 + 4, 1 + 2 + 3 + 4 + 5]
```

---

#### Test cases

```python
print(add([1,2,3,4,5]))
print(add([20,21,22,23,24,25]))
print(add([2,4,6,8,10]))
print(add([1,4,9,16,25,36]))
print(add([1,8,27,64,125]))
```

#### Output
```
[1, 3, 6, 10, 15]
[20, 41, 63, 86, 110, 135]
[2, 6, 12, 20, 30]
[1, 5, 14, 30, 55, 91]
[1, 9, 36, 100, 225]
```

---

#### Solution

```python
from itertools import accumulate
def add(lst):
    return list(accumulate(lst))
```

---

[Codewars link](https://www.codewars.com/kata/59b44d00bf10a439dd00006f)
