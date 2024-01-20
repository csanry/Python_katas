## Maximum subarray sum - 5kyu

**Instructions**

- The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers.

```
max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6: [4, -1, 2, 1]
```

- Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array.

- If the list is made up of only negative numbers, return 0 instead.

- Empty list is considered to have zero greatest sum.

- Note that the empty list or array is also a valid subarray.


---

#### Test cases

```python
print(max_sequence([]))
print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(max_sequence([-2, -1, -3, -4, -1, -2, -1, -5, -4]))
print(max_sequence([7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43]))
```

#### Output

```
0
6
0
155
```

---

#### Solution

```python
def max_sequence(arr):
    glo_max, loc_max = 0, 0
    for i in arr:
        loc_max += i
        if loc_max < 0:
            loc_max = 0
        if loc_max > glo_max:
            glo_max = loc_max
    return glo_max
```

---

[Codewars link](https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c)
