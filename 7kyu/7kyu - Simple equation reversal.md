## Simple equation reversal - 7kyu

**Instructions**

- Given a mathematical equation that has *,+,-,/, reverse it as follows:

```
solve("100*b/y") = "y/b*100"
solve("a+b-c/d*30") = "30*d/c-b+a"
```

---

#### Test cases

```python
print(solve("100*b/y"))
print(solve("a+b-c/d*30"))
print(solve("a*b/c+50"))
```

#### Output 

```
y/b*100
30*d/c-b+a
50+c/b*a
```

---

#### Solution

```python
import re 
def solve(eq):
    return ''.join(re.split(r'([+-/*])', eq)[::-1])
```

---

[Codewars link](https://www.codewars.com/kata/5aa3af22ba1bb5209f000037)
