## Hell's Kitchen - 7kyu

**Instructions**

- Given a string of four words, turn them in to Gordon language.

- Obviously the words should be caps.

- Every word should end with `!!!!`.

- Any letter `a` or `A` should become `@`.

- Any other vowel should become `*`.

---

#### Test cases

```python
print(gordon('What feck damn cake'))
print(gordon('are you stu pid'))
print(gordon('i am a chef'))
print(gordon('dont you talk tome'))
print(gordon('how dare you feck'))
```

#### Output

```
WH@T!!!! F*CK!!!! D@MN!!!! C@K*!!!!
@R*!!!! Y**!!!! ST*!!!! P*D!!!!
*!!!! @M!!!! @!!!! CH*F!!!!
D*NT!!!! Y**!!!! T@LK!!!! T*M*!!!!
H*W!!!! D@R*!!!! Y**!!!! F*CK!!!!
```

---

#### Solution

```python
import re
def gordon(a):
    st = ' '.join(w.upper().replace('A', '@') + '!!!!' for w in a.split())
    return re.sub(r'[EIOU]', '*', st)
```

---

[Codewars link](https://www.codewars.com/kata/57d1f36705c186d018000813)
