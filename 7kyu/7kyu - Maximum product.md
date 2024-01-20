## Maximum Product - 7kyu

**Instructions**

- Given an array of integers, find the maximum product obtained from multiplying 2 adjacent numbers in the array.

- Array/list size is at least 2.

- Array/list numbers could be a mixture of positives, negatives or zeroes.

---

#### Test cases

```python
print(adjacent_element_product([4, 12, 3, 1, 5]))
print(adjacent_element_product([5, 1, 2, 3, 1, 4]))
print(adjacent_element_product([-23, 4, -5, 99, -27, 329, -2, 7, -921]))
print(adjacent_element_product([5, 1, 2, 3, 1, 4]))
print(adjacent_element_product([1, 2, 3, 0]))
```

#### Output
```
48
6
-14
6
6
```

---

#### Solution

```python
def adjacent_element_product(arr):
    return max(i * j for i, j in zip(arr, arr[1:]))
```

---

[Codewars link](https://www.codewars.com/kata/5a4138acf28b82aa43000117)
