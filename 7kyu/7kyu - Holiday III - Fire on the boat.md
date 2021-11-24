## Fire on the boat - 7kyu

**Instructions**

- Enjoying your holiday, you head out on a scuba diving trip!

- Disaster!! The boat has caught fire!!

- You will be provided a string that lists many boat related items. 

- If any of these items are "Fire" you must spring into action. Change any instance of "Fire" into "~~". 

- Then return the string.

---

#### Test cases

```python
print(fire_fight("Boat Rudder Mast Boat Hull Water Fire Boat Deck Hull Fire Propeller Deck Fire Deck Boat Mast"))
print(fire_fight("Mast Deck Engine Water Fire"))
print(fire_fight("Fire Deck Engine Sail Deck Fire Fire Fire Rudder Fire Boat Fire Fire Captain"))
```

#### Output 

```
Boat Rudder Mast Boat Hull Water ~~ Boat Deck Hull ~~ Propeller Deck ~~ Deck Boat Mast
Mast Deck Engine Water ~~
~~ Deck Engine Sail Deck ~~ ~~ ~~ Rudder ~~ Boat ~~ ~~ Captain
```

---

#### Solution

```python
def fire_fight(s):
    return s.replace('Fire', '~~')
```

---

[Codewars link](https://www.codewars.com/kata/57e8fba2f11c647abc000944/)
