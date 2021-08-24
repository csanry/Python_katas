## Array Leaders - 7kyu

**Instructions**

- An element is an array leader if it is greater than the sum of all the elements to its right side.

- Given an array of integers, find all the leaders in the array.

---

#### Test cases

```python
print(array_leaders([1,2,3,4,0]))
print(array_leaders([16,17,4,3,5,2]))
print(array_leaders([-1,-29,-26,-2]))
print(array_leaders([-36,-12,-27]))
print(array_leaders([5,2]))
print(array_leaders([0,-1,-29,3,2]))
```

#### Output 
```
[4]
[17, 5, 2]
[-1]
[-36, -12]
[5, 2]
[0, -1, 3, 2]
```

---

#### Solution

```python
def array_leaders(numbers):
    cnt = 0
    leaders = []
    for i in numbers[::-1]:
        if i > cnt:
            leaders.append(i)
        cnt += i
    return leaders[::-1]
```

---

[Codewars link](https://www.codewars.com/kata/5a651865fd56cb55760000e0)
