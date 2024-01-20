## Largest 5 digit number in a series - 7kyu

**Instructions**

- Given a string of only digits, complete the solution so that it returns the greatest sequence of 5 consecutive digits.

- Return a 5 digit integer.

- The string will always be at least length 5.

---

#### Test cases

```python
print(solution('357926291'))
print(solution('32792333'))
print(solution('56587532'))
print(solution('21473901'))
print(solution('1000234257236912917649653294733992734'))
```

#### Output
```
92629
92333
87532
73901
99273
```

---

#### Solution

```python
def solution(digits):
    return int(max(digits[i:i+5] for i in range(len(digits) - 4)))
```

---

[Codewars link](https://www.codewars.com/kata/51675d17e0c1bed195000001)
