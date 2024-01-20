## Duplicate Encoder - 6kyu

**Instructions**

- The goal of this exercise is to convert a string to a new string where each character in the new string is:

- "(" if that character appears only once in the original string.

- ")" if that character appears more than once in the original string.

- Ignore capitalization when determining if a character is a duplicate.

---

#### Test cases

```python
print(duplicate_encoder('din'))
print(duplicate_encoder('recede'))
print(duplicate_encoder('Success'))
print(duplicate_encoder('(( @'))
```

#### Output

```
(((
()()()
)())())
))((
```

---

#### Solution

```python
from collections import Counter

def duplicate_encoder(word):
    cnt = Counter(word.lower())
    return ''.join('(' if cnt[c] == 1 else ')' for c in word.lower())
```

---

[Codewars link](https://www.codewars.com/kata/54b42f9314d9229fd6000d9c)
