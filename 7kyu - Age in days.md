## Age in days - 7kyu

**Instructions**

- Complete the function which returns your age in days. 

- The birthday is given in the following order: year, month, day.

- The birthday is expected to be in the past.

---

#### Test cases

```python
# today = 21/7/2021
print(age_in_days(2021, 7, 19))
print(age_in_days(2021, 6, 21))
```

#### Output 
```
You are 2 days old
You are 30 days old
```

---

#### Solution

```python
import datetime as dt

def age_in_days(year, month, day):
    return "You are {} days old".format((dt.date.today() - dt.date(year, month, day)).days)
```

---

[Codewars link](https://www.codewars.com/kata/5803753aab6c2099e600000e)
