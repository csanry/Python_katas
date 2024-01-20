## Father and son - 7kyu

**Instructions**

- Every uppercase letter is Father, The corresponding lowercase letters is the Son.

- Given a string s, If the father and son both exist, keep them.

- If it is a separate existence, delete them. Return the result.

---

#### Test cases

```python
print(sc("Aab"))
print(sc("AabBc"))
print(sc("SONson"))
print(sc("DONKEYmonkey"))
print(sc("monkeyDONKEY"))
print(sc("BANAna"))
```

#### Output
```
Aa
AabB
SONson
ONKEYonkey
onkeyONKEY
ANAna
```

---

#### Solution

```python
def sc(s):
    return ''.join(let for let in s if let.swapcase() in set(s))
```

---

[Codewars link](https://www.codewars.com/kata/56fe9a0c11086cd842000008)
