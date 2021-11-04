## Delete occurrences of an element if occurs more than n times - 6kyu

**Instructions**

- Given a list `order` and a number `max_e`, create a new list that contains each number of lst at most N times without reordering.

- For example if `max_e = 2`, and the input is `[1, 2, 3, 1, 2, 1, 2, 3]`, you take `[1, 2, 3, 1, 2]`.

- Drop the next `[1, 2]` since this would lead to 1 and 2 being in the result 3 times.

- Finally, take 3, which leads to `[1, 2, 3, 1, 2, 3]`.

---

#### Test cases

```python
delete_nth([1, 1, 1, 1], 2) 
delete_nth([20, 37, 20, 21], 1) 
```

#### Output 
```
[1, 1]
[20, 37, 21]
```

---

#### Solution

```python
from collections import defaultdict
def delete_nth(order, max_e):
    cnt = defaultdict(int)
    result = []
    for element in order:
        if cnt[element] < max_e:
            result.append(element)
            cnt[element] += 1
    return result
```

---


[Codewars link](https://www.codewars.com/kata/554ca54ffa7d91b236000023)
