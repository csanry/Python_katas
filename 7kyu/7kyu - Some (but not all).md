## Some (but not all) - 7kyu

**Instructions**

- Your task is to create a function that given a sequence and a predicate, returns `True` if only some (but not all) the elements in the sequence are `True` after applying the predicate

---

#### Test cases

```python
print(some_but_not_all('abcdefg&%$', str.isalpha))
print(some_but_not_all('&%$=', str.isalpha))
print(some_but_not_all('abcdefg', str.isalpha))
print(some_but_not_all([4, 1], lambda x: x>3))
print(some_but_not_all([1, 1], lambda x: x>3))
print(some_but_not_all([4, 4], lambda x: x>3))
```

#### Output
```
True
False
False
True
False
False
```

---

#### Solution

```python
def some_but_not_all(seq, pred):
    return any(map(pred, seq)) and not all(map(pred, seq))
```

---


[Codewars link](https://www.codewars.com/kata/60dda5a66c4cf90026256b75)
