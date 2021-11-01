## Two to One - 7kyu

**Instructions**

- Take 2 strings s1 and s2 including only letters from a to z. 

- Return a new sorted string, the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.

---

#### Test cases

```python
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
print(longest(a, b))

c = "abcdefghijklmnopqrstuvwxyz"
print(longest(c, c))
```

#### Output 
```
"abcdefklmopqwxy"
"abcdefghijklmnopqrstuvwxyz"
```

---

#### Solution

```python
def longest(s1, s2):
    return ''.join(sorted(set(s1 + s2)))
```

---

[Codewars link](https://www.codewars.com/kata/5656b6906de340bd1b0000ac)
