## All inclusive - 7kyu

**Instructions**

- Given a string `strng` and an array of strings `arr`

- Output `True` if all rotations of `strng` are included in `arr`, `False` otherwise.

---

#### Test cases

```python
print(contain_all_rots("", []))
print(contain_all_rots("", ["bsjq", "qbsj"]))
print(contain_all_rots("bsjq", ["bsjq", "qbsj", "sjqb", "twZNsslC", "jqbs"]))
print(contain_all_rots("XjYABhR", ["TzYxlgfnhf", "yqVAuoLjMLy", "BhRXjYA", "YABhRXj", "hRXjYAB", "jYABhRX", "XjYABhR", "ABhRXjY"]))
```

#### Output
```
True
True
True
False
```

---

#### Solution

```python
def contain_all_rots(strng, arr):
    return all(strng[i:] + strng[:i] in arr for i in range(len(strng)))
```

---

[Codewars link](https://www.codewars.com/kata/5700c9acc1555755be00027e)
