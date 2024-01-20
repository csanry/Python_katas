## Strong password? - 7kyu

**Instructions**

- Your users' passwords were all stolen in the Yahoo! hack, and it turns out they have been lax in creating secure passwords.

- Create a function that checks their new password (passed as a string) to make sure it meets the following requirements:

    - Between 8 - 20 characters

    - Contains only the following characters (and at least one character from each category)

    - uppercase letters, lowercase letters, digits, special characters from !@#$%^&*?

- Return `valid` if passed or `not valid` otherwise.

---

#### Test cases

```python
print(check_password(""))
print(check_password("password"))
print(check_password("P1@p"))
print(check_password("P1@pP1@p"))
print(check_password("P1@pP1@pP1@pP1@pP1@pP1@p"))
print(check_password("Paaaaaa222!!!"))
```

#### Output

```
not valid
not valid
not valid
valid
not valid
valid
```

---

#### Solution

```python
from string import ascii_lowercase, ascii_uppercase
def check_password(s):
    val = '!@#$%^&*?' + ascii_lowercase + ascii_uppercase + '1234567890'
    return 'valid' if ( all(map(lambda x: x in val, s)) and
                        8 <= len(s) <= 20 and
                        any(map(str.islower, s)) and
                        any(map(str.isupper, s)) and
                        any(map(str.isdigit, s))  and
                        any(map(lambda x: x in '!@#$%^&*?', s))
                        ) else 'not valid'
```

---

[Codewars link](https://www.codewars.com/kata/57e35f1bc763b8ccce000038)
