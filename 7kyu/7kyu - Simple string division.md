## Simple string division - 7kyu

**Instructions**

- Given a number in form of a string and an integer `k`, your task is to insert `k` commas into the string and determine which of the partitions is the largest.

---

#### Test cases

```python
print(solve('123', 1))
print(solve('1234', 1))
print(solve('1234', 2))
print(solve('1234', 3))
```

#### Output 

```
23
234
34
4
```

---

#### Solution

```python
def solve(st, k):
    length = len(st) - k
    return max(map(int, (st[i:length+i] for i in range(len(st)))))
```

---

[Codewars link](https://www.codewars.com/kata/5b83c1c44a6acac33400009a)
