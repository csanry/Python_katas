## Testing 1-2-3 - 7kyu

**Instructions**

- Write a function which takes a list of strings and returns each line prepended by the correct number.

- The numbering starts at 1. The format is `n: string`. Notice the colon and space in between.

---

#### Test cases

```python
print(number([]))
print(number(["a", "b", "c"]))
```

#### Output
```
[]
["1: a", "2: b", "3: c"]
```

---

#### Solution

```python
def number(lines):
    return [f'{i}: {v}' for i, v in enumerate(lines, 1)]
```

---

[Codewars link](https://www.codewars.com/kata/54bf85e3d5b56c7a05000cf9)
