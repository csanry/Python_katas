## Satisfying Numbers - 7kyu

**Instructions**

- 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

- Find the smallest positive number that is evenly divisible by all of the numbers from 1 to n `(n <= 40)`.

---

#### Test cases

```python
print(smallest(1))
print(smallest(2))
print(smallest(3))
print(smallest(4))
print(smallest(5))
print(smallest(6))
print(smallest(7))
print(smallest(8))
print(smallest(9))
print(smallest(10))
```

#### Output 

```
1
2
6
12
60
60
420
840
2520
2520
```

---

#### Solution

```python
from numpy import lcm

def smallest(n):
    return lcm.reduce(range(1, n+1))
```

---

[Codewars link](https://www.codewars.com/kata/55e7d9d63bdc3caa2500007d)
