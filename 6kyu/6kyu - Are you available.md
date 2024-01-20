## Are you available? - 6kyu

**Instructions**

- Write a helper function `check_availability` that will take 2 arguments:

- `schedule`, which is going to be a nested array with Dan's schedule for a given day. Inside arrays will consist of 2 elements - start and finish time of a given appointment.

- `current_time` - is a string with specific time in hh:mm 24-h format for which the function will check availability based on the schedule.

- If no appointments are scheduled for `current_time`, the function should return `True`.

- If there are no appointments for the day, the output should also be `True`

- If Dan is in the middle of an appointment at `current_time`, the function should return a string with the time he's going to be available.

---

#### Test cases

```python
print(check_availability([['09:30', '10:15'], ['12:20', '15:50']], '10:00'))
print(check_availability([['09:30', '10:15'], ['12:20', '15:50']], '11:00'))
```

#### Output
```
10:15
True
```

---

#### Solution

```python
def check_availability(schedule, current_time):
    for ts, te in schedule:
        if ts <= current_time < te:
            return te
    return True
```

---


[Codewars link](https://www.codewars.com/kata/5603002927a683441f0000cb)
