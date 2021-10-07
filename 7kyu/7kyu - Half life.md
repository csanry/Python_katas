## Half Life - 7kyu

**Instructions**

- Given the birthdates of two people, find the date when the younger one is exactly half the age of the other.

- The dates are given in the format YYYY-MM-DD and are not sorted in any particular order.

- Round down to the nearest day.

- Return the result as a string, like the input dates.

---

#### Test cases

```python
print(half_life("1990-12-06", "2000-02-29"))
print(half_life("2012-03-31", "1990-06-09"))
print(half_life("1984-08-14", "1990-04-17"))
print(half_life("2000-06-30", "1978-03-17"))
print(half_life("1969-12-20", "2000-10-07"))
```

#### Output 

```
2009-05-24
2034-01-21
1995-12-19
2022-10-14
2031-07-26
```

---

#### Solution

```python
from datetime import datetime
def half_life(person1, person2):
    fmt = '%Y-%m-%d'
    d1, d2 = map(lambda s: datetime.strptime(s, fmt), sorted((person1, person2)))
    return datetime.strftime(d2 + (d2 - d1), fmt)
```

---

[Codewars link](https://www.codewars.com/kata/5d472159d4f8c3001d81b1f8)
