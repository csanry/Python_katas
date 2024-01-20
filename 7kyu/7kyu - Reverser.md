## Reverser - 7kyu

**Instructions**

- Implement the reverse function, which takes in input `n` and reverses it.

- For instance, `reverse(123)` should return `321`.

- You should do this without converting the inputted number into a string.

- Assume that `n` is always a positive integer.

---

#### Test cases

```python
print(reverse(1234))
print(reverse(10987))
print(reverse(1020))
```

#### Output
```
4321
78901
201
```

---

#### Solution

```python
def reverse(n):
    res = 0
    while n > 0:
        res = res * 10 + n % 10; n //= 10
    return res
```

---

[Codewars link](https://www.codewars.com/kata/58069e4cf3c13ef3a6000168)
