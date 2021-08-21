## The Office IV - 7kyu

**Instructions**

- Your job at your company is both boring and difficult.

- It isn't made any easier by the fact that everyone wants a meeting with you, and that the meeting rooms are always taken!

- In this kata, you will be given an array. Each value represents a meeting room.

- Find the first empty one and return its index (N.B. There may be more than one empty room in some test cases).

- If all rooms are busy, return `"None available!"`

---

#### Test cases

```Python
meeting(['X', 'O', 'X', 'O'])
meeting(['X', 'X', 'X', 'X'])
```

#### Output 
```
1
None available!
```

---

#### Solution

```python
def meeting(rooms):
    for i in range(len(rooms)):
        if rooms[i] == 'O':
            return i
    return "None available!"
```

---


[Codewars link](https://www.codewars.com/kata/the-office-iv-find-a-meeting-room)
