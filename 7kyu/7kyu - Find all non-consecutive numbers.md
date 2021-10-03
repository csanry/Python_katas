## Find all non-consecutive numbers - 7kyu

**Instructions**

- A number is non consecutive if it is not exactly one larger than the previous element in the array. 

- The first element gets a pass and is never considered non consecutive.

- E.g., if we have an array [1,2,3,4,6,7,8,15,16] then 6 and 15 are non-consecutive.

- Return the results as an array of objects with two values `i: <the index of the non-consecutive number>` and `n: <the non-consecutive number>`.

- The array elements will all be numbers. The numbers will also all be unique and in ascending order. The numbers could be positive and/or negetive and the gap could be larger than one.

---

#### Test cases

```python
print(all_non_consecutive([1,2,3,4,6,7,8,10]))
```

#### Output 
```
[{'i': 4, 'n': 6}, {'i': 7, 'n': 10}]
```

---

#### Solution

```python
def all_non_consecutive(arr):
    return [{'i': i, 'n': arr[i]} for i in range(1, len(arr)) if arr[i-1]+1 != arr[i]]
```

---

[Codewars link](https://www.codewars.com/kata/58f8b35fda19c0c79400020f)
