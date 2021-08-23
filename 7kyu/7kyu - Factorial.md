## Factorial - 7kyu

**Instructions**

- Calculate the factorial for a given input.

- If the input is below 0 or above 12 return a ValueError.

---

#### Test cases

```python
print(factorial(0))
print(factorial(5))
print(factorial(8))
print(factorial(10))
```

#### Output 
```
1
120
40320
3628800
```

---

#### Solution

```python
import math 
def factorial(n): 
    if n < 0 or n > 12: 
        raise ValueError
    return math.factorial(n)
```

---

[Codewars link](https://www.codewars.com/kata/54ff0d1f355cfd20e60001fc)
