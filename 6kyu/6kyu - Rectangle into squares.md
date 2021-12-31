## Rectangle into Squares - 6kyu

**Instructions**

- You will be given two dimensions `l` and `w` of a true rectangle.

- Break down the rectangle into squares.

- Return a collection of the size of each squares.

---

#### Test cases

```python
print(sq_in_rect(5, 5))
print(sq_in_rect(5, 3))
print(sq_in_rect(20, 14))
print(sq_in_rect(37, 14))
```

#### Output 

```
None
[3, 2, 1, 1]
[14, 6, 6, 2, 2, 2]
[14, 14, 9, 5, 4, 1, 1, 1, 1]
```

---

#### Solution

```python
def sq_in_rect(l, w):
    if l == w:
        return None
    l, w, res = max(l, w), min(l, w), []
    while w:
        res.append(w)
        if 2 * w >= l:
            w, l = l - w, w
        else:
            l -= w
    return res
```

---

[Codewars link](https://www.codewars.com/kata/55466989aeecab5aac00003e)
