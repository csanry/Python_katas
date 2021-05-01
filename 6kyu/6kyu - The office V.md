## The Office V - 6kyu

**Instructions**

- You need chairs for your meeting - specified by `need`

- Find the spare chairs from the array of meeting `rooms`.

- Each meeting room object will have the number of occupants as a string.

- Each occupant is represented by 'X'.
- The room object will also have an integer telling you how many chairs there are in the room.
- Return an array of integers that shows how many chairs you take from each room in order.
- Only take up to the required amount.

- If you need no chairs: return `"Game On!"`
- If there are insufficient chairs, return `"Not Enough!"`

---

#### Test case

```Python
meeting([["XXX", 3], ["XXXXX", 6], ["XXXXXX", 9], ["XXX", 2]], 4)
```

#### Output 
```python
[0, 1, 3]
```

No chairs free in room 0, take `1` from room 1, take `3` from room 2. No need to consider room 3 as you have your 4 chairs already.

---

#### Solution

```python
def meeting(rooms, need):
    if need == 0:
        return "Game On!"

    result = []
    for people, chairs in rooms:
        taken = min(max(chairs-len(people), 0), need)
        result.append(taken)
        need -= taken
        if need == 0:
            return result
    return "Not Enough!"
```

---


[Codewars link](https://www.codewars.com/kata/the-office-v-find-a-chair)
