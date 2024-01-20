## Regex count lowercase letters - 8kyu

**Instructions**

- Count the total number of lowercase letters in a string using regex.

---

#### Test cases

```python
print(lowercase_count("abc"))
print(lowercase_count("abcABC123"))
print(lowercase_count("abcABC123!@#$%^&*()_-+=}{[]|\':;?/>.<,~"))
print(lowercase_count(""))
print(lowercase_count("ABC123!@#$%^&*()_-+=}{[]|\':;?/>.<,~"))
print(lowercase_count("abcdefghijklmnopqrstuvwxyz"))
```

#### Output
```
3
3
3
0
0
26
```

---

#### Solution

```python
def lowercase_count(strng):
    import re
    return len(re.findall(r'[a-z]', strng))
```

---

[Codewars link](https://www.codewars.com/kata/56a946cd7bd95ccab2000055)
