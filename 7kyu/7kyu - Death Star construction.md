## Death Star Construction - 7kyu

**Instructions**

- The construction of the new Death Star is almost complete. It only needs a certain amount of 3 materials – iron, steel, and chromium. The emperor wants the construction finished within a week because he senses an impending rebel attack and knows the battle station will be destroyed if it is not completed within this timeframe. He has already ordered enough material delivered to the station within a week. The problem is, the rebels are attacking the supply routes and there are different amounts of material arriving at the station each week. Will the station be ready in time or will it be destroyed?

- The required resources are:

    - 100 Gt of iron

    - 75 Gt of steel

    - 50 Gt of chromium

- The input will consist of an array with 8 elements:

    - The first 7 elements are the shipments - 3-elements-long arrays where each number corresponds to the amount of material that was ordered (iron, steel, and chromium)

    - The last element is a number representing the day of the rebel attack (0-indexed) - any materials which should have been delivered that day will be lost, and later shipments will be cancelled due to the trading route becoming unsafe

- Output:

    - If enough resources are delivered before the attack, return "The station is completed!"

    - Otherwise, return "The station is destroyed! It needed X iron, Y steel and Z chromium for completion.", where X, Y and Z are the quantities of the respective material

---

#### Test cases

```python
print(death_star([[100, 75, 49], [20, 15, 20], [10, 15, 10], [50, 50, 20], [20, 15, 10], [20, 15, 10], [20, 15, 10]], 1))
print(death_star([[20, 15, 10], [20, 15, 20], [10, 15, 10], [50, 50, 20], [20, 15, 10], [20, 15, 10], [20, 15, 10]], 5))
```

#### Output
```
The station is destroyed! It needed 0 iron, 0 steel and 1 chromium for completion.
The station is completed!
```

---

#### Solution

```python
def death_star(week, attack):
    day = 0
    t_i, t_s, t_c = 0, 0, 0
    while day < attack:
        t_i += week[day][0]
        t_s += week[day][1]
        t_c += week[day][2]
        day += 1
    return "The station is " + (f"destroyed! It needed {max(0, 100 - t_i)} iron, {max(0, 75 - t_s)} steel and {max(0, 50 - t_c)} chromium for completion.", "completed!")[all([t_i >= 100, t_s >= 75, t_c >= 50])]
```

---


[Codewars link](https://www.codewars.com/kata/5a996f3d5084d73a7100040c)
