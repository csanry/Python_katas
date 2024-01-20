## Duplicate sandwich - 7kyu

**Instructions**

- Given a list consisting of unique elements except for one thing that appears twice:

- Output a list of everything in between both occurrences of this element in the list.

- All elements will be the same datatype.

- All used elements will be hashable.

---

#### Test cases

```python
print(duplicate_sandwich([0, 1, 2, 3, 4, 5, 6, 1, 7, 8]))
print(duplicate_sandwich(['None', 'Hello', 'Example', 'hello', 'None', 'Extra']))
print(duplicate_sandwich([0, 0]))
print(duplicate_sandwich([True, False, True]))
print(duplicate_sandwich(['e', 'x', 'a', 'm', 'p', 'l', 'e']))
```

#### Output
```
[2, 3, 4, 5, 6]
['Hello', 'Example', 'hello']
[]
[False]
['x', 'a', 'm', 'p', 'l']
```

---

#### Solution

```python
def duplicate_sandwich(arr):
    start, end = [idx for idx, val in enumerate(arr) if arr.count(val) == 2]
    return arr[start+1: end]
```

---

[Codewars link](https://www.codewars.com/kata/5f8a15c06dbd530016be0c19)
