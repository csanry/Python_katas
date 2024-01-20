## Bus timer - 7kyu

**Instructions**

- There is a bus that goes to your office every 15 minutes, the first bus is at 06:00, and the last bus is at 00:00.

- It takes 5 minutes to walk from your front door to the bus stop.

- Implement a function that when given the current time, will tell you much time is left, before you must leave to catch the next bus.

- Input will be formatted as HH:MM (24-hour clock).

---

#### Test cases

```python
print(bus_timer("10:00"))
print(bus_timer("15:05"))
print(bus_timer("06:10"))
```

#### Output

```
10
5
0
```

---

#### Solution

```python
def bus_timer(current_time):
    hr, mn = map(int, current_time.split(':'))

    if hr < 6:
        mn = (5 - hr) * 60 + 60 - mn
    elif hr == 23 and mn > 55:
        return 355 + 60 - mn
    else:
        mn = 15 - mn % 15

    return mn - 5 if mn > 4 else mn + 10
```

---

[Codewars link](https://www.codewars.com/kata/5736378e3f3dfd5a820000cb)
