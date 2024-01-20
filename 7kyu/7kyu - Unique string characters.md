## Unique string characters - 7kyu

**Instructions**

- Given two strings a and b, return the characters that are not common in the two strings.

- For example:

```python
solve("xyab","xzca") = "ybzc"
# The first string has 'yb' which is not in the second string.
# The second string has 'zc' which is not in the first string.
```

- Return the characters from the 1st string concatenated with the 2nd string.

---

#### Test cases

```python
print(solve("xyab", "xzca"))
print(solve("xyabb", "xzca"))
print(solve("abcd", "xyz"))
print(solve("xxx", "xzca"))
```

#### Output
```
ybzc
ybbzc
abcdxyz
zca
```

---

#### Solution

```python
def solve(a, b):
    new_a = [let for let in a if let not in b]
    new_b = [let for let in b if let not in a]
    return ''.join(new_a + new_b)
```

---

[Codewars link](https://www.codewars.com/kata/5a262cfb8f27f217f700000b)
