## The coupon code - 7kyu

**Instructions**

- Your online store likes to give out coupons for special occasions. Some customers try to cheat the system by entering invalid codes or using expired coupons.

- Write a function which verifies that a coupon code is valid and not expired.

- A coupon is no more valid on the day after the expiration date.

- All dates will be passed as strings in this format: `MONTH DATE, YEAR`.

---

#### Test cases

```python
print(check_coupon("123", "123", "July 9, 2015", "July 9, 2015"))
print(check_coupon("123", "123", "July 9, 2015", "July 2, 2015"))
```

#### Output

```
True
False
```

---

#### Solution

```python
from datetime import datetime as dt

def check_coupon(entered_code, correct_code, current_date, expiration_date):
    d = lambda st: dt.strptime(st, '%B %d, %Y')
    return entered_code is correct_code and d(current_date) <= d(expiration_date)
```

---

[Codewars link](https://www.codewars.com/kata/539de388a540db7fec000642)
