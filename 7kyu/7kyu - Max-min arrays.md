## Max-min arrays - 7kyu

**Instructions**

- Given an array of unique elements, rearrange the values so that the first max value is followed by the first minimum, followed by second max value then second min value, etc.

```
-- example
solve([15,11,10,7,12]) => [15,7,12,10,11]
```

---

#### Test cases

```python
print(solve([15,11,10,7,12]))
print(solve([91,75,86,14,82]))
print(solve([84,79,76,61,78]))
print(solve([52,77,72,44,74,76,40]))
print(solve([1,6,9,4,3,7,8,2]))
print(solve([78,79,52,87,16,74,31,63,80]))
```

#### Output 

```
[15, 7, 12, 10, 11]
[91, 14, 86, 75, 82]
[84, 61, 79, 76, 78]
[77, 40, 76, 44, 74, 52, 72]
[9, 1, 8, 2, 7, 3, 6, 4]
[87, 16, 80, 31, 79, 52, 78, 63, 74]
```

---

#### Solution

```python
from collections import deque
def solve(arr):
    dq, res = deque(sorted(arr)), []
    while dq: 
        res.append(dq.pop())
        if dq:
            res.append(dq.popleft())
    return res
```

---

[Codewars link](https://www.codewars.com/kata/5a090c4e697598d0b9000004)
