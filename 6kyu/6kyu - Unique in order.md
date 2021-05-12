## Unique In Order - 6kyu

**Instructions**

- Take a sequence as an argument and return a list of items without any elements with the same value next to each other and preserving the original order of elements.

```python
unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD') == ['A', 'B', 'C', 'c', 'A', 'D']
```

---

#### Test cases

```python
print(unique_in_order(''))
print(unique_in_order('ABBCcAD'))
print(unique_in_order('AAAABBBCCDAABBB'))
print(unique_in_order([1, 2, 3, 3, 3, 2]))
```

#### Output 
```
[]
['A', 'B', 'C', 'c', 'A', 'D']
['A', 'B', 'C', 'D', 'A', 'B']
[1, 2, 3, 2]
```

---

#### Solution

```python
from itertools import groupby
def unique_in_order(iterable):
    return [k for k, _ in groupby(iterable)]
```

---

[Codewars link](https://www.codewars.com/kata/54e6533c92449cc251001667)
