## Spraying Trees - 7kyu

**Instructions**

- There are five workers : James, John, Robert, Michael and William.

- They work one by one and on weekends they rest.

- Order is same as in the description (James works on Monday,John works on Tuesday and so on).

- You have to create a function `task` that will take 3 arguments `w`, `n`, `c`:

- `w`: Weekday

- `n`: Number of trees that must be sprayed on that day

- `c`: Cost of 1 litre liquid that is needed to spray tree, let's say one tree needs 1 litre liquid.

- Let the cost of all liquids be `x`

- Return a string like this: 'It is `(weekday)` today, `(name)`, you have to work, you must spray `(number)` trees and you need `(x)` dollars to buy liquid'

---

#### Test cases

```python
print(task('Wednesday',10,2))
print(task('Monday',4,3))
print(task('Friday',5,4))
print(task('Tuesday',6,1))
print(task('Thursday',5,3))
```

#### Output
```
It is Wednesday today, Robert, you have to work, you must spray 10 trees and you need 20 dollars to buy liquid
It is Monday today, James, you have to work, you must spray 4 trees and you need 12 dollars to buy liquid
It is Friday today, William, you have to work, you must spray 5 trees and you need 20 dollars to buy liquid
It is Tuesday today, John, you have to work, you must spray 6 trees and you need 6 dollars to buy liquid
It is Thursday today, Michael, you have to work, you must spray 5 trees and you need 15 dollars to buy liquid
```

---

#### Solution

```python
def task(w, n, c):
    worker = {'Monday': 'James', 'Tuesday': 'John', 'Wednesday': 'Robert', 'Thursday': 'Michael', 'Friday': 'William'}
    return f"It is {w} today, {worker[w]}, you have to work, you must spray {n} trees and you need {n*c} dollars to buy liquid"

```

---


[Codewars link](https://www.codewars.com/kata/5981a139f5471fd1b2000071)
