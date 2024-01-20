## Scramblies - 5kyu

**Instructions**

- Complete the function `scramble(str1, str2)` that returns `True` if a portion of `str1` characters can be rearranged to match `str2`, otherwise returns `False`.

- Only lower case letters will be used (a-z). No punctuation or digits will be included.

- Performance needs to be considered.

---

#### Test cases

```python
print(scramble('rkqodlw', 'world'))
print(scramble('cedewaraaossoqqyt', 'codewars'))
print(scramble('katas', 'steak'))
print(scramble('scriptjava', 'javascript'))
print(scramble('scriptingjava', 'javascript'))
```

#### Output
```
True
True
False
True
True
```

---

#### Solution

```python
def scramble(s1, s2):
    from collections import Counter
    return not(Counter(s2) - Counter(s1))
```

---


[Codewars link](https://www.codewars.com/kata/55c04b4cc56a697bb0000048)
