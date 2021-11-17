## V A P O R C O D E - 7kyu

**Instructions**

- Write a function that converts any sentence into a `V A P O R W A V E` sentence. 

- A `V A P O R W A V E` sentence converts all the letters into uppercase, and adds 2 spaces between each letter (or special character) to create this `V A P O R W A V E` effect.

- Note that spaces should be ignored in this case.

---

#### Test cases

```python
print(vaporcode("Lets go to the movies"))
print(vaporcode("Why isn't my code working?"))
```

#### Output 

```
L  E  T  S  G  O  T  O  T  H  E  M  O  V  I  E  S
W  H  Y  I  S  N  '  T  M  Y  C  O  D  E  W  O  R  K  I  N  G  ?
```

---

#### Solution

```python
def vaporcode(s):
    return '  '.join(s.upper().replace(' ', ''))
```

---

[Codewars link](https://www.codewars.com/kata/5966eeb31b229e44eb00007a)
