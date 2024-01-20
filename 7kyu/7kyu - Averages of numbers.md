## Averages of numbers - 7kyu

**Instructions**

- Given an array of integers, return an array of the averages of each integer and the following number, if there is one.

- If the array has 0 or 1 values or is null, your method should return an empty array.

---

#### Test cases

```python
print(averages([2, 2, 2, 2, 2]))
print(averages([2, -2, 2, -2, 2]))
print(averages([1, 3, 5, 1, -10]))
print(averages([]))
```

#### Output

```
[2.0, 2.0, 2.0, 2.0]
[0.0, 0.0, 0.0, 0.0]
[2.0, 4.0, 3.0, -4.5]
[]
```

---

#### Solution

```python
def averages(arr):
    return [(a + b) / 2 for a, b in zip(arr, arr[1:])] if isinstance(arr, list) else []
```

---

[Codewars link](https://www.codewars.com/kata/57d2807295497e652b000139)
