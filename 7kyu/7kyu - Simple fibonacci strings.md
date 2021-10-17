## Simple fibonacci strings - 7kyu

**Instructions**

- Given a fibonacci sequence as such:
 
```python
f0 = '0'
f1 = '01'
f2 = '010' = f1 + f0
f3 = '01001' = f2 + f1
```

- You will be given a number and your task is to return the `nth` fibonacci string.

- `n` will always be >= 0.

---

#### Test cases

```python
print(solve(0))
print(solve(1))
print(solve(2))
print(solve(3))
print(solve(5))
```

#### Output 

```
0
01
010
01001
0100101001001
```

---

#### Solution

```python
def solve(n):
    a, b = '01'
    for _ in range(n): 
        a, b = a + b, a
    return a 
```

---

[Codewars link](https://www.codewars.com/kata/5aa39ba75084d7cf45000008)
