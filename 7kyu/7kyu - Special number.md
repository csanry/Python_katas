## Special Number - 7kyu

**Instructions**

- A number is a Special Number if it’s digits only consists of 0, 1, 2, 3, 4 or 5

- Given a number determine if it special number or not.

---

#### Test cases

```python
print(special_number(2))
print(special_number(7))
print(special_number(79))
print(special_number(39))
print(special_number(55))
print(special_number(709))
print(special_number(970569))
print(special_number(11350224))
```

#### Output 
```
Special!!
NOT!!
NOT!!
NOT!!
Special!!
NOT!!
NOT!!
Special!!
```

---

#### Solution

```python
def special_number(number):
    return 'NOT!!' if any(int(i) > 5 for i in str(number)) else 'Special!!'
```

---

[Codewars link](https://www.codewars.com/kata/5a55f04be6be383a50000187)
