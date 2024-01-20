## What's up next? - 8kyu

**Instructions**

- Given a sequence of items and a specific item in that sequence, return the item immediately following the item specified. If the item occurs more than once in a sequence, return the item after the first occurrence.

- This should work for a sequence of any type.

- When the item isn't present or nothing follows it, return `None`.

---

#### Test cases

```python
print(next_item([1, 2, 3, 4, 5, 6, 7, 8], 5))
print(next_item(['a', 'b', 'c'], 'd'))
print(next_item(['a', 'b', 'c'], 'c'))
print(next_item('testing', 't'))
print(next_item(iter(range(1, 30000)), 12))
```

#### Output
```
6
None
None
e
13
```

---

#### Solution

```python
def next_item(xs, item):
    it = iter(xs)
    for i in it:
        if i == item:
            break
    return next(it, None)
```

---

[Codewars link](https://www.codewars.com/kata/542ebbdb494db239f8000046)
