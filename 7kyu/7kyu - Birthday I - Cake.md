## Birthday I - Cake - 7kyu

**Instructions**

- It's your Birthday. The numbers of candles on the cake is provided (x). Please note this is not reality, and your age can be anywhere up to 1,000.

- As a surprise, your colleagues have arranged for your friend to hide inside the cake and burst out.

- When your friend jumps out of the cake, he/she will knock some of the candles to the floor. If the number of candles that fall is higher than 70% of total candles (x), the carpet will catch fire.

- You will work out the number of candles that will fall from the provided string `y`.

- You must add up the character ASCII code of each even indexed (assume a 0 based indexing) character in `y`, with the alphabetical position of each odd indexed character in `y` to give the string a total.

```
example: 'abc' > a=97, b=2, c=99 > y total = 198.
```

---

#### Test cases

```python
print(cake(900, 'abcdef'))
print(cake(56, 'ifkhchlhfd'))
print(cake(256, 'aaaaaddddr'))
print(cake(333, 'jfmgklfhglbe'))
print(cake(12, 'jaam'))
```

#### Output

```
That was close!
Fire!
Fire!
Fire!
Fire!
```

---

#### Solution

```python
def cake(candles, debris):
    # even index -> get ascii code
    # odd index -> get position

    tot = sum(ord(v) - 96 if i & 1 else ord(v) for i, v in enumerate(debris))
    if tot > candles * 0.7 and candles > 0:
        return 'Fire!'
    return 'That was close!'
```

---

[Codewars link](https://www.codewars.com/kata/5805ed25c2799821cb000005/)
