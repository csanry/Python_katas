## How many consecutive numbers are needed? - 7kyu

**Instructions**

- Create the function `consecutive(arr)` that takes an array of integers and return the minimum number of integers needed to make the contents of arr consecutive from the lowest number to the highest number.

- If arr contains `[4, 8, 6]` then the output should be 2 because two numbers need to be added to the array (5 and 7) to make it a consecutive array of numbers from 4 to 8. 

- Numbers in arr will be unique.

---

#### Test cases

```python
print(consecutive([4,8,6]))
print(consecutive([1,2,3,4]))
print(consecutive([]))
print(consecutive([1]))
print(consecutive([-10, -9]))
```

#### Output 
```
2
0
0
0
0
```

---

#### Solution

```python
def consecutive(arr):
    return (max(arr) - min(arr) + 1) - len(arr) if arr else 0
```

---

[Codewars link](https://www.codewars.com/kata/559cc2d2b802a5c94700000c)
