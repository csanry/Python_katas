## Orthogonal Vectors - 7kyu

**Instructions**

- Vectors are classified as orthogonal if their dot product equals zero.

- Complete the function that accepts two sequences as inputs and returns true if the vectors are orthogonal, and false if they are not.

- The sequences will always be correctly formatted and of the same length, so there is no need to check them first.

---

#### Test cases

```python
print(is_orthogonal([1,2], [2,1]))
print(is_orthogonal([1,-2], [2,1]))
print(is_orthogonal([7,8], [7,-6]))
print(is_orthogonal([-13,-26], [-8,4]))
print(is_orthogonal([1,2,3], [0,-3,2]))
print(is_orthogonal([3,4,5], [6,7,-8]))
print(is_orthogonal([3,-4,-5], [-4,-3,0]))
print(is_orthogonal([1,-2,3,-4], [-4,3,2,-1]))
print(is_orthogonal([2,4,5,6,7], [-14,-12,0,8,4]))
print(is_orthogonal([5,10,1,20,2], [-2,-20,-1,10,5]))
```

#### Output
```
False
True
False
True
True
False
True
True
True
False
```

---

#### Solution

```python
def is_orthogonal(u, v):
    # import numpy as np
    # return np.dot(u, v) == 0
    return sum(i * j for i, j in zip(u, v)) == 0
```

---

[Codewars link](https://www.codewars.com/kata/53670c5867e9f2222f000225)
