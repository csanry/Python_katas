## Recursion 101 - 7kyu

**Instructions**

- Given two positive integers a and b, apply the following operations:

```
i) If a=0 or b=0, return [a,b]. Otherwise, go to step (ii);
ii) If a>=2*b, set a = a-2*b, and repeat step (i). Otherwise, go to step (iii);
iii) If b>=2*a, set b = b-2*a, and repeat step (i). Otherwise, return [a,b].
```

---

#### Test cases

```python
print(solve(6, 19))
print(solve(2, 1))
print(solve(22, 5))
print(solve(2, 10))
```

#### Output
```
[6, 7]
[0, 1]
[0, 1]
[2, 2]
```

---

#### Solution

```python
def solve(a, b):
    if not a or not b:
        return [a, b]
    elif a >= 2 * b:
        return solve(a % (2*b), b)
    elif b >= 2 * a:
        return solve(a, b % (2*a))
    else:
        return [a, b]
```

---

[Codewars link](https://www.codewars.com/kata/5b752a42b11814b09c00005d)
