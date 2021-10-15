## Random case - 7kyu

**Instructions**

Write a function that will randomly make characters in a string upper or lower.

---

#### Test cases

```python
st = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit'
print(random_case(st))
```

#### Output 

```
# random output
lOReM ipsUm DOlor SiT AmET, coNSECTEtuR ADIPiscING elIt
```

---

#### Solution

```python
import random
def random_case(x):
    return ''.join(random.choice((let.upper(), let.lower())) for let in x)
```

---

[Codewars link](https://www.codewars.com/kata/57073869924f34185100036d)
