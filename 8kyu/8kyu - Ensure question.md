## Ensure question - 8kyu

**Instructions**

- Given a string, write a function that returns the string with a question mark ("?") appended to the end.

- If the original string already ends with a question mark returns the original string.

---

#### Test cases

```python
print(ensure_question(''))
print(ensure_question('Yes'))
print(ensure_question('No?'))
print(ensure_question('Well??'))
```

#### Output 

```
?
Yes?
No?
Well??
```

---

#### Solution

```python
def ensure_question(s):
    return s if s.endswith('?') else f'{s}?'
```

---

[Codewars link](https://www.codewars.com/kata/5866fc43395d9138a7000006)
