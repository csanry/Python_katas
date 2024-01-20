## Change two-dimensional array - 7kyu

**Instructions**

Given a two-dimensional square array of random integers, change all negative integers on the main diagonal to 0, and non-negatives to 1.

---

#### Test cases

```python
print(matrix([[-1, 4, -5, -9, 3],
              [6, -4, -7, 4, -5],
              [3, 5, 4, -9, -1],
              [1, 5, -7, -8, -9],
              [-3, 2, 1, -5, 6]]))
```

#### Output
```
[[0, 4, -5, -9, 3],
 [6, 0, -7, 4, -5],
 [3, 5, 1, -9, -1],
 [1, 5, -7, 0, -9],
 [-3, 2, 1, -5, 1]]
```

---

#### Solution

```python
def matrix(m):
    return [[v if i != j else int(v >= 0) for j, v in enumerate(r)]
            for i, r in enumerate(m)]
```

---

[Codewars link](https://www.codewars.com/kata/581214d54624a8232100005f)
