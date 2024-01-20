## Fix String Case - 7kyu

**Instructions**

- Given a string that may have mixed uppercase and lowercase letters.

- Convert that string to either lowercase only or uppercase only based on:

    - Make as few changes as possible.

    - If the string contains equal number of uppercase and lowercase letters, convert the string to lowercase.

---

#### Test cases

```python
print(fix_case('code'))
print(fix_case('CODe'))
print(fix_case('CODewars'))
print(fix_case('CODEwarsTEST'))
print(fix_case('codeWARS'))
```

#### Output

```
code
CODE
codewars
CODEWARSTEST
codewars
```

---

#### Solution

```python
def fix_case(s):
    cnt = sum(-1 if c.islower() else 1 for c in s)
    return s.upper() if cnt > 0 else s.lower()
```

---

[Codewars link](https://www.codewars.com/kata/5b180e9fedaa564a7000009a)
