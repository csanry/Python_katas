## Digitize - 7kyu

**Instructions**

- Given a non-negative integer, return an array / a list of the individual digits in order.

---

#### Test cases

```python
print(digitize(123))
print(digitize(1))
print(digitize(0))
print(digitize(1230))
print(digitize(8675309))
```

#### Output 

```
[1, 2, 3]
[1]
[0]
[1, 2, 3, 0]
[8, 6, 7, 5, 3, 0, 9]
```

---

#### Solution

```python
def digitize(n): 
    return [*map(int, str(n))]
```

---

[Codewars link](https://www.codewars.com/kata/5417423f9e2e6c2f040002ae)
