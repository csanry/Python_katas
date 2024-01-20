## Crossing Sum - 7kyu

**Instructions**

- Given a rectangular `matrix` and integers `a and b`, consider the union of the ath row and the bth (both 0-based) column of the `matrix`.

- Return sum of all elements of that union.

---

#### Test cases

```python
print(crossing_sum([[1,1,1,1],[2,2,2,2],[3,3,3,3]],1,3))
print(crossing_sum([[1,1],[3,3],[1,1],[2,2]],3,0))
print(crossing_sum([[100]],0,0))
print(crossing_sum([[1,2,3,4,5]],0,0))
print(crossing_sum([[1],[2],[3],[4],[5]],0,0))
```

#### Output

```
12
9
100
15
15
```

---

#### Solution

```python
def crossing_sum(matrix, row, col):
    row_sum = sum(matrix[row])
    col_sum = sum(line[col] for line in matrix)
    return row_sum + col_sum - matrix[row][col]

def crossing_sum(matrix, row, col):
    '''(A u B) = A + B - (A n B)'''
    return sum(matrix[row]) + sum(line[col] for line in matrix) - matrix[row][col]
```

---

[Codewars link](https://www.codewars.com/kata/5889ab4928c08c08da00009b)
