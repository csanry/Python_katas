## Even numbers in an array - 7kyu

**Instructions**

- Given an array of numbers, return a new array of length `n` containing the last even numbers from the original array (in the same order).

- The original array will be not empty and will contain at least `n` even numbers.

---

#### Test cases

```python
print(even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
print(even_numbers([-22, 5, 3, 11, 26, -6, -7, -8, -9, -8, 26], 2))
print(even_numbers([6, -25, 3, 7, 5, 5, 7, -3, 23], 1))
```

#### Output

```
[4, 6, 8]
[-8, 26]
[6]
```

---

#### Solution

```python
def even_numbers(arr, n):
    res = []
    for num in arr[::-1]:
        if not num & 1:
            res.append(num)
            if len(res) == n:
                return res[::-1]
```

---

[Codewars link](https://www.codewars.com/kata/5a431c0de1ce0ec33a00000c)
