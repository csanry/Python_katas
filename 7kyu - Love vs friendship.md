## Love vs friendship - 7kyu

**Instructions**

- If　a = 1, b = 2, c = 3 ... z = 26

- Then l + o + v + e = 54

- and f + r + i + e + n + d + s + h + i + p = 108

- Write a function that accepts a lowercase string as input and converts them into marks.

---

#### Test cases

```python
print(words_to_marks('attitude'))
print(words_to_marks('friends'))
print(words_to_marks('family'))
print(words_to_marks('selfness'))
print(words_to_marks('knowledge'))
```

#### Output 
```
100
75
66
99
96
```

---

#### Solution

```python
def words_to_marks(s):
    return sum(ord(c) - 96 for c in s)
```

---

[Codewars link](https://www.codewars.com/kata/59706036f6e5d1e22d000016)
