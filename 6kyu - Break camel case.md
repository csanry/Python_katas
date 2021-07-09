## Break Camel Case - 6kyu

**Instructions**

- Complete the solution so that the function will break up camel casing, using a space between words.

---

#### Test cases

```python
print(solution("helloWorld"))
print(solution("camelCase"))
print(solution("breakCamelCase"))
```

#### Output 
```
hello World
camel Case
break Camel Case
```

---

#### Solution

```python
def solution(s): 
    return ''.join(f" {c}" if c.isupper() else c for c in s)
```

---


[Codewars link](https://www.codewars.com/kata/5208f99aee097e6552000148)
