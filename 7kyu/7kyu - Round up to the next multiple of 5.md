## Round up to the next multiple of 5 - 7kyu

**Instructions**

- Given an integer as input, can you round it to the next (meaning, "higher") multiple of 5?

Examples:
```
input:    output:
0    ->   0
2    ->   5
3    ->   5
12   ->   15
21   ->   25
30   ->   30
-2   ->   0
-5   ->   -5
etc.
```

- Input may be any positive or negative integer (including 0).

---

#### Test cases

```python
print(round_to_next5(0))
print(round_to_next5(3))
print(round_to_next5(12))
print(round_to_next5(21))
print(round_to_next5(-2))
print(round_to_next5(-5))
```

#### Output 
```
0
5
15
25
0
-5
```

---

#### Solution

```python
def round_to_next5(n):
    return n + ((5 - n) % 5)
```

---

[Codewars link](https://www.codewars.com/kata/55d1d6d5955ec6365400006d)
