## Chuck Norris V - Body count - 7kyu

**Instructions**

- To stop having to count like a mere mortal chuck developed his own special code using the hairs on his beard. You do not need to know the details of how it works, you simply need to know that the format is as follows: 'A8A8A8A8A8.-A%8.88.'

- In Chuck's code, 'A' can be any capital letter and '8' can be any number 0-9 and any %, - or . symbols must not be changed.

- Your task is to use regex to verify if the number is a genuine Chuck score.

- Return true if the provided count passes, and false if it does not.

- The pattern only needs to appear within the text. The full input can be longer, i.e. the pattern can be surrounded by other characters.

---

#### Test cases

```python
print(body_count('A6C2E5Z9A4.-F%8.08.'))
print(body_count('d G8H1E2O9N3.-W%8.56. f'))
print(body_count('B4A1D1I8B4.-E%8.76.'))
print(body_count('ffr65A C8K4D9U7V5.-Y%8.00.'))
print(body_count(' 76     B2L4D0A8C6.-T%8.90.       lkd'))
print(body_count('B2L4D0A8C6.-T%8.90'))
print(body_count('B2L4D0AFC6.-T%8.90.'))
```

#### Output

```
True
True
True
True
True
False
False
```

---

#### Solution

```python
import re

def body_count(code):
    return bool(re.search(r'([A-Z]\d){5}\.-[A-Z]%\d\.\d{2}\.', code))
```

---

[Codewars link](https://www.codewars.com/kata/57066ad6cb72934c8400149e)
