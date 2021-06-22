## The Office I - 7kyu

**Instructions**

- In a team meeting, a terrible person declares to the group that you aren't working. 

- You quickly have to gauge the feeling in the room to decide whether or not you should gather your things and leave.

- Given a dictionary `meet` containing team member names as keys, and their happiness rating out of 10 as the value:

- Assess the overall happiness rating of the group. If <= 5, return `"Get Out Now!"`. Else return `"Nice Work Champ!".`

- Happiness rating will be total score / number of people in the room.

- Note that your boss is in the room (boss), their score is worth double it's face value

---

#### Test case

```Python
outed({'tim':0, 'jim':2, 'randy':0, 'sandy':7, 'andy':0, 'katie':5,
       'laura':1, 'saajid':2, 'alex':3, 'john':2, 'mr':0}, 'laura')
```

#### Output 
```
Get Out Now!
```

---

#### Solution

```python
def outed(meet, boss):
    happiness = (sum(meet.values()) + meet[boss]) / len(meet)
    return 'Get Out Now!' if happiness <= 5 else 'Nice Work Champ!'
```

---


[Codewars link](https://www.codewars.com/kata/57ecf6efc7fe13eb070000e1)
