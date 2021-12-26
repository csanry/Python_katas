## Required Data II - 6kyu

**Instructions**

- Given an `arr`, a `k` integer and the mode string `min` or `max`.

- If `str_` is `max`, the function will build internally an array of received values in descending order and will output the k-th term in the list.

- If `str_` is `min`, the function will build internally an array of received values in ascending order and will output the k-th term in the list.

- If the value of `k` is higher than the number of values, the asked function will return the string `No way`.

- If the array has elements that are not integers, the function will output `Invalid entry list`.

- If our array is an empty list, the function should output `No values in the array`.

- If there is a typing mistake in the third entry, the function will return `Valid entries: 'max' or 'min'`.

- If the second entry is not a positive integer (k < 0), the function should output `Incorrect value for k`. 

- The code should detect if `k` is a string, too, with the same result.

- If we have more than one error, the code should not output all the mistakes or invalid entries. It will output only one, checking in the following order:

    - The value of `k`.

    - The mode strings: `max` or `min`.

    - The array with the values.

---

#### Test cases

```python
print(given_nth_value([3, 3, -1, 10, 6, 8, -5, 4, 22, 31, 34, - 16, -16, 8, 8], 5, 'min'))
print(given_nth_value([3, 3, -1, 10, 6, 8, -5, 4, 22, 31, 34, - 16, -16, 8, 8], 6, 'max'))
print(given_nth_value([3, 3], -5, 'min'))
print(given_nth_value([3, 3, -1, 10, 6, 8, -5, 4, 22, 31, 34, - 16, -16, 8, 8], 13, 'max'))
print(given_nth_value([3, 3, -1, 10, 6, 8, -5, 'Yes', 4, 22, 31], 4, 'max'))
print(given_nth_value([], 4, 'max'))
print(given_nth_value([3, 3, -1, 10, 6, 8, -5, 4, 22, 31], 2, 'mix'))
print(given_nth_value([3, 3, -1, 10, 6, 8, -5, 4, 22, 31], 2, 'MaX'))
```

#### Output 

```
4
6
Incorrect value for k
No way
Invalid entry list
No values in the array
Valid entries: 'max' or 'min'
22
```

---

#### Solution

```python
def given_nth_value(arr, k, str_):
    if not isinstance(k, int) or k < 0:
        return 'Incorrect value for k'
    if str_.lower() not in ('min', 'max'):
        return "Valid entries: 'max' or 'min'"
    if not arr:
        return 'No values in the array'
    if any(not isinstance(i, int) for i in arr):
        return 'Invalid entry list'
    if k > len(set(arr)):
        return 'No way'
    lst = sorted(set(arr))
    return lst[k - 1] if str_ == 'min' else lst[-k]
```

---

[Codewars link](https://www.codewars.com/kata/560985a07add63e1a1000019)
