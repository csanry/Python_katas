## Basic Sequence Practice - 7kyu

**Instructions**

- Generate a sequence with the pattern: "the nth term is the sum of numbers from 0 to n, inclusive".

```
[ 0,  1,    3,      6,   ...]
  0  0+1  0+1+2  0+1+2+3 ...
```

- When n < 0 return the sequence with negative terms.

---

#### Test cases

```python
print(sum_of_n(3))
print(sum_of_n(1))
print(sum_of_n(0))
print(sum_of_n(-4))
```

#### Output

```
[0, 1, 3, 6]
[0, 1]
[0]
[0, -1, -3, -6, -10]
```

---

#### Solution

```python
from itertools import accumulate
def sum_of_n(n):
    step = 1 if n >= 0 else -1
    return [*accumulate(range(0, n+step, step))]
```

---

[Codewars link](https://www.codewars.com/kata/5436f26c4e3d6c40e5000282/train/python)
