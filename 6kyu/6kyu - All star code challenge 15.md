## All Star Code Challenge #15 - 6kyu

**Instructions**

- Create a function that accepts a string argument and returns an array of strings with each letter from the input string being rotated to the end.

```
rotate("Hello") -> ["elloH", "lloHe", "loHel", "oHell", "Hello"]
```

---

#### Test cases

```python
print(rotate("Hello"))
print(rotate(" "))
print(rotate(""))
print(rotate("123"))
```

#### Output

```
['elloH', 'lloHe', 'loHel', 'oHell', 'Hello']
[' ']
[]
['231', '312', '123']
```

---

#### Solution

```python
from collections import deque

def rotate(st):
    dq = deque(st)
    res = []
    for _ in range(len(st)):
        dq.rotate(-1)
        res.append(''.join(dq))
    return res
```

---

[Codewars link](https://www.codewars.com/kata/586560a639c5ab3a260000f3)
