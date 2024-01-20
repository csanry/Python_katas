## Count the divisors of a number - 7kyu

**Instructions**

- Count the number of divisors of a positive integer n.

---

#### Test cases

```python
print(divisors(286349))
print(divisors(137768))
print(divisors(338724))
print(divisors(486666))
```

#### Output
```
8
16
27
24
```

---

#### Solution

```python
import math
def divisors(n):
    return sum(1 if i*i==n else 2 for i in range(1, math.floor(math.sqrt(n)+1)) if not n%i)
```

---

[Codewars link](https://www.codewars.com/kata/542c0f198e077084c0000c2e)
