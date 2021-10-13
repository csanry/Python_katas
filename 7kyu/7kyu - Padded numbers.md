## Substituting Variables Into Strings: Padded Numbers - 7kyu

**Instructions**

- Complete the solution so that it returns a formatted string. 

- The return value should equal "Value is VALUE" where value is a 5 digit padded number.

---

#### Test cases

```python
print(solution(0))
print(solution(5))
print(solution(109))
print(solution(1204))
```

#### Output 

```
Value is 00000
Value is 00005
Value is 00109
Value is 01204
```

---

#### Solution

```python
def solution(value):
    return f'Value is {value:0>5}'
```

---

[Codewars link](https://www.codewars.com/kata/51c89385ee245d7ddf000001)
