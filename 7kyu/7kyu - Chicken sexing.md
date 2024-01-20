## Chicken sexing - 7kyu

**Instructions**

- Bob is a chicken sexer. His job is to sort baby chicks into a Male(M) and Female(F) piles. When Bob can't guess, he marks it with a '?'.

- Bob's bosses don't trust Bob's ability just yet, so they have paired him with an expert sexer.

- All of Bob's decisions will be checked against the experts choices to generate a correctness score.

    - When they agree, he gets 1 point.

    - When they disagree but one has said '?', he gets 0.5 points.

    - When they disagree completely, he gets 0 points.

---

#### Test cases

```python
print(correctness(('M', 'F', '?'), ('M', 'F', '?')))
print(correctness(('M', '?', 'M'), ('M', 'F', '?')))
print(correctness(('F', 'M', 'F'), ('M', 'F', 'M')))
```

#### Output
```
3
2
0
```

---

#### Solution

```python
def correctness(bob, exp):
    return sum(1 if b == e
               else 0.5 if '?' in (b, e)
               else 0
               for (b, e) in zip(bob, exp))
```

---


[Codewars link](https://www.codewars.com/kata/57ed40e3bd793e9c92000fcb)
