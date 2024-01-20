## Extended weekends - 7kyu

**Instructions**

- If the first day of the month is a Friday, it is likely that the month will have an Extended Weekend.

- That is, it could have five Fridays, five Saturdays and five Sundays.

- Given a start year and an end year, find months that have extended weekends and return:

    - The first and last month in the range that has an extended weekend.

    - The number of months that have extended weekends in the range, inclusive of start year and end year.

---

#### Test cases

```python
print(solve(2016, 2020))
print(solve(1900, 1950))
print(solve(1800, 2500))
```

#### Output

```
('Jan', 'May', 5)
('Mar', 'Dec', 51)
('Aug', 'Oct', 702)
```

---

#### Solution

```python
from datetime import date
def solve(a,b):
    first = None
    count = 0
    for year in range(a, b+1):
        for month in (1, 3, 5, 7, 8, 10, 12):
            d = date(year, month, 1)
            if d.isoweekday() == 5:
                last = d.strftime('%b')
                if first is None:
                    first = last
                count += 1
    return first, last, count
```

---

[Codewars link](https://www.codewars.com/kata/5be7f613f59e0355ee00000f)
