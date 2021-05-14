## Remove the parentheses - 6kyu

**Instructions**

- Given a string, remove everything inside the parentheses as well as the parentheses themselves.

---

#### Test cases

```python
print(remove_parentheses("example(unwanted thing)example"))
print(remove_parentheses("example (unwanted thing) example"))
print(remove_parentheses("a (bc d)e"))
print(remove_parentheses("a(b(c))"))
print(remove_parentheses("hello example (words(more words) here) something"))
print(remove_parentheses("(first group) (second group) (third group)"))
```

#### Output 
```
exampleexample
example  example
a e
a
hello example  something
"   "
```

---

#### Solution

```python
def remove_parentheses(s):
    lvl, out = 0, []
    for char in s:
        lvl += (char == '(')
        if not lvl:
            out.append(char)
        lvl -= (char == ')')
    return ''.join(out)
```

---

[Codewars link](https://www.codewars.com/kata/5f7c38eb54307c002a2b8cc8)
