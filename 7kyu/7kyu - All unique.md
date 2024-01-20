## All Unique - 7kyu

**Instructions**

- Write a program to determine if a string contains only unique characters.

- Return `True` if it does and `False` otherwise.

- The string may contain any of the 128 ASCII characters.

- Characters are case-sensitive, e.g. `a` and `A` are considered different characters.

---

#### Test cases

```python
print(has_unique_chars("abcdef"))
print(has_unique_chars("++-"))
print(has_unique_chars("  nAa"))
```

#### Output

```
True
False
False
```

---

#### Solution

```python
def has_unique_chars(string):
    return len(set(string)) == len(string)
```

---

[Codewars link](https://www.codewars.com/kata/553e8b195b853c6db4000048)
