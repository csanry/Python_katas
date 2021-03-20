## Tap Code Translation - 7kyu

**Instructions**

- Tap code is a way to communicate using a series of taps and pauses for each letter. 

- For this function, we will use dots . for the taps and whitespaces for the pauses.

- The number of taps needed for each letter matches its coordinates in the following polybius square (note the c/k position). 

- Then you "tap" the row, a pause, then the column. Each letter is separated from others with a pause too.

```
   1  2  3  4  5
1  A  B C\K D  E
2  F  G  H  I  J
3  L  M  N  O  P
4  Q  R  S  T  U
5  V  W  X  Y  Z
```

- Given a lowercase string of a single word (no whitespaces or punctuation, only letters), return the encoded string as taps and pauses.

---

#### Test cases

```python
print(tap_code_translation("breaks"))
print(tap_code_translation("taps"))
print(tap_code_translation("knocks"))
```

#### Output 

```
. .. .... .. . ..... . . . ... .... ...
.... .... . . ... ..... .... ...
. ... ... ... ... .... . ... . ... .... ...
```

---

#### Solution

```python
from itertools import product

def tap_code_translation(text):
    base = ['.', '..', '...', '....', '.....']
    v = (' '.join(c) for c in product(base, base))
    k = 'abcdefghijlmnopqrstuvwxyz'
    d = {k: v for (k, v) in zip(k, v)}
    
    return ' '.join(d.get(c, '. ...') for c in text)
```

---

[Codewars link](https://www.codewars.com/kata/605f5d33f38ca800322cb18f)
