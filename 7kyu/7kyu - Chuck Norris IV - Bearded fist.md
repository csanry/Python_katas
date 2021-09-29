## Chuck Norris IV - Bearded Fist - 7kyu

**Instructions**

- When shaving, Chuck accidentally punched himself in the face. 

- Chuck can't remember a thing - he needs your help!!

- Hidden within the provided sequence of sequences are numbers that represent the letters of the words for some of Chuck's favourite things! 

- Your job is to translate them, and return the words so that Chuck can get back to the business of punching and kicking things.

---

#### Test cases

```python
print(fist_beard([[78], [117, 110, 99], [104, 117], [107, 115]]))
print(fist_beard([[70, 97, 99], [101, 45, 75, 105, 99, 107]]))
```

#### Output 

```
Nunchuks
Face-Kick
```

---

#### Solution

```python
from itertools import chain
def fist_beard(arr): 
    return ''.join(map(chr, chain.from_iterable(arr)))
```

---

[Codewars link](https://www.codewars.com/kata/57066708cb7293901a0013a1)
