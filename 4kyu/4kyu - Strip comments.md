## Strip comments - 4kyu

**Instructions**

- Complete the solution so that it strips all text that follows any of a set of comment markers passed in. 

- Any whitespace at the end of the line should also be stripped out.

---

#### Test cases

```python
print(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))
print(solution("a #b\nc\nd $e f g", ["#", "$"]))
```

#### Output 
```
"apples, pears\ngrapes\nbananas"
"a\nc\nd"
```

---

#### Solution

```python
def solution(string, markers):
    lines = string.split('\n')
    for m in markers: 
        lines = [s.split(m)[0].rstrip() for s in lines]
    return '\n'.join(lines)
```

---

[Codewars link](https://www.codewars.com/kata/51c8e37cee245da6b40000bd)
