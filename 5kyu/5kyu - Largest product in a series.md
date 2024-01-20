## Largest product in a series - 5kyu

**Instructions**

- Complete the function so that it'll find the greatest product of five consecutive digits in the given string of digits.

- The input string always has more than 5 digits

---

#### Test cases

```python
print(greatest_product("123834539327238239583"))
print(greatest_product("395831238345393272382"))
print(greatest_product("92494737828244222221111111532909999"))
print(greatest_product("92494737828244222221111111532909999"))
print(greatest_product("02494037820244202221011110532909999"))
```

#### Output
```
3240
3240
5292
5292
0
```

---

#### Solution

```python
from functools import reduce
from operator import mul

def greatest_product(n):
    prods = []
    for i in range(len(n) - 4):
        prods.append(reduce(mul, map(int, n[i:i+5])))
    return max(prods)
```

---


[Codewars link](https://www.codewars.com/kata/529872bdd0f550a06b00026e)
