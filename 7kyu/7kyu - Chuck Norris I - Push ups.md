## Chuck Norris I - Push ups - 7kyu

**Instructions**

- Today, Chuck got home from work 10 minutes earlier than his wife.

- Naturally he decided to bang out some push ups. He counts them in binary, because he thinks coding is cool.

- When his wife arrives home, she starts talking to Chuck, spoiling his count!

- Your job is to write a function to isolate Chuck's count, and then work out how many push ups he has done!

- Return your answer as a number.

- Careful Chuck doesn't lose count!

- Even if he does, always return the highest number he counted to!

- If Chuck's wife has left a list of jobs for him he won't be able to do any push ups... if there is no sign of a count, simply return `CHUCK SMASH!!`

- In the event someone dares to provide Chuck with something other than a string, return `FAIL!!`

- Your code should still pass in the case that the binary is mixed up with other characters - maybe Chuck has a cough... e.g.: `1ee1gf00t10h1011tr00` --> `110010101100` --> 3244.

---

#### Test cases

```python
print(chuck_push_ups('1 "Chuck" 10 "Stop that!" 11 "Your vest looks stupid" 100 101 110'))
print(chuck_push_ups('1000 "Did you kick someone in the face today?" 1001 1010 "Will I be making dinner then?!" 1011 110'))
print(chuck_push_ups('10000 "Nice Beard" 1111 "Are you wearing denim shorts?" 1110 1101'))
print(chuck_push_ups(''))
print(chuck_push_ups([]))
print(chuck_push_ups(1))
print(chuck_push_ups('"How was your day Chuck?"'))
```

#### Output

```
6
11
16
FAIL!!
FAIL!!
FAIL!!
CHUCK SMASH!!
```

---

#### Solution

```python
import re

def chuck_push_ups(st):
    if not isinstance(st, str) or not st or st is []:
        return 'FAIL!!'
    lst = [re.sub(r'[\D23456789]', '', st) for st in re.findall(r'\S+[01]\S+', st)]
    return max(map(lambda x: int(x, 2), lst), default='CHUCK SMASH!!')
```

---

[Codewars link](https://www.codewars.com/kata/570564e838428f2eca001d73/)
