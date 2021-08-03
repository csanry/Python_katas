## Power of 4 - 7kyu

**Instructions**

- Write a function that returns if a given number is a power of 4.

---

#### Test cases

```python
print(power_of_4(64))
print(power_of_4('pippi'))
print(power_of_4(-25))
print(power_of_4(256))
print(power_of_4(True))
```

#### Output 
```
True
False
False
True
False
```

---

#### Solution

```python
def power_of_4(n):
    from math import pow, log
    return pow(4, round(log(n, 4))) == n if type(n) in (int, float) and n > 0 else False
```

---

[Codewars link](https://www.codewars.com/kata/544d114f84e41094a9000439)
