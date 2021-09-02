## Row weights - 7kyu

**Instructions**

- Several people are standing in a row divided into two teams.

- The first person goes into team 1, the second goes into team 2, the third goes into team 1, and so on.

- Given an array of positive integers (the weights of the people), return a new array of two integers. 

- Where the first one is the total weight of team 1, and the second one is the total weight of team 2.




---

#### Test cases

```python
print(row_weights([80]))
print(row_weights([100, 50]))
print(row_weights([50, 60, 70, 80]))
print(row_weights([13, 27, 49]))
print(row_weights([70, 58, 75, 34, 91]))
print(row_weights([29, 83, 67, 53, 19, 28, 96]))
print(row_weights([0]))
print(row_weights([100, 51, 50, 100]))
print(row_weights([39, 84, 74, 18, 59, 72, 35, 61]))
print(row_weights([0, 1, 0]))
```

#### Output 
```
(80, 0)
(100, 50)
(120, 140)
(62, 27)
(236, 92)
(211, 164)
(0, 0)
(150, 151)
(207, 235)
(0, 1)
```

---

#### Solution

```python
def row_weights(arr):
    return (sum(arr[::2]), sum(arr[1::2]))
```

---

[Codewars link](https://www.codewars.com/kata/5abd66a5ccfd1130b30000a9)
