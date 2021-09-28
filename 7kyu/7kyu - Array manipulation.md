## Array Manipulation - 7kyu

**Instructions**

- Given an array of positive integers, replace every element with the least greatest element to its right. 

- If there is no greater element to its right, replace it with -1. 

- Return the resulting array.

---

#### Test cases

```python
print(array_manip([8, 58, 71, 18, 31, 32, 63, 92, 43, 3, 91, 93, 25, 80, 28]))
print(array_manip([ 2, 4, 18, 16, 7, 3, 9, 13, 18, 10 ]))
```

#### Output 

```
[18, 63, 80, 25, 32, 43, 80, 93, 80, 25, 93, -1, 28, -1, -1]
[3, 7, -1, 18, 9, 9, 10, 18, -1, -1]
```

---

#### Solution

```python
def min_larger_e(val, arr):
    return min(filter(lambda x: x > val, arr), default=-1)

def array_manip(arr):
    return [min_larger_e(val, arr[i:]) for i, val in enumerate(arr, 1)]
```

---

[Codewars link](https://www.codewars.com/kata/58d5e6c114286c8594000027)
