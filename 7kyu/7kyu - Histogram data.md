## Histogram data - 7kyu

**Instructions**

- You will be given an array of non-negative integers and positive integer bin width.

- Your task is to create the Histogram method that will return histogram data corresponding to the input array. The histogram data is an array that stores under index i the count of numbers that belong to bin i. The first bin always starts with zero.

- On an empty input you should return empty output.

---

#### Test cases

```python
print(histogram([1, 1, 0, 1, 3, 2, 6], 1))
print(histogram([1, 1, 0, 1, 3, 2, 6], 2))
print(histogram([], 1))
print(histogram([8], 1))
```

#### Output
```
[1, 3, 1, 1, 0, 0, 1]
[4, 2, 0, 1]
[]
[0, 0, 0, 0, 0, 0, 0, 0, 1]
```

---

#### Solution

```python
def histogram(values, bin_width):
    if not values:
        return []
    arr = [0] * (max(values) // bin_width + 1)
    for v in values:
        arr[v // bin_width] += 1
    return arr
```

---

[Codewars link](https://www.codewars.com/kata/5704bf9b38428f1446000a9d)
