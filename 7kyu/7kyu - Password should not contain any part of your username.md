## Password should not contain any part of your username - 7kyu

**Instructions**

- For any password and username pair, the length of the longest common substring should be less than half the length of the shortest of the two.

- Return True if the rule is followed, else False.

---

#### Test cases

```python
print(validate("", ""))
print(validate("username", "myname"))
print(validate("sword", "password" ))
print(validate("qwertyuiop", "asdfghjkl"))
print(validate("MASH", "M*A*S*H"))
print(validate("asdfghjkl", "lkjhgfdsa"))
```

#### Output
```
False
False
False
True
True
True
```

---

#### Solution

```python
def validate(username, password):
    short, long = sorted((username, password), key = len)
    max_length = (len(short) + 1) // 2
    return all(short[i:i+max_length] not in long for i in range(max_length)) and max_length > 0
```

---

[Codewars link](https://www.codewars.com/kata/5c511d8877c0070e2c195faf)
