## Evens and Odds - 7kyu

**Instructions**

- This kata is about converting numbers to their binary or hexadecimal representation.

- If a number is even, convert it to binary.

- If a number is odd, convert it to hex.

---

#### Test cases

```python
print(evens_and_odds(2))
print(evens_and_odds(13))
```

#### Output 
```
10
d
```

---

#### Solution

```python
def evens_and_odds(n):
    return hex(n)[2:] if n%2 else bin(n)[2:]
```

---

[Codewars link](https://www.codewars.com/kata/583ade15666df5a64e000058)
