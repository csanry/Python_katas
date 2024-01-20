## All Star Code Challenge #23 - 6kyu

**Instructions**

- Create a function that takes an array of players and returns an array of player names, in order of descending score.

- Each player's score is calculated as follows:

    - Each normal kill is worth 100 points.

    - Each assist is worth 50 points.

    - Each point of damage done is worth 0.5 points.

    - Each point of healing done is worth 1 point.

    - The longest kill streak is worth 2^N, where N is the number of kills of the streak.

    - Environmental kills are worth 500 points.

---

#### Test cases

```python
p1 = {
  "name": "JuanPablo", "norm_kill": 5, "assist": 12,
  "damage": 3200, "healing": 0, "streak": 4, "env_kill": 1}
p2 = {
  "name": "ProfX", "norm_kill": 2, "assist": 14, "damage": 600,
  "healing": 1500, "streak": 0, "env_kill": 0}
p3 = {
  "name": "Ajna", "norm_kill": 1, "assist": 8, "damage": 900,
  "healing": 30, "streak": 3, "env_kill": 5}

print(scoring([p1]))
print(scoring([p1, p2]))
print(scoring([]))
print(scoring([p1, p3, p2]))
```

#### Output

```
['JuanPablo']
['JuanPablo', 'ProfX']
[]
['Ajna', 'JuanPablo', 'ProfX']
```

---

#### Solution

```python
def scoring(array):
    res, players = [], []
    for p in array:
        score = 100 * p['norm_kill'] + 50 * p['assist'] + 0.5 * p['damage'] +\
                p['healing'] + 500 * p['env_kill'] + 2 ** p['streak']
        res.append(score)
        players.append(p['name'])
    return [name for _, name in sorted(zip(res, players))[::-1]]
```

---

[Codewars link](https://www.codewars.com/kata/5865dd726b56998ec4000185)
