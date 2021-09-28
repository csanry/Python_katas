## Binary operations - 7kyu

**Instructions**

- Your work is to write a method that takes a value and an index, and returns the value with the bit at given index flipped.

- The bits are numbered from the least significant bit (index 1).

```python
flip_bit(15, 4) == 7 # 15 in binary is 1111, after flipping 4th bit, it becomes 0111, i.e. 7
flip_bit(15, 5) == 31 # 15 in binary is 1111, 5th bit is 0, after flipping, it becomes 11111, i.e., 31
```

- Index number can be out of number's range.
 
- E.g. number is 3 (it has 2 bits) and index number is 8 -> result will be 131.

---

#### Test cases

```python
print(flip_bit(0, 16))
print(flip_bit((1<<31)-1, 31))
print(flip_bit(127, 8))
```

#### Output 

```
32768
1073741823
255
```

---

#### Solution

```python
def flip_bit(value, bit_index):
    return value ^ (1 << (bit_index-1))
```

---

[Codewars link](https://www.codewars.com/kata/560e80734267381a270000a2)
