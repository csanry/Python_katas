## Simple eviternity numbers - 7kyu

**Instructions**

- An eviternity number is a number which:

    - Contains only digits 8, 5 and 3, and

    - The count of the digit 8 >= count of digit 5 >= count of digit 3.

- The first few eviternity numbers are as follows:

```
[8, 58, 85, 88, 358, 385, 538, 583, 588, 835, 853, 858, 885, 888]
```

- Given two integers, a and b, return the number of eviternity numbers in the range (a, b].

---

#### Test cases

```python
print(solve(0,100))
print(solve(0,1000))
print(solve(0,10000))
print(solve(0,100000))
print(solve(0,500000))
```

#### Output
```
4
14
37
103
148
```

---

#### Solution

```python
from itertools import product
from collections import Counter

def is_evit(n):
    cnt = Counter(n)
    return cnt[8] >= cnt[5] >= cnt[3]

eviternity = [*map(int, (''.join(map(str, digs))
                                for nd in range(1, 7)
                                for digs in product((3, 5, 8), repeat = nd)
                                if is_evit(digs)))]
def solve(a, b):
    return sum(a <= n < b for n in eviternity)
```

---

[Codewars link](https://www.codewars.com/kata/5b93f268563417c7ed0001bd)
