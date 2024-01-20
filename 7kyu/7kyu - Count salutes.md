## Count Salutes - 7kyu

**Instructions**

- There is a narrow hallway in which people can go right and left only.

- When two people meet in the hallway, by tradition they must salute each other.

- People move at the same speed left and right.

- Write a function that, given a string representation of people moving in the hallway, will count the number of salutes that will occur.

- Note: 2 salutes occur when people meet, one to the other and vice versa.

- People moving right will be represented by >; people moving left will be represented by <.

- An example input would be >--<--->->. The - character represents empty space.

---

#### Test cases

```python
print(count_salutes('>--->---<--<'))
print(count_salutes('<----<---<-->'))
print(count_salutes('>-<->-<'))
```

#### Output

```
8
0
6
```

---

#### Solution

```python
# more efficient
def count_salutes(hallway):
    right, salutes = 0, 0
    for p in hallway:
        if p == '>':
            right += 1
        elif p == '<':
            salutes += 2 * right
    return salutes

# one liner
def count_salutes(hallway):
    return sum(hallway[i:].count('<') for i in range(len(hallway)) if hallway[i] == '>') * 2
```

---

[Codewars link](https://www.codewars.com/kata/605ae9e1d2be8a0023b494ed)
