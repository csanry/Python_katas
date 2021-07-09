## Create phone number, 6kyu

**Instructions**

- Write a function that accepts an array of 10 integers (between 0 and 9)

- Return a string of those numbers in the form of a phone number.

- Format: (XXX) XXX-XXXX

---

#### Test cases

```python
print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
```

#### Output 
```
(123) 456-7890
```

---

#### Solution

```python
def create_phone_number(n):
    st = ''.join(map(str, n))
    return f"({st[:3]}) {st[3:6]}-{st[6:]}"
```

---


[Codewars link](https://www.codewars.com/kata/525f50e3b73515a6db000b83)
