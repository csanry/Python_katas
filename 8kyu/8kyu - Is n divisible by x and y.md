## Is n divisible by x and y? - 8kyu

**Instructions**

- Create a function that checks if a number n is divisible by two numbers x AND y.

- All inputs are positive, non-zero digits.

---

#### Test cases

```python
print(is_divisible(3, 2, 2))
print(is_divisible(3, 3, 4))
print(is_divisible(12, 3, 4))
print(is_divisible(8, 3, 4))
```

#### Output

```
False
False
True
False
```

---

#### Solution

```python
def is_divisible(n, x, y):
    return n % x == 0 and n % y == 0
```

---

[Codewars link](https://www.codewars.com/kata/5545f109004975ea66000086)
