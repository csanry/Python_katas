## Grandma learning to text - 7kyu

**Instructions**

- Write a function that replaces 'two', 'too' and 'to' with the number '2'.

- Even if the sound is found mid word (like in octopus) or not in lowercase grandma still thinks that should be replaced with a 2.

- Note that 'too' should become '2', not '2o'.

---

#### Test cases

```python
print(textin('I love to text'))
print(textin('see you tomorrow'))
print(textin('look at that octopus'))
print(textin('BECAUSE I WANT TO'))
print(textin('TwO ToO tWo tOo'))
```

#### Output

```
I love 2 text
see you 2morrow
look at that oc2pus
BECAUSE I WANT 2
2 2 2 2
```

---

#### Solution

```python
import re

def textin(s):
    return re.sub(r'(two|too|to)', '2', s, flags=re.I)
```

---

[Codewars link](https://www.codewars.com/kata/5a043fbef3251a5a2b0002b0)
