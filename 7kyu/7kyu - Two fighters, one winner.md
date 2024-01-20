## Two fighters, one winner - 7kyu

**Instructions**

- Create a function that returns the name of the winner in a fight between two fighters.

- Each fighter takes turns attacking the other and whoever kills the other first is victorious.

- Death is defined as having health <= 0.

- Each fighter will be a Fighter instance.

- Both health and damage_per_attack will be integers larger than 0.

- You can mutate the Fighter objects.

---

#### Test cases

```python
print(declare_winner(Fighter("Lew", 10, 2), Fighter("Harry", 5, 4), "Lew"))
print(declare_winner(Fighter("Lew", 10, 2), Fighter("Harry", 5, 4), "Harry"))
print(declare_winner(Fighter("Harald", 20, 5), Fighter("Harry", 5, 4), "Harry"))
print(declare_winner(Fighter("Harald", 20, 5), Fighter("Harry", 5, 4), "Harald"))
print(declare_winner(Fighter("Jerry", 30, 3), Fighter("Harald", 20, 5), "Jerry"))
print(declare_winner(Fighter("Jerry", 30, 3), Fighter("Harald", 20, 5), "Harald"))
```

#### Output

```
Lew
Harry
Harald
Harald
Harald
Harald
```

---

#### Solution

```python
class Fighter(object):
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack

def declare_winner(fighter1, fighter2, first_attacker):
    cur, opp = (fighter1, fighter2) if first_attacker == fighter1.name else (fighter2, fighter1)
    while cur.health > 0:
        opp.health -= cur.damage_per_attack
        cur, opp = opp, cur
    return opp.name
```

---

[Codewars link](https://www.codewars.com/kata/577bd8d4ae2807c64b00045b)
