## Jumping Dutch act - 7kyu

**Instructions**

- 90 character code limit.

- Mr. despair wants to jump off Dutch act, So he came to the top of a building.

- If he jumps from a floor more than 6, he will die in an instant.

- When the floor is less than or equal to 6, he will not immediately die, he would scream first.

- Input: floor, The height of the building.

- Output: a string, The voice of despair (When jumping Dutch act)

- `sc(2)` should return `Aa~ Pa! Aa!`

```
Mr. despair jumped from the 2 floor, the voice is "Aa~"
He fell on the ground, the voice is "Pa!"
He did not die immediately, and the final voice was "Aa!"
```

- `sc(6)` should return `Aa~ Aa~ Aa~ Aa~ Aa~ Pa! Aa!`

- `sc(7)` should return `Aa~ Aa~ Aa~ Aa~ Aa~ Aa~ Pa!`

- `sc(10)` should return `Aa~ Aa~ Aa~ Aa~ Aa~ Aa~ Aa~ Aa~ Aa~ Pa!`

- If floor<=1, Mr. despair is safe, return `""`

---

#### Test cases

```python
print(sc(2))
print(sc(6))
print(sc(7))
print(sc(10))
print(sc(1))
print(sc(-1))
```

#### Output 

```
Aa~ Pa! Aa!
Aa~ Aa~ Aa~ Aa~ Aa~ Pa! Aa!
Aa~ Aa~ Aa~ Aa~ Aa~ Aa~ Pa!
Aa~ Aa~ Aa~ Aa~ Aa~ Aa~ Aa~ Aa~ Aa~ Pa!
""
""
""
```

---

#### Solution

```python
def sc(n): 
    return 'Aa~ ' * (n-1) + ('', 'Pa!')[n>1] + ('', ' Aa!')[1<n<7]
```

---

[Codewars link](https://www.codewars.com/kata/570bbf7b6731d44b36001fde)
