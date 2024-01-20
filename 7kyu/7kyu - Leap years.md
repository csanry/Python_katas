## Leap Years - 7kyu

**Instructions**

- Determine whether a given year is a leap year or not.

- Years divisible by 4 are leap years.

- Years divisible by 100 are not leap years but years divisible by 400 are leap years.

---

#### Test cases

```python
print(is_leap_year(1984))
print(is_leap_year(2000))
print(is_leap_year(1234))
print(is_leap_year(1100))
```

#### Output
```
True
True
False
False
```

---

#### Solution

```python
import calendar

def is_leap_year(year):
    # if calendar is not available:
    # return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    return calendar.isleap(year)
```

---

[Codewars link](https://www.codewars.com/kata/526c7363236867513f0005ca)
