## Sort by binary ones - 7kyu

**Instructions**

- In this example you need to implement a function that sort a list of integers based on it's binary representation.

    1. Sort the list based on the amount of 1's in the binary representation of each number.
    
    2. If two numbers have the same amount of 1's, the shorter string goes first. (ex: "11" goes before "101" when sorting 3 and 5 respectively)
    
    3. If the strings have the same length, lower decimal number goes first. (ex: 21 = "10101" and 25 = "11001", then 21 goes first as is lower)

---

#### Test cases

```python
print(sort_by_binary_ones([1, 3]))
print(sort_by_binary_ones([1, 2, 3, 4]))
print(sort_by_binary_ones([1, 2, 3, 4]))
print(sort_by_binary_ones([1, 3]))
print(sort_by_binary_ones([1, 15, 7, 3, 5]))
print(sort_by_binary_ones([80, 21]))
print(sort_by_binary_ones([0, 1024, 33]))
```

#### Output 

```
[3, 1]
[3, 1, 2, 4]
[3, 1, 2, 4]
[3, 1]
[15, 7, 3, 5, 1]
[21, 80]
[33, 1024, 0]
```

---

#### Solution

```python
def sort_by_binary_ones(arr):
    return sorted(arr, key=lambda x: (-bin(x).count('1'), len(str(x)), x))
```

---

[Codewars link](https://www.codewars.com/kata/59eb28fb0a2bffafbb0000d6)
