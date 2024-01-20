## No zeroes for heroes - 8kyu

**Instructions**

- Numbers ending with zeros are boring.

- They might be fun in your world, but not here.

- Get rid of them. Only the ending ones.

```
1450 -> 145
960000 -> 96
1050 -> 105
-1050 -> -105
```

- Zero alone is fine, don't worry about it.

---

#### Test cases

```python
print(no_boring_zeros(1450))
print(no_boring_zeros(960000))
print(no_boring_zeros(1050))
print(no_boring_zeros(-1050))
print(no_boring_zeros(0))
print(no_boring_zeros(2016))
```

#### Output

```
145
96
105
-105
0
2016
```

---

#### Solution

```python
def no_boring_zeros(n):
    return int(str(n).rstrip('0')) if n else n
```

---

[Codewars link](https://www.codewars.com/kata/570a6a46455d08ff8d001002)
