## Simple validation of a username with regex - 8kyu

**Instructions**

- Write a simple regex to validate a username.

- Allowed characters are lowercase letters, numbers, underscore.

- Length should be between 4 and 16 characters inclusive.

---

#### Test cases

```python
print(validate_usr('asddsa'))
print(validate_usr('a'))
print(validate_usr('Hass'))
print(validate_usr('Hasd_12assssssasasasasasaasasasasas'))
print(validate_usr(''))
print(validate_usr('____'))
print(validate_usr('012'))
```

#### Output

```
True
False
False
False
False
True
False
```

---

#### Solution

```python
import re
def validate_usr(username):
    return bool(re.match(r'^[a-z0-9_]{4,16}$', username))
```

---

[Codewars link](https://www.codewars.com/kata/56a3f08aa9a6cc9b75000023)
