## Graceful Tipping - 7kyu

**Instructions**

- Adding tip to a restaurant bill in a graceful way can be tricky, that's why you need make a function for it.

- The function will receive the restaurant bill (always a positive number) as an argument. You need to: 
    1. add at least 15% in tip
    2. round that number up to an elegant value 
    3. return it.

- What is an elegant number? It depends on the magnitude of the number to be rounded. 

- Numbers below 10 should simply be rounded to whole numbers. Numbers 10 and above should be rounded like this:

    1. 10 - 99.99... ---> Round to number divisible by 5
    2. 100 - 999.99... ---> Round to number divisible by 50
    3. 1000 - 9999.99... ---> Round to number divisible by 500 and so on

---

#### Test cases

```python
print(graceful_tipping(1))
print(graceful_tipping(7))
print(graceful_tipping(12))
print(graceful_tipping(86))
print(graceful_tipping(99))
print(graceful_tipping(1149))
print(graceful_tipping(983212))
```

#### Output 
```
2
9
15
100
150
1500
1500000
```

---

#### Solution

```python
import math
def graceful_tipping(bill):
    bill *= 1.15
    if bill < 10: 
        return math.ceil(bill)
    e = int(math.log10(bill))
    unit = (10 ** e) / 2
    return math.ceil(bill / unit) * unit
```

---

[Codewars link](https://www.codewars.com/kata/5eb27d81077a7400171c6820)
