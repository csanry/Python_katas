## Simple string reversal - 7kyu

**Instructions**

- Reverse a string while maintaining the spaces (if any) in their original place.

**Example**

```
solve("our code") = "edo cruo"
# Normal reversal without spaces is "edocruo".
# However, there is a space at index 3, so the string becomes "edo cruo"

solve("your code rocks") = "skco redo cruoy".
solve("codewars") = "srawedoc"
```

- All input will be lower case letters and in some cases spaces.

---

#### Test cases

```python
print(solve("codewars"))
print(solve("your code"))
print(solve("your code rocks"))
print(solve("i love codewars"))
```

#### Output
```
srawedoc
edoc ruoy
skco redo cruoy
s rawe docevoli
```

---

#### Solution

```python
def solve(s):
    it = reversed(s.replace(' ', ''))
    return ''.join(c if c == ' ' else next(it) for c in s)
```

---

[Codewars link](https://www.codewars.com/kata/5a71939d373c2e634200008e)
