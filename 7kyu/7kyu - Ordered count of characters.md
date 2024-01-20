## Ordered count of characters - 7kyu

**Instructions**

- Count the number of occurrences of each character and return it as a list of tuples in order of appearance.

- Return an empty list for an empty output.

---

#### Test cases

```python
print(ordered_count('abracadabra'))
print(ordered_count('Code Wars'))
```

#### Output
```
[('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)]
[('C', 1), ('o', 1), ('d', 1), ('e', 1), (' ', 1), ('W', 1), ('a', 1), ('r', 1), ('s', 1)]
```

---

#### Solution

```python
def ordered_count(inp):
    from collections import Counter
    return [*Counter(inp).items()]
```

---

[Codewars link](https://www.codewars.com/kata/57a6633153ba33189e000074)
