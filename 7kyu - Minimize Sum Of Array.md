## Minimize Sum Of Array - 7kyu

**Instructions**

- Given an array of integers, find the minimum sum which is obtained from summing each two integers product.

- Array/list will contain positives only.

- Array/list will always has even size.

---

#### Test cases

```python
print(min_sum([5, 4, 2, 3]))
print(min_sum([12, 6, 10, 26, 3, 24]))
print(min_sum([9, 2, 8, 7, 5, 4, 0, 6]))
```

#### Output 
```
22
342
74
```

---

#### Solution

```python
def min_sum(arr):
    arr = sorted(arr)
    return sum(arr[i] * arr[-i-1] for i in range(len(arr)//2))
```

---

[Codewars link](https://www.codewars.com/kata/5a523566b3bfa84c2e00010b)
