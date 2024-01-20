## Sum two arrays - 6kyu

**Instructions**

- Your task is to create a function which takes two arrays consisting of integers, and returns the sum of those two arrays.

- The twist is that `[3, 2, 9]` does not equal `3 + 2 + 9`, it would equal `'3' + '2' + '9'` converted to an integer for this kata, meaning it would equal `329`.

- The output should be an array of the sum in a similar fashion to the input (for example, if the sum is `341`, you would return `[3, 4, 1]`).

---

#### Test cases

```python
print(sum_arrays([3, 2, 9], [1, 2]))
print(sum_arrays([4, 7, 3], [1, 2, 3]))
print(sum_arrays([1], [5, 7, 6]))
print(sum_arrays([-3, 4, 2], [3, 4, 4]))
print(sum_arrays([], []))
print(sum_arrays([0], []))
print(sum_arrays([], [1, 2]))
```

#### Output

```
[3, 4, 1]
[5, 9, 6]
[5, 7, 7]
[2]
[]
[0]
[1, 2]
```

---

#### Solution

```python
def sum_arrays(array1, array2):
    if not array1 and not array2:
        return []
    n1 = int(''.join(map(str, array1))) if array1 else 0
    n2 = int(''.join(map(str, array2))) if array2 else 0
    nt = n1 + n2
    res = [int(x) for x in str(abs(nt))]
    if nt < 0:
        res[0] = -res[0]
    return res
```

---

[Codewars link](https://www.codewars.com/kata/59c3e8c9f5d5e40cab000ca6)
