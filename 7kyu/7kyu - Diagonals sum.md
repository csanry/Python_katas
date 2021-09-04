## Diagonals sum - 7kyu

**Instructions**

- Create a function that receives a (square) matrix and calculates the sum of both diagonals (main and secondary).

---

#### Test cases

```python
print(sum_diagonals( [
  [ 1, 2, 3 ],
  [ 4, 5, 6 ],
  [ 7, 8, 9 ]
] ))
```

#### Output 
```
30 # 1 + 5 + 9 + 3 + 5 + 7
```

---

#### Solution

```python
import numpy as np 

def sum_diagonals(matrix):
    return sum(np.diag(matrix) + np.diag(matrix[::-1]))

# Non-numpy solution using indexing
# def sum_diagonals(matrix):
#     try: 
#         return sum(matrix[i][i] + matrix[::-1][i][i] for i in range(len(matrix))) 
#     except:
#         return 0
```

---

[Codewars link](https://www.codewars.com/kata/5592fc599a7f40adac0000a8)
