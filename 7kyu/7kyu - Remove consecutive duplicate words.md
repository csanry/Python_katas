## Remove consecutive duplicate words - 7kyu

**Instructions**

- Remove all consecutive duplicate words from a string, leaving only first words entries.

**Example**

```
"alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta"
--> "alpha beta gamma delta alpha beta gamma delta"
```

---

#### Test cases

```python
string = 'alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'
print(remove_consecutive_duplicates(string))
```

#### Output

```
alpha beta gamma delta alpha beta gamma delta
```

---

#### Solution

```python
from itertools import groupby
def remove_consecutive_duplicates(s):
    return ' '.join(k for k, _ in groupby(s.split()))
```

---

[Codewars link](https://www.codewars.com/kata/5b39e91ee7a2c103300018b3)
