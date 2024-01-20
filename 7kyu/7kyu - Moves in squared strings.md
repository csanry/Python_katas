## Moves in squared strings - 7kyu

**Instructions**

- You are given a string of n lines, each substring being n characters long: For example:

```
s = "abcd\nefgh\nijkl\nmnop"
```

- We will study some transformations of this square of strings.

```
Vertical mirror: vert_mirror
vert_mirror(s) => "dcba\nhgfe\nlkji\nponm"
Horizontal mirror: hor_mirror
hor_mirror(s) => "mnop\nijkl\nefgh\nabcd"
```

- Or printed:

```
vertical mirror  |  horizontal mirror
abcd --> dcba    |  abcd --> mnop
efgh     hgfe    |  efgh     ijkl
ijkl     lkji    |  ijkl     efgh
mnop     ponm    |  mnop     abcd
```

- Write these two functions and a high-order function `oper(fct, s)` which applies either `vert_mirror` or `hor_mirror` on a string.

```
s = "abcd\nefgh\nijkl\nmnop"
oper(vert_mirror, s) => "dcba\nhgfe\nlkji\nponm"
oper(hor_mirror, s) => "mnop\nijkl\nefgh\nabcd"
```

---

#### Test cases

```python
print(oper(vert_mirror, "hSgdHQ\nHnDMao\nClNNxX\niRvxxH\nbqTVvA\nwvSyRu"))
print(oper(vert_mirror, "IzOTWE\nkkbeCM\nWuzZxM\nvDddJw\njiJyHF\nPVHfSx"))
print(oper(hor_mirror, "lVHt\nJVhv\nCSbg\nyeCt"))
print(oper(hor_mirror, "njMK\ndbrZ\nLPKo\ncEYz"))
```

#### Output

```
"QHdgSh\noaMDnH\nXxNNlC\nHxxvRi\nAvVTqb\nuRySvw"
"EWTOzI\nMCebkk\nMxZzuW\nwJddDv\nFHyJij\nxSfHVP"
"yeCt\nCSbg\nJVhv\nlVHt"
"cEYz\nLPKo\ndbrZ\nnjMK"
```

---

#### Solution

```python
def vert_mirror(strng):
    return '\n'.join(line[::-1] for line in strng.splitlines())

def hor_mirror(strng):
    return '\n'.join(strng.splitlines()[::-1])

def oper(fct, s):
    return fct(s)
```

---

[Codewars link](https://www.codewars.com/kata/56dbe0e313c2f63be4000b25)
