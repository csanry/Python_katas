## Sum of Digits / Digital root - 6kyu

**Instructions**

- Digital root is the recursive sum of all the digits in a number.

- Given `n`, take the sum of the digits of `n`.

- If that value has more than one digit, continue reducing in this way until a single-digit number is produced.

- The input will be a non-negative integer.

---

#### Test cases

```python
print(digital_root(16))
print(digital_root(942))
print(digital_root(132189))
print(digital_root(493193))
```

#### Output

```
7
6
6
2
```

---

#### Solution

```python
def digital_root(n):
    while n > 9:
        n = sum(map(int, str(n)))
    return n

# recursive solution
def digital_root(n):
    if n < 10:
        return n
    return digital_root(sum(map(int, str(n))))

# The digital root of a number is equal to the remainder when that number is divided by 9.
# If the remainder is -1 and the number is greater than 0, then the digital root is 9. If the number is 0, then the digital root of the number is 0.
def digital_root(n):
    # If n % 9 != 0 return n % 9. Otherwise return n (if n == 0) or 9 (if n != 0).
    return n % 9 or n and 9
```

---

[Codewars link](https://www.codewars.com/kata/541c8630095125aba6000c00)
