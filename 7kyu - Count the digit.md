## Count the Digit - 7kyu

**Instructions**

- Take an integer `n (n >= 0)` and a digit `d (0 <= d <= 9)` as an integer.

- Square all numbers `k (0 <= k <= n)` between 0 and n.

- Count the numbers of digits d used in the writing of all the `k**2`.

---

#### Test cases

```python
print(nb_dig(5750, 0))
print(nb_dig(11011, 2))
print(nb_dig(12224, 8))
print(nb_dig(11549, 1))
```

#### Output 
```
4700
9481
7733
11905
```

---

#### Solution

```python
def nb_dig(n, d):
    return ''.join(str(a ** 2) for a in range(n + 1)).count(str(d))
```

---

[Codewars link](https://www.codewars.com/kata/566fc12495810954b1000030)
