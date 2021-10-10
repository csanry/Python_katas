## Maximum Length Difference - 7kyu

**Instructions**

- You are given two arrays `a1` and `a2` of strings. 

- Each string is composed with letters from a to z. 

- Let x be any string in the first array and y be any string in the second array.

- Find `max(abs(length(x) − length(y)))`.

- If `a1` or `a2` are empty return `-1`. 

---

#### Test cases

```python
s1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
s2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
print(mxdiflg(s1, s2))
```

#### Output 

```
13
```

---

#### Solution

```python
def mxdiflg(a1, a2):
    return max(     
        len(max(a1, key=len)) - len(min(a2, key=len)),
        len(max(a2, key=len)) - len(min(a1, key=len))) if a1 and a2 else -1
```

---

[Codewars link](https://www.codewars.com/kata/5663f5305102699bad000056)
