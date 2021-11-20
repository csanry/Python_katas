## Chuck Norris II - One punch - 7kyu

**Instructions**

- Your task, to please Chuck, is to create a function that chains 4 methods on a SINGLE LINE! You can pass with multiple lines, but CHuck will pity you. 

- Chuck expects his list of favourite items to be split, sorted, joined AND have any occurrences of the letters 'e' and 'a' removed - why, you ask? Well Nunchucks hasn't got the letters 'a' or 'e' in it has it?? Chuck says shut your mouth... and don't forget the capitals.

- If anyone dares to provide Chuck with an empty string, an integer or an array, just return a description of their face once Chuck finds out: 'Broken!'

---

#### Test cases

```python
print(one_punch('Beard Knife Grenade Motorbike Hat'))
print(one_punch('Horse Rope Cups Car Beard'))
print(one_punch('Friend Beer Beard Monkey Laptop'))
```

#### Output 

```
Brd Grnd Ht Knif Motorbik
Brd Cr Cups Hors Rop
Brd Br Frind Lptop Monky
```

---

#### Solution

```python
import re
def one_punch(item): 
    return ' '.join(re.sub(r'[AEae]', '', w) for w in sorted(item.split())) if isinstance(item, str) and item else 'Broken!'
```

---

[Codewars link](https://www.codewars.com/kata/57057a035eef1f7e790009ef)
