## Limit string length - 7kyu

**Instructions**

- The function must return the truncated version of the given string up to the given limit followed by "..." if the result was truncated.

- Return the same string if nothing was truncated.

---

#### Test cases

```python
print(solution('Testing String', 3))
print(solution('Testing String', 8))
print(solution('Test', 10))
print(solution('Test', 4))
```

#### Output 

```
Tes...
Testing ...
Test
Test
```

---

#### Solution

```python
def solution(st, limit):
    return f'{st[:limit]}...' if len(st) > limit else st
```

---

[Codewars link](https://www.codewars.com/kata/5208fc3cb613bc725f000142)
