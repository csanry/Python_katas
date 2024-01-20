## Draw stairs - 8kyu

**Instructions**

- Given a number `n`, draw stairs using the letter `I`, `n` tall and `n` wide, with the tallest in the top left.

- For example `n = 3` result in:

```
I
 I
  I
```

---

#### Test cases

```python
print(draw_stairs(3))
```

#### Output

```
I\n I\n  I
```

---

#### Solution

```python
def draw_stairs(n):
    return '\n'.join(f'{i * " "}I' for i in range(n))
```

---

[Codewars link](https://www.codewars.com/kata/5b4e779c578c6a898e0005c5)
