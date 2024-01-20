## Convert string to camel case - 6kyu

**Instructions**

- Complete the function so that it converts dash/underscore delimited words into camel casing.

- The first word within the output should be capitalized only if the original word was capitalized.

---

#### Test cases

```python
print(to_camel_case(''))
print(to_camel_case("the_stealth_warrior"))
print(to_camel_case("The-Stealth-Warrior"))
print(to_camel_case("A-B-C"))
```

#### Output
```
""
theStealthWarrior
TheStealthWarrior
ABC
```

---

#### Solution

```python
import re
def to_camel_case(text):
    sp = re.split(r'[-_]', text)
    return ''.join(st if not sp.index(st) else st.capitalize() for st in sp)
```

---

[Codewars link](https://www.codewars.com/kata/517abf86da9663f1d2000003)
