## Triple X - 7kyu

**Instructions**

- Given a string, return true if the first instance of "x" in the string is immediately followed by the string "xx".

---

#### Test cases

```python
print(triple_x(""))
print(triple_x("there's no XXX here"))
print(triple_x("abraxxxas"))
print(triple_x("xoxotrololololololoxxx"))
print(triple_x("soft kitty, warm kitty, xxxxx"))
print(triple_x("softx kitty, warm kitty, xxxxx"))
```

#### Output

```
False
False
True
False
True
False
```

---

#### Solution

```python
def triple_x(s):
    return s.find('x') == s.find('xxx') >= 0
```

---

[Codewars link](https://www.codewars.com/kata/568dc69683322417eb00002c)
