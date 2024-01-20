## Fizz buzz cuckoo clock - 7kyu

**Instructions**

- Given a string containing hour and minute values in 24-hour time, separated by a colon, and with leading zeros:

- Write a function to select from the sounds you had recorded depending on the time.

    - When a minute is evenly divisible by three, the clock will say the word "Fizz".

    - When a minute is evenly divisible by five, the clock will say the word "Buzz".

    - When a minute is evenly divisible by both, the clock will say "Fizz Buzz", with two exceptions:

    - On the hour, instead of "Fizz Buzz", the clock door will open, and the cuckoo bird will come out and "Cuckoo" between one and twelve times depending on the hour.

        - On the half hour, instead of "Fizz Buzz", the clock door will open, and the cuckoo will come out and "Cuckoo" just once.

        - With minutes that are not evenly divisible by either three or five, at first you had intended to have the clock just say the numbers ala Fizz Buzz, but then you decided at least for version 1.0 to just have the clock make a quiet, subtle "tick" sound for a little more clock nature and a little less noise.

---

#### Test cases

```python
print(fizz_buzz_cuckoo_clock("13:34"))
print(fizz_buzz_cuckoo_clock("21:00"))
print(fizz_buzz_cuckoo_clock("11:15"))
print(fizz_buzz_cuckoo_clock("03:03"))
print(fizz_buzz_cuckoo_clock("14:30"))
print(fizz_buzz_cuckoo_clock("08:55"))
print(fizz_buzz_cuckoo_clock("00:00"))
print(fizz_buzz_cuckoo_clock("12:00"))
```

#### Output

```
tick
Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo
Fizz Buzz
Fizz
Cuckoo
Buzz
Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo
Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo
```

---

#### Solution

```python
def fizz_buzz_cuckoo_clock(time):
    h, m = map(int, time.split(':'))
    h = h - 12 if h > 12 else 12 if h == 0 else h

    if m == 0:
        return ' '.join('Cuckoo' for _ in range(h))
    elif m == 30:
        return 'Cuckoo'
    else:
        return ('Fizz ' * (m % 3 == 0) + 'Buzz' * (m % 5 == 0)).strip() or 'tick'
```

---

[Codewars link](https://www.codewars.com/kata/58485a43d750d23bad0000e6)
