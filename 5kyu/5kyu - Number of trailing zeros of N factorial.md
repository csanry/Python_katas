## Number of trailing zeros of N! - 5kyu

**Instructions**

- Write a program that will calculate the number of trailing zeros in a factorial of a given number.

---

#### Test cases

```python
print(zeros(0))
print(zeros(6))
print(zeros(30))
print(zeros(100))
```

#### Output 

```
0
1
7
24
```

---

#### Solution

```python
def zeros(n):
    x = n // 5
    return x + zeros(x) if x else 0
```

---

[Codewars link](https://www.codewars.com/kata/52f787eb172a8b4ae1000a34)
