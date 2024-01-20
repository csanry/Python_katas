## Return the first M multiples of N - 7kyu

**Instructions**

- Implement a function, multiples(m, n), which returns an array of the first `m` multiples of the real number `n`.

- Assume that `m` is a positive integer.

---

#### Test cases

```python
print(multiples(3, 5))
print(multiples(1, 3.14))
print(multiples(5, -1))
```

#### Output
```
[5, 10, 15]
[3.14]
[-1, -2, -3, -4, -5]
```

---

#### Solution

```python
def multiples(m, n):
    return [i * n for i in range(1, m+1)]
```

---

[Codewars link](https://www.codewars.com/kata/593c9175933500f33400003e)
