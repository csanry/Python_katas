## Shaving the Beard - 7kyu

**Instructions**

- Given a beard represented as an array of arrays, is to trim the beard as follows:

```
['|', 'J', '|', '|'],
['|', '|', '|', 'J'],
['...', '...', '...', '...']
```

- Trim any curled hair: replace 'J' with '|'.

- Trim any hair from the chin (last array): replace '|' or 'J' with '...'.

- All sub arrays will be same length. Return the corrected array of arrays.

---

#### Test cases

```python
print(trim([["J", '|'], ["J", '|'], ["...", '|']]))
print(trim([["J", "|", "J"], ["J", "|", "|"], ["...", "|", "J"]]))
print(trim([["J", "|", "J", "J"], ["J", "|", "|", "J"], ["...", "|", "J", "|"]]))
```

#### Output

```
[['|', '|'], ['|', '|'], ['...', '...']]
[['|', '|', '|'], ['|', '|', '|'], ['...', '...', '...']]
[['|', '|', '|', '|'], ['|', '|', '|', '|'], ['...', '...', '...', '...']]
```

---

#### Solution

```python
def trim(beard):
    res = [[*map(lambda x: x.replace('J', '|'), arr)] for arr in beard]
    res[-1] = ['...'] * len(res[-1])
    return res
```

---

[Codewars link](https://www.codewars.com/kata/57efa1a2108d3f73f60000e9)
