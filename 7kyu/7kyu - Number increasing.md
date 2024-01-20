## Number Increasing - 7kyu

**Instructions**

- Initially a number 1 is written on a board.

- Return if it is possible to reach `n` using a combination of the following operations:

    - Multiply the number by 3.

    - Increase the number by 5.

---

#### Test cases

```python
print(number_increasing(1))
print(number_increasing(2))
print(number_increasing(3))
print(number_increasing(4))
print(number_increasing(5))
print(number_increasing(6))
print(number_increasing(100))
print(number_increasing(101))
print(number_increasing(12345))
print(number_increasing(54321))
```

#### Output

```
True
False
True
False
False
True
False
True
False
True
```

---

#### Solution

```python
def number_increasing(n):
    return n not in {2, 4, 7, 12, 17, 22} and n % 5 != 0
```

---

[Codewars link](https://www.codewars.com/kata/589d1e88e8afb7a85e00004e)
