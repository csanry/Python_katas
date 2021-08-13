## Plus - minus - plus - plus - ... - Count - 7kyu

**Instructions**

- Count how often the sign changes in the array.

---

#### Test cases

```python
print(catch_sign_change([1, 3, 4, 5]))
print(catch_sign_change([1, -3, -4, 0, 5]))
print(catch_sign_change([]))
print(catch_sign_change([-47,84,-30,-11,-5,74,77]))
```

#### Output 
```
0
2
0
3
```

---

#### Solution

```python
def catch_sign_change(lst):
    return sum((a < 0) != (b < 0) for (a, b) in zip(lst, lst[1:]))
```

---

[Codewars link](https://www.codewars.com/kata/5bbb8887484fcd36fb0020ca)
