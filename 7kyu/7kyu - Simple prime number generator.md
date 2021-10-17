## Simple Prime Number Generator - 7kyu

**Instructions**

- Your task here is to generate a list of prime numbers, starting from 2 to `n`.
 
---

#### Test cases

```python
print(generate_primes(25))
print(generate_primes(55))
print(generate_primes(150))
```

#### Output 

```
[2, 3, 5, 7, 11, 13, 17, 19, 23]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149]
```

---

#### Solution

```python
from math import sqrt
from itertools import islice, count
def is_prime(n):
    return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n)-1)))

def generate_primes(x):
    return [*filter(is_prime, range(2, x+1))]
```

---

[Codewars link](https://www.codewars.com/kata/58fa5e33a6d84c1324000207)
