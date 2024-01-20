## Double Trouble - 7kyu

**Instructions**

- Given an array of integers `x`, and a target `t`, you must find out if any two consecutive numbers in the array sum to `t`.

- If so, remove the second number.

```
Example
x = [1, 2, 3, 4, 5]
t = 3

1+2 = t, so remove 2.
No other pairs = t, so rest of array remains:

[1, 3, 4, 5]
```

- Work through the array from left to right and return the resulting array.

---

#### Test cases

```python
print(trouble([1, 3, 5, 6, 7, 4, 3],7))
print(trouble([4, 1, 1, 1, 4],2))
print(trouble([2, 6, 2],8))
print(trouble([2, 2, 2, 2, 2, 2], 4))
```

#### Output

```
[1, 3, 5, 6, 7, 4]
[4, 1, 4]
[2, 2]
[2]
```

---

#### Solution

```python
def trouble(x, t):
    res = [x[0]]
    for e in x[1:]:
        if e + res[-1] != t:
            res.append(e)
    return res
```

---

[Codewars link](https://www.codewars.com/kata/57f7796697d62fc93d0001b8/)
