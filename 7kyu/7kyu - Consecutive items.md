## Consecutive items - 7kyu

**Instructions**

- You are given a list of unique integers `arr`, and two integers `a` and `b`.

- Your task is to find out whether or not `a` and `b` appear consecutively in `arr`, and return a boolean value (`True` if `a` and `b` are consecutive, `False` otherwise).

- It is guaranteed that `a` and `b` are both present in `arr`.

---

#### Test cases

```python
print(consecutive([1, 3, 5, 7], 3, 7))
print(consecutive([1, 3, 5, 7], 3, 1))
print(consecutive([1, 6, 9, -3, 4, -78, 0], -3, 4))
```

#### Output 
```
False
True
True
```

---

#### Solution

```python
def consecutive(arr, a, b):
    return any(a in (x, y) and b in (x, y) for x, y in zip(arr, arr[1:]))
    # alternative
    # return abs(arr.index(a) - arr.index(b)) == 1
```

---


[Codewars link](https://www.codewars.com/kata/5f6d533e1475f30001e47514/solutions/python)
