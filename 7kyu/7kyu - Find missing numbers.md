## Find missing numbers - 7kyu

**Instructions**

- You will get an array of numbers.

- Every preceding number is smaller than the one following it.

- Some numbers will be missing, for instance:

```
[-3, -2, 1, 5] # missing numbers are: -1, 0, 2, 3, 4
```

- Return an array of those missing numbers.

---

#### Test cases

```python
print(find_missing_numbers([-3,-2,1,4]))
print(find_missing_numbers([-1,0,1,2,3,4]))
print(find_missing_numbers([]))
print(find_missing_numbers([0]))
print(find_missing_numbers([-4,4]))
```

#### Output
```
[-1, 0, 2, 3]
[]
[]
[]
[-3, -2, -1, 0, 1, 2, 3]
```

---

#### Solution

```python
def find_missing_numbers(arr):
    return [i for i in range(arr[0], arr[-1]+1) if i not in arr] if arr else []
```

---

[Codewars link](https://www.codewars.com/kata/56d02e6cc6c8b49c510005bb)
