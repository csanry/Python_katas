## Get Planet Name By ID - 8kyu

**Instructions**

- Given an ID, return the corresponding planet.

---

#### Test cases

```python
print(get_planet_name(2))
print(get_planet_name(5))
print(get_planet_name(3))
print(get_planet_name(4))
print(get_planet_name(8))
print(get_planet_name(1))
```

#### Output

```
Venus
Jupiter
Earth
Mars
Neptune
Mercury
```

---

#### Solution

```python
def get_planet_name(id):
    d = {1: 'Mercury', 2: 'Venus', 3: 'Earth', 4: 'Mars', 5: 'Jupiter',
         6: 'Saturn', 7: 'Uranus', 8: 'Neptune'}
    return d.get(id)
```

---

[Codewars link](https://www.codewars.com/kata/515e188a311df01cba000003)
