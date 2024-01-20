## Numbers in strings - 7kyu

**Instructions**

- Given a string that has lowercase letters and numbers, compare the number groupings and return the largest number.

- Numbers will not have leading zeros.

---

#### Test cases

```python
print(solve('gh12cdy695m1'))
print(solve('2ti9iei7qhr5'))
print(solve('vih61w8oohj5'))
print(solve('f7g42g16hcu5'))
print(solve('lu1j8qbbb85'))
```

#### Output
```
695
9
61
42
85
```

---

#### Solution

```python
import re
def solve(s):
    return max(map(int, re.findall(r'(\d+)', s)))
```

---

[Codewars link](https://www.codewars.com/kata/59dd2c38f703c4ae5e000014)
