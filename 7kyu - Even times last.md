## Evens times last - 7kyu

**Instructions**

- Given a sequence of integers, return the sum of all the integers that have an even index, multiplied by the integer at the last index.

- Indices in sequence start from 0.

- If the sequence is empty, you should return 0.

---

#### Test cases

```python
print(even_last([]))
print(even_last([2, 3, 4, 5]))
print(even_last([45, 46, 84, 59, 85, 25]))
print(even_last([59, -15, 70, 85, 42, 54]))
print(even_last([41, -36, 71, -44, 67, 83]))
```

#### Output 
```
0
30
5350
9234
14857
```

---

#### Solution

```python
def even_last(arr):
    return sum(arr[::2]) * arr[-1] if arr else 0
```

---

[Codewars link](https://www.codewars.com/kata/5a1a9e5032b8b98477000004)
