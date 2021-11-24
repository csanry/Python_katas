## Elevator distance - 7kyu

**Instructions**

- Imagine you start on the 5th floor of a building, then travel down to the 2nd floor, then back up to the 8th floor. You have travelled a total of 3 + 6 = 9 floors of distance.

- Given an array representing a series of floors you must reach by elevator, return an integer representing the total distance travelled for visiting each floor in the array in order.

- Array will always contain at least 2 floors. Random tests will contain 2-20 elements in array, and floor values between 0 and 30.

---

#### Test cases

```python
print(elevator_distance([5,2,8]))
print(elevator_distance([1,2,3]))
print(elevator_distance([7,1,7,1]))
```

#### Output 

```
9
2
18
```

---

#### Solution

```python
def elevator_distance(arr): 
    return sum(abs(i-j) for i, j in zip(arr, arr[1:]))
```

---

[Codewars link](https://www.codewars.com/kata/59f061773e532d0c87000d16)
