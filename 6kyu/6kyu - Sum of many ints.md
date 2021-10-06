## Sum of many ints - 6kyu

**Instructions**

- For i from 1 to n, do i % m and return the sum.

```
f(n=10, m=5) // returns 20 (1+2+3+4+0 + 1+2+3+4+0)
```

---

#### Test cases

```python
print(f(10, 5))
print(f(20, 20))
print(f(15, 10))
print(f(91955261, 83968173))
```

#### Output 

```
20
190
60
3557223787848294
```

---

#### Solution

```python
def f(n, m):
    div, mod = divmod(n, m)
    cyclesum = (m - 1) * m / 2
    partsum = mod * (mod + 1) / 2
    return (cyclesum * div) + partsum
```

---

[Codewars link](https://www.codewars.com/kata/54c2fc0552791928c9000517/)
