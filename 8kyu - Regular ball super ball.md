## Regular Ball Super Ball - 8kyu

**Instructions**

- Create a class Ball.

- Ball objects accept one argument for "ball type" when instantiated.

- If no arguments are given, ball objects should instantiate with a ball type of "regular".

---

#### Test cases

```python
print(Ball().ball_type)
print(Ball('super').ball_type)
```

#### Output 
```
regular
super
```

---

#### Solution

```python
class Ball:
    def __init__(self, ball_type = 'regular'):
        self.ball_type = ball_type
```

---

[Codewars link](https://www.codewars.com/kata/53f0f358b9cb376eca001079)
