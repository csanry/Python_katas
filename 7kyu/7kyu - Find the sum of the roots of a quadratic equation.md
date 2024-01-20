## Find the sum of the roots of a quadratic equation - 7kyu

**Instructions**

- Implement function which will return sum of roots of a quadratic equation rounded to 2 decimal places if there are any possible roots, else return `None`.

- If you use discriminant, when discriminant = 0, x1 = x2 = root => return sum of both roots.

- There will always be valid arguments.

---

#### Test cases

```python
print(roots(6, 3, 8))
print(roots(2, 11, -6))
print(roots(5, -8, 3))
print(roots(6, 4, 9))
print(roots(1, -2, -5.25))
```

#### Output

```
None
-5.5
1.6
None
2.0
```

---

#### Solution

```python
def roots(a, b, c):
    return round(-b/a, 2) if b**2 - 4*a*c >= 0 else None
```

---

[Codewars link](https://www.codewars.com/kata/57d448c6ba30875437000138)
