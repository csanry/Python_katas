## Simple Fun #3: Late Ride - 7kyu

**Instructions**

- One night you go for a ride on your motorcycle. At 00:00 you start your engine, and the built-in timer automatically begins counting the length of your ride, in minutes. 

- Given `n` as the minutes passed since 00:00, calculate the current time. 

- Return an answer as the sum of digits that the digital timer in the format hh:mm would show.

---

#### Test cases

```python
print(late_ride(240))
print(late_ride(808))
print(late_ride(1439))
print(late_ride(0))
print(late_ride(23))
print(late_ride(8))
```

#### Output 
```
4
14
19
0
5
8
```

---

#### Solution

```python
def late_ride(n):
    h, m = divmod(n, 60)
    return sum(map(int, str(h) + str(m)))
```

---

[Codewars link](https://www.codewars.com/kata/588422ba4e8efb583d00007d)
