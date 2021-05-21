## Is the string uppercase? - 8kyu

**Instructions**

- Create a function to see whether the string is ALL CAPS.

- Spaces and special characters are allowed.

---

#### Test cases

```python
print(is_uppercase("c"))
print(is_uppercase("C"))
print(is_uppercase("hello I AM DONALD"))
print(is_uppercase("HELLO I AM DONALD"))
print(is_uppercase("$%&"))
```

#### Output 

```
False
True
False
True
True
```

---

#### Solution

```python
import re
def is_uppercase(inp):
    return not re.search(r'[a-z]', inp)
```

---

[Codewars link](https://www.codewars.com/kata/56cd44e1aa4ac7879200010b)
