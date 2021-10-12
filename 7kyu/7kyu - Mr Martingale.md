## Mr Martingale - 7kyu

**Instructions**

- You will be given a starting cash balance and an array of binary digits to represent a win (1) or a loss (0). 

- Return your balance after playing all rounds, applying the Martingale strategy.

**The Martingale strategy**

- You start with a stake of 100 dollars. 

- If you lose a round, you lose the stake placed on that round and you double the stake for your next bet. 

- When you win, you win 100% of the stake and revert back to staking 100 dollars on your next bet.

---

#### Test cases

```python
print(martingale(500, []))
print(martingale(1000, [1, 1, 0, 0, 1]))
print(martingale(0, [0, 0, 0, 0, 1, 0, 0,]))
print(martingale(5100, [1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0]))
print(martingale(-500, [1, 1, 0, 1, 0, 1, 0]))
```

#### Output 

```
500
1300
-200
5600
-200
```

---

#### Solution

```python
def martingale(bank, outcomes):
    bet = 100
    for win in outcomes:
        if win:
            bank += bet
            bet = 100
        else:
            bank -= bet
            bet *= 2
    return bank
```

---

[Codewars link](https://www.codewars.com/kata/5eb34624fec7d10016de426e)
