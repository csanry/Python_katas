## Jumping number - 7kyu

**Instructions**

- A number is jumping if all adjacent digits in it differ by 1.

- Given a number, return `"Jumping!!"` if the number is jumping else or `"Not!!"`.

---

#### Test cases

```python
print(jumping_number(7))
print(jumping_number(9))
print(jumping_number(79))
print(jumping_number(98))
print(jumping_number(8957))
print(jumping_number(4343456))
print(jumping_number(98789876))
```

#### Output 
```
Jumping!!
Jumping!!
Not!!
Jumping!!
Not!!
Jumping!!
Jumping!!
```

---

#### Solution

```python
def jumping_number(n):
    return ['Jumping!!', 'Not!!'][any(abs(int(a) - int(b)) != 1 for a, b in zip(str(n), str(n)[1:]))]
```

---

[Codewars link](https://www.codewars.com/kata/5a54e796b3bfa8932c0000ed)
