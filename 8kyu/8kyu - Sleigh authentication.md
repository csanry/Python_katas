## Sleigh Authentication - 8kyu

**Instructions**

- Your task is to implement the `authenticate()` method of the sleigh class.

- `authenticate()` takes the name of the person, who wants to board the sleigh and a secret password. 

- If the name equals `Santa Claus` and the password is `Ho Ho Ho!`, return `True`. Otherwise, return `False`.

---

#### Test cases

```python
sleigh = Sleigh()
print(sleigh.authenticate('Santa Claus', 'Ho Ho Ho!'))
print(sleigh.authenticate('Santa', 'Ho Ho Ho!'))
print(sleigh.authenticate('Santa Claus', 'Ho Ho!'))
print(sleigh.authenticate('jhoffner', 'CodeWars'))
```

#### Output 

```
True
False
False
False
```

---

#### Solution

```python
class Sleigh:
    @staticmethod
    def authenticate(name='', password=''):
        return name == 'Santa Claus' and password == 'Ho Ho Ho!'
```

---

[Codewars link](https://www.codewars.com/kata/52adc142b2651f25a8000643)
