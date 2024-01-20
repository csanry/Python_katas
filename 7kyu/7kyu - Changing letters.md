## Changing letters - 7kyu

**Instructions**

- When provided with a string, capitalize all vowels.

- Note: Y is not a vowel.

---

#### Test cases

```python
print(swap("HelloWorld!"))
print(swap("Sunday"))
```

#### Output
```
HEllOWOrld!
SUndAy
```

---

#### Solution

```python
def swap(st):
    return ''.join(c.upper() if c in 'aeiou' else c for c in st)
    # alternative > str.translate method followed by str.maketrans() function
    # return st.translate(str.maketrans('aeiou', 'AEIOU'))
```

---

[Codewars link](https://www.codewars.com/kata/5831c204a31721e2ae000294)
