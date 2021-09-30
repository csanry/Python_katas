## Convert integer to binary - 7kyu

**Instructions**

- Given an integer as an argument, return its binary form.

- Notes: negative numbers should be handled as two's complement; assume all numbers are integers stored using 4 bytes (or 32 bits).

- Your output should ignore leading 0s.

---

#### Test cases

```python
print(to_binary(2))
print(to_binary(3))
print(to_binary(4))
print(to_binary(-3))
print(to_binary(0))
```

#### Output 
```
10
11
100
11111111111111111111111111111101
0
```

---

#### Solution

```python
def to_binary(n):
    return bin(n if n >= 0 else (2 ** 32) + n)[2:]
```

---

[Codewars link](https://www.codewars.com/kata/55606aeebf1f0305f900006f)
