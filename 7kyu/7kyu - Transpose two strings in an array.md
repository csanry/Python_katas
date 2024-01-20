## Transpose two strings in an array - 7kyu

**Instructions**

- You will be given an array that contains two strings.

- Create a function that will take those two strings and transpose them, so that the strings go from top to bottom instead of left to right.

```
transpose_two_strings(['Hello','World']) returns

H W
e o
l r
l l
o d
```

- There should be one space in between the two characters.

- You don't have to modify the case.

- If one string is longer than the other, there should be a space where the character would be.

---

#### Test cases

```python
print(transpose_two_strings(["Hello","World"]))
print(transpose_two_strings(["joey","louise"]))
print(transpose_two_strings(["a","cat"]))
print(transpose_two_strings(["cat",""]))
print(transpose_two_strings(["!a!a!","?b?b"]))
```

#### Output

```
"H W\ne o\nl r\nl l\no d"
"j l\no o\ne u\ny i\n  s\n  e"
"a c\n  a\n  t"
"c  \na  \nt  "
"! ?\na b\n! ?\na b\n!  "
```

---

#### Solution

```python
from itertools import zip_longest
def transpose_two_strings(arr):
    return '\n'.join(f'{a} {b}' for a, b in zip_longest(*arr, fillvalue=' '))
```

---

[Codewars link](https://www.codewars.com/kata/581f4ac139dc423f04000b99)
