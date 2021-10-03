## Find factors of a number - 7kyu

**Instructions**

- Create a function that takes a number and finds the factors of it, listing them in descending order in an array.

---

#### Test cases

```python
print(factors(-4))
print(factors(54))
print(factors(100))
print(factors(320))
```

#### Output 
```
-1
[54, 27, 18, 9, 6, 3, 2, 1]
[100, 50, 25, 20, 10, 5, 4, 2, 1]
[320, 160, 80, 64, 40, 32, 20, 16, 10, 8, 5, 4, 2, 1]
```

---

#### Solution

```python
import math
def factors(x):
    if not isinstance(x, int) or x < 1:
        return -1
    seen = set()
    for i in range(1, math.floor(math.sqrt(x)) + 1):
        if x % i == 0:
            seen.add(i)
            seen.add(x // i)
    return sorted(seen)[::-1]
```

---

[Codewars link](https://www.codewars.com/kata/564fa92d1639fbefae00009d)
