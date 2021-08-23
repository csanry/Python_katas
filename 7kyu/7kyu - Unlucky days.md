## Unlucky Days - 7kyu

**Instructions**

- Given a year as an integer, output the number of Black Fridays in the year.

- A Black Friday is a Friday that falls on the 13th.

---

#### Test cases

```python
print(unlucky_days(2015))
print(unlucky_days(1986))
```

#### Output 
```
3
1
```

---

#### Solution

```python
def unlucky_days(year):
    import datetime 
    return sum(datetime.date(year, month, 13).weekday() == 4 for month in range(1, 13))
```

---

[Codewars link](https://www.codewars.com/kata/56eb0be52caf798c630013c0)
