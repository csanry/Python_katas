## Sort Out The Men From Boys - 7kyu

**Instructions**

- Men are the even numbers and Boys are the odds.

- Given an array of n integers, separate the even numbers from the odds.

- Return an array/list where even numbers come first then odds.

- Arrange the even numbers in ascending order while odds in descending.

---

#### Test cases

```python
print(men_from_boys([82, 91, 72, 76, 76, 100, 85]))
print(men_from_boys([2, 15, 17, 15, 2, 10, 10, 17, 1, 1]))
print(men_from_boys([-32, -39, -35, -41]))
print(men_from_boys([-64, -71, -63, -66, -65]))
print(men_from_boys([-17, -45, -15, -33, -85, -56, -86, -30]))
print(men_from_boys([82, -61, -87, -12, 21, 1]))
print(men_from_boys([63, -57, 76, -85, 88, 2, -28]))
```

#### Output
```
[72, 76, 82, 100, 91, 85]
[2, 10, 17, 15, 1]
[-32, -35, -39, -41]
[-66, -64, -63, -65, -71]
[-86, -56, -30, -15, -17, -33, -45, -85]
[-12, 82, 21, 1, -61, -87]
[-28, 2, 76, 88, 63, -57, -85]
```

---

#### Solution

```python
def men_from_boys(arr):
    men, boys = [], []
    for i in set(arr):
        boys.append(i) if i%2 else men.append(i)
    return sorted(men) + sorted(boys)[::-1]
```

---

[Codewars link](https://www.codewars.com/kata/5af15a37de4c7f223e00012d)
