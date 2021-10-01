## By 3, or not by 3? That is the question - 7kyu

**Instructions**

- Given a series of digits as a string, determine if the number represented by the string is divisible by three.

- You can expect all test case arguments to be strings representing values greater than 0.

- Try to avoid using the % (modulo) operator.

---

#### Test cases

```python
print(divisible_by_three('123'))
print(divisible_by_three('19254'))
print(divisible_by_three('88'))
print(divisible_by_three('1'))
```

#### Output 
```
True
True
False
False
```

---

#### Solution

```python
def divisible_by_three(st):
    while len(st) != 1: 
        st = str(sum(int(n) for n in st))
    return int(st) in [3, 6, 9]
```

---

[Codewars link](https://www.codewars.com/kata/59f7fc109f0e86d705000043)
