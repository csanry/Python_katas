## Merge two sorted arrays into one - 8kyu

**Instructions**

- You are given two sorted arrays that both only contain integers.

- Your task is to find a way to merge them into a single one, sorted in asc order.

- `arr1` and `arr2` may have same integers. Remove duplicated in the returned result.

---

#### Test cases

```python
arr1 = [1, 2, 3, 4, 5]
arr2 = [6, 7, 8, 9, 10]
print(merge_arrays(arr1, arr2))

arr3 = [1, 3, 5, 7, 9]
arr4 = [10, 8, 6, 4, 2]
print(merge_arrays(arr3, arr4))

arr5 = [1, 3, 5, 7, 9, 11, 12]
arr6 = [1, 2, 3, 4, 5, 10, 12]
print(merge_arrays(arr5, arr6))
```

#### Output

```
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[1, 2, 3, 4, 5, 7, 9, 10, 11, 12]
```

---

#### Solution

```python
def merge_arrays(arr1, arr2):
    return sorted(set(arr1 + arr2))
```

---

[Codewars link](https://www.codewars.com/kata/5899642f6e1b25935d000161)
