## Is a number prime? - 6kyu

**Instructions**

- Define a function that takes one integer argument and returns a boolean value depending on if the integer is a prime.

- A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

---

#### Test cases

```python
print(is_prime(0))
print(is_prime(1))
print(is_prime(2))
print(is_prime(73))
print(is_prime(75))
print(is_prime(-1))
```

#### Output 

```
False
False
True
True
False
False
```

---

#### Solution

```python
# given only one even prime (2), we only need to iterate over the odd integers up to the sqrt of n 
# to find at least one divisor (if exists)
from math import sqrt, floor

def is_prime(n):
    return all(n % d for d in range(3, floor(sqrt(n)) + 1, 2)) if n > 2 and n % 2 else n == 2
```

---

[Codewars link](https://www.codewars.com/kata/5262119038c0985a5b00029f/)
