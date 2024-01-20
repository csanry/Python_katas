## Cool String - 7kyu

**Instructions**

- Let's call a string cool if it is formed only by Latin letters and no two lowercase and no two uppercase letters are in adjacent positions.

- Given a string, check if it is cool.

---

#### Test cases

```python
print(cool_string("aQwFdA"))
print(cool_string("aBC"))
print(cool_string("AaA"))
print(cool_string("q q"))
print(cool_string("wWw1"))
print(cool_string("2"))
print(cool_string("aAaAaAa"))
print(cool_string("    "))
```

#### Output
```
True
False
True
False
False
False
True
False
```

---

#### Solution

```python
def cool_string(s):
    if s.isalpha():
        if len(s) == 1:
            return True
        elif s[0].islower():
            return s[0:len(s):2].islower() and s[1:len(s):2].isupper()
        else:
            return s[0:len(s):2].isupper() and s[1:len(s):2].islower()
    return False
```

---

[Codewars link](https://www.codewars.com/kata/590fd3220f05b4f1ad00007c)
