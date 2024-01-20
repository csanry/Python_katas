## Missing values - 7kyu

**Instructions**

- You are given a sequence of positive ints where every element appears three times, except one that appears only once (let's call it x) and one that appears only twice (let's call it y).

- Your task is to find x * x * y.

---

#### Test cases

```python
print(missing_values([1, 1, 1, 2, 2, 3]))
print(missing_values([96, 56, 24, 46, 75, 46, 75, 21, 46, 21, 75, 96, 56, 96, 56]))
print(missing_values([27, 65, 44, 39, 44, 21, 21, 44, 65, 39, 21, 65]))
print(missing_values([66, 4, 80, 66, 4, 83, 97, 81, 19, 4, 80, 51, 83, 81, 83, 66, 51, 80, 97, 81, 97]))
print(missing_values([60, 76, 86, 76, 86, 53, 60, 88, 71, 71, 71, 86, 88, 76, 88, 17, 60, 26, 17, 17, 26, 53, 98, 53]))
print(missing_values([42, 23, 45, 33, 33, 19, 42, 79, 79, 23, 95, 95, 79, 19, 42, 33, 19, 23]))
print(missing_values([4, 74, 41, 41, 41, 88, 63, 35, 35, 4, 88, 13, 63, 74, 63, 88, 4, 74]))
```

#### Output

```
18
12096
28431
18411
249704
192375
5915
```

---

#### Solution

```python
import numpy as np
from collections import Counter

def missing_values(seq):
    return np.product([k ** (3 - v) for k, v in Counter(seq).items()])
```

---

[Codewars link](https://www.codewars.com/kata/58a66c208b88b2de660000c3)
