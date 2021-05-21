## Sum of Multiples - 8kyu

**Instructions**

- Find the sum of all multiples of `n` below `m`.

- `m` is excluded from the multiples.

```
sum_mul(2, 9)   ==> 2 + 4 + 6 + 8 = 20
sum_mul(3, 13)  ==> 3 + 6 + 9 + 12 = 30
sum_mul(4, 123) ==> 4 + 8 + 12 + ... = 1860
sum_mul(4, -7)  ==> "INVALID"
```

---

#### Test cases

```python
print(sum_mul(0, 0))
print(sum_mul(2, 9))
print(sum_mul(4, -7))
```

#### Output 

```
INVALID
20
INVALID
```

---

#### Solution

```python
def sum_mul(n, m):
    return sum(range(n, m, n)) if n > 0 < m else 'INVALID'
```

---

[Codewars link](https://www.codewars.com/kata/57241e0f440cd279b5000829)
