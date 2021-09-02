## The reject() function - 7kyu

**Instructions**

- Implement a function which filters out array values which satisfy the given predicate.

---

#### Test cases

```python
print(reject([1, 2, 3, 4, 5, 6], lambda x: x%2==0))
print(reject(['a', 'b', 3, 'd'], lambda x: type(x)==int))
print(reject(['a', 'b', 3, 'd'], lambda x: type(x)==str))
```

#### Output 
```
[1, 3, 5]
['a', 'b', 'd']
[3]
```

---

#### Solution

```python
def reject(seq, predicate):
    from itertools import filterfalse
    return list(filterfalse(predicate, seq))
```

---

[Codewars link](https://www.codewars.com/kata/52988f3f7edba9839c00037d)
