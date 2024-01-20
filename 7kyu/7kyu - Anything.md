## Anything - 7kyu

**Instructions**

- Create a class that will make anything True.

---

#### Test cases

```python
print(anything({}) != [])
print(anything('Hello') < 'World')
print(anything(80) > 81)
print(anything(5) == ord)
```

#### Output
```
True
True
True
True
```

---

#### Solution

```python
class anything(object):
    def __init__(self, foo):
        pass
    def __eq__(self, other):
        return True
    __ne__ = __lt__ = __le__ = __gt__ = __ge__ = __eq__
```

---

[Codewars link](https://www.codewars.com/kata/557d9e4d155e2dbf050000aa)
