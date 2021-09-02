## What dominates your array? - 7kyu

**Instructions**

- A zero-indexed array arr consisting of n integers is given. 

- The dominator of array arr is the value that occurs in more than half of the elements of arr.

- For example, consider array arr such that `arr = [3,4,3,2,3,1,3,3]`

- The dominator of arr is 3 because it occurs in 5 out of 8 elements of arr and 5 is more than a half of 8.

- Write a function such that, given a zero-indexed array arr consisting of n integers, returns the dominator of arr. The function should return −1 if array does not have a dominator. 

- All values in arr will be >=0.

---

#### Test cases

```python
print(dominator([3,4,3,2,3,1,3,3]))
print(dominator([1,2,3,4,5]))
print(dominator([1,1,1,2,2,2]))
print(dominator([1,1,1,2,2,2,2]))
print(dominator([]))
```

#### Output 
```
3
-1
-1
2
-1
```

---

#### Solution

```python
def dominator(arr):
    return next((i for i in set(arr) if arr.count(i) > len(arr) / 2), -1)
```

---

[Codewars link](https://www.codewars.com/kata/559e10e2e162b69f750000b4)
