## Construct a bit vector set - 7kyu

**Instructions**

- Write a function which accepts a sequence of unique integers as argument and returns a 32-bit integer such that the integer, in its binary representation has 1 at only those indexes (counted from right) which are in the sequence.

```
sort_by_bit([1, 2, 0, 4]) # returns 23 as binary representation:
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 1 1 1
                                          . . . . . 5 4 3 2 1 0  <--- indices
                                                      |   | | |
                                                      |   | | |
                            these bits are 1 due to the corresponding indices in the given array
```

---

#### Test cases

```python
print(sort_by_bit([]))
print(sort_by_bit([0, 1]))
print(sort_by_bit([14, 12, 11, 24, 2, 31, 15, 18, 4]))
print(sort_by_bit([7, 23, 14, 9, 6, 20, 29, 5, 18, 13, 12, 2, 26, 27, 10, 31, 0, 25, 19, 1]))
```

#### Output

```
0
3
2164578324
2929489639
```

---

#### Solution

```python
def sort_by_bit(seq):
    return sum(2 ** i for i in seq)
```

---

[Codewars link](https://www.codewars.com/kata/52f5424d0531259cfc000d04)
