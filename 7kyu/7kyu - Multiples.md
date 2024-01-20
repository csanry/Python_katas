## Multiples! - 7kyu

**Instructions**

- Take a value `x` and returns `Bang` if the number is divisible by 3, `Boom` if it is divisible by 5, `BangBoom` if it divisible by 3 and 5, and `Miss` if it isn't divisible by any of them.

- Note: Your program should only return one value

---

#### Test cases

```python
print(multiple(30))
print(multiple(3))
print(multiple(98))
print(multiple(65))
print(multiple(23))
print(multiple(15))
```

#### Output

```
BangBoom
Bang
Miss
Boom
Miss
BangBoom
```

---

#### Solution

```python
def multiple(x):
    return ('', 'Bang')[x % 3 == 0] + ('', 'Boom')[x % 5 == 0] or 'Miss'
```

---

[Codewars link](https://www.codewars.com/kata/55a8a36703fe4c45ed00005b)
