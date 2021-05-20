## Determine offspring sex based on genes XX and XY chromosomes - 8kyu

**Instructions**

- Determine if the sex of the offspring will be male or female based on the X or Y chromosome present in the male's sperm.

---

#### Test cases

```python
print(chromosome_check('XY'))
print(chromosome_check('XX'))
```

#### Output 

```
Congratulations! You're going to have a son.
Congratulations! You're going to have a daughter.
```

---

#### Solution

```python
def chromosome_check(sperm):
    return f"Congratulations! You're going to have a {'son' if 'Y' in sperm else 'daughter'}."
```

---

[Codewars link](https://www.codewars.com/kata/56530b444e831334c0000020)
