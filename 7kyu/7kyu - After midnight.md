## After(?) midnight - 7kyu

**Instructions**

- Write a function that takes a negative or positive integer, which represents the number of minutes before (-) or after (+) Sunday midnight.

- Return the current day of the week and the current time in 24hr format ('hh:mm') as a string.

---

#### Test cases

```python
print(day_and_time(0))
print(day_and_time(-3))
print(day_and_time(45))
print(day_and_time(759))
print(day_and_time(1236))
print(day_and_time(1447))
print(day_and_time(7832))
print(day_and_time(18876))
print(day_and_time(259180))
print(day_and_time(-349000))
```

#### Output 
```
Sunday 00:00
Saturday 23:57
Sunday 00:45
Sunday 12:39
Sunday 20:36
Monday 00:07
Friday 10:32
Saturday 02:36
Thursday 23:40
Tuesday 15:20
```

---

#### Solution

```python
import datetime as dt
def day_and_time(mins):
    sunday = dt.datetime(2021, 1, 3, 0, 0, 0)
    new = sunday + dt.timedelta(minutes = mins)
    return new.strftime('%A %H:%M')
```

---

[Codewars link](https://www.codewars.com/kata/56fac4cfda8ca6ec0f001746)
