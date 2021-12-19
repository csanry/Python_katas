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
```

---

[Codewars link](https://www.codewars.com/kata/541c8630095125aba6000c00)
