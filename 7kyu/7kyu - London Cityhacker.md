## London CityHacker - 7kyu

**Instructions**

- You are given a sequence of a journey in London, UK. The sequence will contain bus numbers and TFL tube names as strings e.g.

```python
['Northern', 'Central', 243, 1, 'Victoria']
```

- Journeys will always only contain a combination of tube names and bus numbers.

- Each tube journey costs £2.40 and each bus journey costs £1.50.

- If there are 2 or more adjacent bus journeys, the bus fare is capped for sets of two adjacent buses and calculated as one bus fare for each set.

- Calculate the total cost of the journey and return the cost rounded to 2 decimal places in the format (where x is a number): £x.xx

---

#### Test cases

```python
print(london_city_hacker([12, 'Central', 'Circle', 21]))
print(london_city_hacker(['Piccidilly', 56]))
print(london_city_hacker(['Northern', 'Central', 'Circle']))
print(london_city_hacker(['Piccidilly', 56, 93, 243]))
print(london_city_hacker([386, 56, 1, 876]))
```

#### Output
```
£7.80
£3.90
£7.20
£5.40
£3.00
```

---

#### Solution

```python
def london_city_hacker(journey):
    total, consec = 0, 0
    for ride in journey:
        if type(ride) is str:
            consec = 0
            total += 2.40
        else:
            consec += 1
            if consec == 2:
                consec = 0
                continue
            total += 1.50
    return f'£{total:.2f}'
```

---

[Codewars link](https://www.codewars.com/kata/5bce125d3bb2adff0d000245)
