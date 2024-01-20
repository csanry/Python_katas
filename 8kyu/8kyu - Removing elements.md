## Removing elements - 8kyu

**Instructions**

- Given an array, remove every other element from the array.

---

#### Test cases

```python
print(remove_every_other(['Hello', 'Goodbye', 'Hello Again']))
print(remove_every_other([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
```

#### Output

```
['Hello', 'Hello Again']
[1, 3, 5, 7, 9]
```

---

#### Solution

```python
def remove_every_other(lst):
    return lst[::2]
```

---

[Codewars link](https://www.codewars.com/kata/5769b3802ae6f8e4890009d2)
