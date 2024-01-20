## Odds ones out! - 7kyu

**Instructions**

- Given a list of numbers that each repeat a certain number of times, remove all numbers that repeat an odd number of times while keeping everything else the same.

```
odd_ones_out([1, 2, 3, 1, 3, 3]) = [1, 1]
# the number 1 appears twice
# the number 2 appears once
# the number 3 appears three times
```

---

#### Test cases

```python
print(odd_ones_out([75, 68, 75, 47, 68]))
print(odd_ones_out([42, 72, 32, 4, 94, 82, 67, 67]))
print(odd_ones_out([100, 100, 5, 5, 100, 50, 68, 50, 68, 50, 68, 5, 100]))
print(odd_ones_out([82, 86, 71, 58, 44, 79, 50, 44, 79, 67, 82, 82, 55, 50]))
```

#### Output
```
[75, 68, 75, 68]
[67, 67]
[100, 100, 100, 100]
[44, 79, 50, 44, 79, 50]
```

---

#### Solution

```python
def odd_ones_out(numbers):
    from collection import Counter
    cnt = Counter(numbers)
    return [i for i in numbers if not cnt[i]&1]
```

---

[Codewars link](https://www.codewars.com/kata/5d376cdc9bcee7001fcb84c0)
