## Find the capitals - 7kyu

**Instructions**

- Write a function that takes a single string as an argument.

- The function must return an ordered list containing the indexes of all capital letters in the string.

---

#### Test cases

```python
print(capitals('CodEWaRs'))
print(capitals('lQUQcVUAkVplXpdstrg'))
print(capitals('Xtzhl'))
print(capitals('YwzaGfiYtz'))
```

#### Output

```
[0, 3, 4, 6]
[1, 2, 3, 5, 6, 7, 9, 12]
[0]
[0, 4, 7]
```

---

#### Solution

```python
def capitals(word):
    return [i for i, v in enumerate(word) if v.isupper()]
```

---

[Codewars link](https://www.codewars.com/kata/539ee3b6757843632d00026b)
