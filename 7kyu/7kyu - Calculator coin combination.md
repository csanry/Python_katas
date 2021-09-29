## Calculator: Coin Combination - 7kyu

**Instructions**

- The function takes cents value (int) and needs to return the minimum number of coins combination of the same value.

- The function should return an array where
    - coins[0] = pennies ==> $00.01
    
    - coins[1] = nickels ==> $00.05
    
    - coins[2] = dimes ==> $00.10
    
    - coins[3] = quarters ==> $00.25
    
---

#### Test cases

```python
print(coin_combo(2346))
print(coin_combo(325))
print(coin_combo(6))
print(coin_combo(11))
print(coin_combo(27))
print(coin_combo(23))
print(coin_combo(934))
```

#### Output 
```
[1, 0, 2, 93]
[0, 0, 0, 13]
[1, 1, 0, 0]
[1, 0, 1, 0]
[2, 0, 0, 1]
[3, 0, 2, 0]
[4, 1, 0, 37]
```

---

#### Solution

```python
def coin_combo(cents):
    quarters, cents = divmod(cents, 25)
    dimes, cents = divmod(cents, 10)
    nickels, cents = divmod(cents, 5)
    return [cents, nickels, dimes, quarters]
```

---

[Codewars link](https://www.codewars.com/kata/564d0490e96393fc5c000029)
