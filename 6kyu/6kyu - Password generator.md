## Password Generator - 6kyu

**Instructions**

- You need to write a password generator that meets the following criteria:

    - 6 - 20 characters long

    - Contains at least one lowercase letter

    - Contains at least one uppercase letter

    - Contains at least one number

    - Contains only alphanumeric characters (no special characters)

- Return the random password as a string.

---

#### Solution

```python
from random import choice, shuffle, randint
from string import ascii_lowercase as LOWER, ascii_uppercase as UPPER, digits as DIGITS

def password_gen():
    pw = [choice(LOWER), choice(UPPER), choice(DIGITS)] + [choice(LOWER + UPPER + DIGITS) for _ in range(randint(3, 17))]
    shuffle(pw)
    return ''.join(pw)
```

---

[Codewars link](https://www.codewars.com/kata/58ade2233c9736b01d0000b3)
