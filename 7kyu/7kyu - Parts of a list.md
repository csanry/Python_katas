## Kata name - Xkyu

**Instructions**

- Write a function `partlist` that gives all the ways to divide a list (an array) of at least two elements into two non-empty parts.

- Each two non empty parts will be in a pair.

- Each part will be in a string.

- Elements of a pair must be in the same order as in the original array.

---

#### Test cases

```python
print(partlist(["I", "wish", "I", "hadn't", "come"]))
print(partlist(["cdIw", "tzIy", "xDu", "rThG"]))
print(partlist(["vJQ", "anj", "mQDq", "sOZ"]))
```

#### Output 

```
[('I', "wish I hadn't come"), ('I wish', "I hadn't come"), ('I wish I', "hadn't come"), ("I wish I hadn't", 'come')]
[('cdIw', 'tzIy xDu rThG'), ('cdIw tzIy', 'xDu rThG'), ('cdIw tzIy xDu', 'rThG')]
[('vJQ', 'anj mQDq sOZ'), ('vJQ anj', 'mQDq sOZ'), ('vJQ anj mQDq', 'sOZ')]
```

---

#### Solution

```python
def partlist(arr):
    return [(' '.join(arr[:i]), ' '.join(arr[i:])) for i in range(1, len(arr))]
```

---

[Codewars link](https://www.codewars.com/kata/56f3a1e899b386da78000732)
