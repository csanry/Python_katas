## Sum of a Sequence [Hard-Core Version] - 6kyu

**Instructions**

- Sum all the numbers from the first parameter being the beginning to the second parameter being the upper limit (possibly included), going in steps expressed by the third parameter:

```
sequence_sum(2, 2, 2) # 2
sequence_sum(2, 6, 2) # 12 (= 2 + 4 + 6)
sequence_sum(1, 5, 1) # (= 1 + 2 + 3 + 4 + 5)
sequence_sum(1, 5, 3) # 5 (= 1 + 4)
```

- If it is an impossible sequence (with the beginning being larger the end and a positive step or the other way around), just return 0.

---

#### Test cases

```python
print(sequence_sum(-1, -5, -3))
print(sequence_sum(780, 6851543, 5))
print(sequence_sum(20, 673388797, 5))
```

#### Output 
```
-5
4694363402480
45345247259849570
```

---

#### Solution

```python
def sequence_sum(b, e, step):
    n = (e - b) // step
    return (n+1) * (2 * b + n * step) // 2 if n >= 0 else 0
```

---


[Codewars link](https://www.codewars.com/kata/587a88a208236efe8500008b)
