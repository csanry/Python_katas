## Get decimal part of the given number - 7kyu

**Instructions**

- Write a function that returns only the decimal part of the given number.

- Always return a positive decimal part.

---

#### Test cases

```python
print(get_decimal(4.5))
print(get_decimal(-1.2))
print(get_decimal(10))
```

#### Output 

```
0.5
0.2
0
```

---

#### Solution

```python
def get_decimal(n): 
    return abs(n) % 1
```

---

[Codewars link](https://www.codewars.com/kata/586e4c61aa0428f04e000069/train/python)
