## Array madness - 8kyu

**Instructions**

- Given two integer arrays `a, b`, both of `length >= 1`, create a program that returns if the sum of the squares of each element in `a` is strictly greater than the sum of the cubes of each element in `b`.

---

#### Test cases

```python
print(array_madness([4, 5, 6], [1, 2, 3]))
print(array_madness([1, 2, 3], [4, 5, 6]))
```

#### Output 

```
True
False
```

---

#### Solution

```python
def array_madness(a,b):
    return sum(map(lambda x: x ** 2, a)) > sum(map(lambda y: y ** 3, b))
```

---

[Codewars link](https://www.codewars.com/kata/56ff6a70e1a63ccdfa0001b1)
