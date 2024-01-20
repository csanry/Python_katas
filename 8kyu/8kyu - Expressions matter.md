## Expressions matter - 8kyu

**Instructions**

- Given three integers `a, b, c` return the largest number obtained after inserting the following operators and brackets: `+, *, ()`.

- In other words, try every combination of a,b,c with `*+()`, and return the maximum.

---

#### Test cases

```python
print(expression_matter(2, 2, 2))
print(expression_matter(5, 1, 3))
print(expression_matter(3, 5, 7))
print(expression_matter(5, 6, 1))
print(expression_matter(1, 6, 1))
print(expression_matter(2, 6, 1))
```

#### Output

```
8
20
105
35
8
14
```

---

#### Solution

```python
def expression_matter(a, b, c):
    return max(a+b+c, a*b*c, (a+b)*c, a*(b+c))
```

---

[Codewars link](https://www.codewars.com/kata/5ae62fcf252e66d44d00008e)
