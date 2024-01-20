## Simple string characters - 7kyu

**Instructions**

- Given a string, return a list of ints detailing the count of uppercase letters, lowercase, numbers and special characters, as follows.

```python
solve("*'&ABCDabcde12345") = [4,5,5,3].
# the order is: uppercase letters, lowercase, numbers and special characters.
```

---

#### Test cases

```python
print(solve("Codewars@codewars123.com"))
print(solve("bgA5<1d-tOwUZTS8yQ"))
print(solve("P*K4%>mQUDaG$h=cx2?.Czt7!Zn16p@5H"))
print(solve("RYT'>s&gO-.CM9AKeH?,5317tWGpS<*x2ukXZD"))
print(solve("$Cnl)Sr<7bBW-&qLHI!mY41ODe"))
print(solve("@mw>0=QD-iAx!rp9TaG?o&M%l$34L.nbft"))
```

#### Output
```
[1, 18, 3, 2]
[7, 6, 3, 2]
[9, 9, 6, 9]
[15, 8, 6, 9]
[10, 7, 3, 6]
[7, 13, 4, 10]
```

---

#### Solution

```python
def solve(s):
    res = [0, 0, 0, 0]
    for c in s:
        i = 0 if c.isupper() else 1 if c.islower() else 2 if c.isdigit() else 3
        res[i] += 1
    return res
```

---

[Codewars link](https://www.codewars.com/kata/5a29a0898f27f2d9c9000058)
