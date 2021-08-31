## Sorted? yes? no? how? - 7kyu

**Instructions**

- Complete the method which accepts an array of integers, and returns:

    - "yes, ascending" - if the numbers in the array are sorted in an ascending order.
    
    - "yes, descending" - if the numbers in the array are sorted in a descending order.
    
    - "no" - otherwise.
    
---

#### Test cases

```python
print(is_sorted_and_how([1, 2]))
print(is_sorted_and_how([15, 7, 3, -8]))
print(is_sorted_and_how([4, 2, 30]))
```

#### Output 
```
yes, ascending
yes, descending
no
```

---

#### Solution

```python
def is_sorted_and_how(arr):
    if arr == sorted(arr):
        return 'yes, ascending'
    elif arr == sorted(arr, reverse = True):
        return 'yes, descending'
    else:
        return 'no'
```

---

[Codewars link](https://www.codewars.com/kata/580a4734d6df748060000045)
