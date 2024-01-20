## Base reduction - 6kyu

**Instructions**

- Given a positive integer ```0 < n < 1000000000```.

- Return the end result of the base reduction.

- If it cannot be fully reduced (reduced down to a single-digit number), return `-1`.

- Assume that if 150 conversions from base 11 take place in a row, the number cannot be fully reduced.

```
- Base reduction is a process where a number is inputted, repeatedly converted into another base, and then outputted if it cannot be reduced anymore.
- During the base conversions, the number is converted from the lowest base it can be converted from into base 10.
- For example, 123 would be converted from base 4 to base 10, since base 4 is the lowest base that 123 can be in (123 base 3 is impossible; in base 3, there is no digit 3).
- If the lowest possible base the number can be converted into is 10, convert the number from base 11 to base 10.
- For example, 53109 would be converted from base 11 to base 10, since base 10 is the lowest base it can be in.
- In the end, you should get a number that cannot be reduced by this process (a single digit number).
```

---

#### Test cases

```python
print(basereduct(10))
print(basereduct(5312))
```

#### Output
```
2
3
```

---

#### Solution

```python
import sys
sys.setrecursionlimit(150)

def basereduct(x):
    x = baseconvert(x)
    try:
        return x if x < 10 else basereduct(x)
    except RuntimeError:
        return -1

def baseconvert(x):
    nums = [*map(int, str(x))][::-1]
    base = max(nums) + 1
    if base == 10:
        base = 11
    return sum(v * base ** i for i, v in enumerate(nums))
```

---

[Codewars link](https://www.codewars.com/kata/5840e31f770be1636e0000d3)
