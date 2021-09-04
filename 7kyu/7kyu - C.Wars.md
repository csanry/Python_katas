## C.wars - 7kyu

**Instructions**

- Initialize the names provided, keeping the last name.

---

#### Test cases

```python
print(initials('code wars'))
print(initials('Barack hussein obama'))
print(initials('Ava Daniel Madison Luiza Alexander Bell'))
print(initials('Julia Ygritte Isabella Rafael Griffin'))
print(initials('Noah Michael Abigail Lucas Eduarda Parker'))
```

#### Output 
```
C.Wars
B.H.Obama
A.D.M.L.A.Bell
J.Y.I.R.Griffin
N.M.A.L.E.Parker
```

---

#### Solution

```python
def initials(name):
    return '.'.join(i[0].upper() if i in name.split()[:-1] else i.capitalize() for i in name.split())
```

---

[Codewars link](https://www.codewars.com/kata/55968ab32cf633c3f8000008)
