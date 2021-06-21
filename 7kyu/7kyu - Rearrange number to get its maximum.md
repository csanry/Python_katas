## Rearrange Number to Get its Maximum - 7kyu

**Instructions**

- Create a function that takes one positive three digit integer and rearranges its digits to get the maximum possible number. 

- Assume that the argument is an integer. 

- Return null if the argument is not valid.

---

#### Test cases

```python
print(max_redigit(123))
print(max_redigit(555))
print(max_redigit(-1))
print(max_redigit(0))
print(max_redigit(99))
print(max_redigit(1000))
```

#### Output 

```
321
555
None
None
None
None
```

---

#### Solution

```python
def max_redigit(num):
    return int(''.join(sorted(str(num), reverse=True))) if 99 < num < 1000 else None
```

---

[Codewars link](https://www.codewars.com/kata/563700da1ac8be8f1e0000dc)
