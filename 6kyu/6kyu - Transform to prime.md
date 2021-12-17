## Transform to Prime - 6kyu

**Instructions**

- Given a list of n integers, find the minimum number to be inserted into a list, so that sum of all elements of list should equal the closest prime number.

- List size is at least 2.

- List numbers are always positive and could contain duplicates.

- The sum of numbers in the new list should equal to the closest prime number.

---

#### Test cases

```python
print(minimum_number([3, 1, 2]))
print(minimum_number([5, 2]))
print(minimum_number([1, 1, 1]))
print(minimum_number([2, 12, 8, 4, 6]))
print(minimum_number([50, 39, 49, 6, 17, 28]))
```

#### Output 

```
1
0
0
5
2
```

---

#### Solution

```python
from itertools import count
from math import sqrt, floor

def is_prime(n): 
    return n == 2 or n % 2 and all(n % d for d in range(3, floor(sqrt(n)) + 1, 2))

def minimum_number(numbers):
    s = sum(numbers)
    return next(x for x in count(0) if is_prime(s + x))
```

---

[Codewars link](https://www.codewars.com/kata/5a946d9fba1bb5135100007c)
