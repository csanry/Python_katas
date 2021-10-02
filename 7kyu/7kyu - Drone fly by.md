## Drone fly-by - 7kyu

**Instructions**

- You will be given two strings: `lamps` and `drone`. 

- Lamps represents a row of lamps, currently off, each represented by `x`. 

- When these lamps are on, they should be represented by `o`.

- The `drone` string represents the position of the drone `T` and its flight path up until this point =. 

- The drone always flies left to right, and always begins at the start of the row of `lamps`. 

- Anywhere the drone has flown, including its current position, will result in the lamp at that position switching on.

- Return the resulting `lamps` string.

---

#### Test cases

```python
print(fly_by('xxxxxx', '====T'))
print(fly_by('xxxxxxxxx', '==T'))
print(fly_by('xxxxxxxxxxxxxxx', '=========T'))
```

#### Output 

```
ooooox
oooxxxxxx
ooooooooooxxxxx
```

---

#### Solution

```python
def fly_by(lamps, drone):
    return lamps.replace('x', 'o', len(drone))
```

---

[Codewars link](https://www.codewars.com/kata/58356a94f8358058f30004b5/train/python)
