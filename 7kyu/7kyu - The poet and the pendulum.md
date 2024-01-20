## The poet and the pendulum - 7kyu

**Instructions**

- Given an array of n integers, arrange them in a way similar to the to-and-fro movement of a pendulum.

- The smallest element of the list of integers, must come in the center position of the array.

- The next number goes to the right, then the left, and so on.

---

#### Test cases

```python
print(pendulum([4,6,8,7,5]))
print(pendulum([19,30,16,19,28,26,28,17,21,17]))
print(pendulum([-9,-2,-10,-6]))
print(pendulum([-19,-9,-5,-6,-15,-16,-5,-12]))
print(pendulum([11,-16,-18,13,-11,-12,3,18]))
```

#### Output
```
[8, 6, 4, 5, 7]
[28, 26, 19, 17, 16, 17, 19, 21, 28, 30]
[-6, -10, -9, -2]
[-5, -9, -15, -19, -16, -12, -6, -5]
[13, 3, -12, -18, -16, -11, 11, 18]
```

---

#### Solution

```python
def pendulum(values):
    values = sorted(values)
    a, b = [], []
    for idx, val in enumerate(values):
        a.append(val) if idx%2 else b.append(val)
    return b[::-1] + a
```

---

[Codewars link](https://www.codewars.com/kata/5bd776533a7e2720c40000e5)
