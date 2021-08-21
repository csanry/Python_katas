## The Office II - 7kyu

**Instructions**

- Every now and then people in the office moves teams or departments.

- Depending what people are doing with their time they can become more or less boring. Time to assess the current team.

- You will be provided with a dictionary `staff` containing staff names as keys and department they work in as values.

- Each department has a different `boredom` assessment score, provided in the following dictionary:

```Python
boredom_scores = {
    'accounts': 1,
    'finance': 2,
    'canteen': 10,
    'regulation': 3,
    'trading': 6,
    'change': 6,
    'IS': 8,
    'retail': 5,
    'cleaning': 4,
    'pissing about': 25
}
```

- Depending on the cumulative score of the team, return the appropriate sentiment:

```
<=80: 'kill me now'
< 100 & > 80: 'i can handle this'
100 or over: 'party time!!'
```

---

#### Test cases

```python
boredom({'a': 'change', 'b': 'cleaning'})
boredom({'a': 'pissing about', 'b': 'pissing about', 'c': 'pissing about', 'd': 'pissing about'})
```

#### Output
```
kill me now
party time!!
```

---

#### Solution

```python
def boredom(staff):
    score = sum(map(boredom_scores.get, staff.values()))
    return (
        'kill me now' if score <= 80 else
        'i can handle this' if score < 100 else
        'party time!!')
```

---

[Codewars link](https://www.codewars.com/kata/the-office-ii-boredom-score)
