## Greed is Good - 5kyu

**Instructions**

- Greed is a dice game played with five six-sided dice.

- Your mission is to score a throw according to these rules.

**Scoring scheme**

```
 Three 1's => 1000 points
 Three 6's =>  600 points
 Three 5's =>  500 points
 Three 4's =>  400 points
 Three 3's =>  300 points
 Three 2's =>  200 points
 One   1   =>  100 points
 One   5   =>   50 point
```

- You will always be given an array with five six-sided dice values.

- A single die can only be counted once in each roll.

- For example, a given "5" can only count as part of a triplet (contributing to the 500 points) or as a single 50 points, but not both in the same roll.

**Example scoring**

```
Throw       Score
 ---------   ------------------
 5 1 3 4 1   250:  50 (for the 5) + 2 * 100 (for the 1s)
 1 1 1 3 1   1100: 1000 (for three 1s) + 100 (for the other 1)
 2 4 4 5 4   450:  400 (for three 4s) + 50 (for the 5)
```


---

#### Test cases

```python
print(score([2, 3, 4, 6, 2]))
print(score([4, 4, 4, 3, 3]))
print(score([2, 4, 4, 5, 4]))
```

#### Output
```
0
400
450
```

---

#### Solution

```python
from collections import Counter
def score(dice):
    triples = {1: 1000, 2: 200, 3: 300, 4: 400, 5: 500, 6: 600}
    singles = {1: 100, 2: 0, 3: 0, 4: 0, 5: 50, 6: 0}
    res = Counter(dice)
    return sum(triples.get(k, 0) * (v//3) + singles.get(k, 0) * (v%3) for k, v in res.items())
```

---


[Codewars link](https://www.codewars.com/kata/5270d0d18625160ada0000e4)
