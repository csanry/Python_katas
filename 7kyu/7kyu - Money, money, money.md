## Money, money, money - 7kyu

**Instructions**

- Given a sum `P`, calculate the amount of years required to amount to a sum of money `D`.

- Interest `I` is paid yearly. After paying taxes `T` for the year the new sum is reinvested.

- Only the year's accrued interest is taxed.

```
  Let P be the Principal = 1000.00      
  Let I be the Interest Rate = 0.05      
  Let T be the Tax Rate = 0.18      
  Let D be the Desired Sum = 1100.00

After 1st Year -->
  P = 1041.00
After 2nd Year -->
  P = 1083.86
After 3rd Year -->
  P = 1128.30
Therefore years required is 3
```

---

#### Test cases

```python
print(calculate_years(1000, 0.05, 0.18, 1100))
print(calculate_years(1000,0.01625,0.18,1200))
print(calculate_years(1000,0.05,0.18,1000))
```

#### Output 
```
3 
14
0
```

---

#### Solution

```python
def calculate_years(P, I, T, D):
    years = 0
    while P < D:
        i = P * I * (1 - T)
        P += i; years += 1
    return years
```

---

[Codewars link](https://www.codewars.com/kata/563f037412e5ada593000114)
