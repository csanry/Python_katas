## Over the road - 7kyu

**Instructions**

- You've just moved into a perfectly straight street with exactly `n` identical houses on either side of the road.

- Naturally, you would like to find out the house number of the people on the other side of the street.

- The street looks something like this:

```
1|   |6
3|   |4
5|   |2
```

- Evens increase on the right; odds decrease on the left. House numbers start at 1 and increase without gaps.

- Given your house number `address` and length of street `n`, give the house number on the opposite side of the street.

---

#### Test cases

```python
print(over_the_road(1, 3))
print(over_the_road(3, 3))
print(over_the_road(2, 3))
print(over_the_road(3, 5))
print(over_the_road(7, 11))
print(over_the_road(23633656673, 310027696726))
```

#### Output

```
6
4
5
8
16
596421736780
```

---

#### Solution

```python
def over_the_road(address, n):
    '''
    Thinking sequentially:
    Left side houses are [1, 3, ... 2n-3, 2n-1]
    Right side houses are [2n, 2n-2, ... 4, 2]
    Sum of opposite house numbers will always be 2n+1
    '''
    return 2 * n + 1 - address
```

---

[Codewars link](https://www.codewars.com/kata/5f0ed36164f2bc00283aed07)
