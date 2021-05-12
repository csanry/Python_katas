## Get ASCII value of character - 8kyu

**Instructions**

- Get the ASCII value of a character.

---

#### Test cases

```python
print(get_ascii("A"))
print(get_ascii(" "))
print(get_ascii("!"))
```

#### Output 

```
65
32
33
```

---

#### Solution

```python
def get_ascii(chr):
    return ord(chr)
```

---

[Codewars link](https://www.codewars.com/kata/55acfc59c3c23d230f00006d)
