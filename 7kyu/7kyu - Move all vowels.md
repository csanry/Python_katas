## Move all vowels - 7kyu

**Instructions**

- Given a string as input, move all of its vowels to the end of the string, in the same order as they were before.

- Vowels in this kata are a, e, i, o, u.

- All provided input strings are lowercase.

---

#### Test cases

```python
print(move_vowels('day'))
print(move_vowels('apple'))
print(move_vowels('peace'))
print(move_vowels('maker'))
print(move_vowels('programming'))
print(move_vowels('javascript'))
print(move_vowels('python'))
print(move_vowels('ruby'))
print(move_vowels('haskell'))
print(move_vowels('clojure'))
print(move_vowels('csharp'))
```

#### Output 

```
dya
pplae
pceae
mkrae
prgrmmngoai
jvscrptaai
pythno
rbyu
hskllae
cljroue
cshrpa
```

---

#### Solution

```python
def move_vowels(input): 
    return ''.join(sorted(input, key = lambda x: x in 'aeiou'))
```

---

[Codewars link](https://www.codewars.com/kata/56bf3287b5106eb10f000899/)
