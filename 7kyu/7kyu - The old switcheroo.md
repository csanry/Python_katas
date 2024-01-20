## The old switcheroo - 7kyu

**Instructions**

- Write a function that takes in a string and replaces all the vowels `a, e, i, o, u` with their respective positions (1-indexed) within that string.

- Your function should be case-insensitive to the vowels.

---

#### Test cases

```python
print(vowel_2_index('this is my string'))
print(vowel_2_index('Codewars is the best site in the world'))
print(vowel_2_index('Tomorrow is going to be raining'))
```

#### Output

```
th3s 6s my str15ng
C2d4w6rs 10s th15 b18st s23t25 27n th32 w35rld
T2m4rr7w 10s g1415ng t20 b23 r2627n29ng
```

---

#### Solution

```python
def vowel_2_index(st):
    return ''.join(str(i) if c.lower() in 'aeiou' else c for i, c in enumerate(st, 1))
```

---

[Codewars link](https://www.codewars.com/kata/55d410c492e6ed767000004f)
