## Holiday II - Plane seating - 7kyu

**Instructions**

- Finding your seat on a plane is never fun, particularly for a long haul flight... You arrive, realise again just how little leg room you get, and sort of climb into the seat covered in a pile of your own stuff.

- To help confuse matters many airlines omit the letters 'I' and 'J' from their seat naming system.

- The naming system consists of a number (in this case between 1-60) that denotes the section of the plane where the seat is (1-20 = front, 21-40 = middle, 40+ = back).

- This number is followed by a letter, A-K with the exclusions mentioned above.

- Letters A-C denote seats on the left cluster, D-F the middle and G-K the right.

- Given a seat number, your task is to return the seat location in the following format:

- '2B' would return 'Front-Left'.

- If the number is over 60, or the letter is not valid, return 'No Seat!!'.

---

#### Test cases

```python
print(plane_seat('2B'))
print(plane_seat('20B'))
print(plane_seat('58I'))
print(plane_seat('60D'))
print(plane_seat('17K'))
```

#### Output

```
Front-Left
Front-Left
No Seat!!
Back-Middle
Front-Right
```

---

#### Solution

```python
def plane_seat(a):
    num, let = int(a[:-1]), a[-1]
    num_dict = {1 <= num <= 20: 'Front',
                21 <= num <= 40: 'Middle',
                40 < num <= 60: 'Back'}
    let_dict = {let in 'ABC': 'Left',
                let in 'DEF': 'Middle',
                let in 'GHK': 'Right'}
    try:
        return f"{num_dict[True]}-{let_dict[True]}"
    except:
        return "No Seat!!"
```

---

[Codewars link](https://www.codewars.com/kata/57e8f757085f7c7d6300009a/)
