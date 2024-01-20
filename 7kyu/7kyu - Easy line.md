## Easy line - 7kyu

**Instructions**

- Calculate the sum of the squares of the binomial coefficients on a given horizontal line.

- The function will take `n (with n >= 0)` as a parameter.

---

#### Test cases

```python
easyline(0)
easyline(4)
easyline(11)
```

#### Output
```
1
70 # 1 + 16 + 36 + 16 + 1
705432
```

---

#### Solution

```python
import math

def easyline(n):
    return math.factorial(n * 2) // math.factorial(n)**2
```

---

[Codewars link](https://www.codewars.com/kata/56e7d40129035aed6c000632)
