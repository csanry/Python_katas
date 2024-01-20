## Planting Trees - 7kyu

**Instructions**

- There is a rectangular land and we need to plant trees on the edges of that land.

- Given three parameters:

    - `width` and `length`, two integers > 1 that represents the land's width and length.

    - `gaps`, an integer >= 0, that is the distance between two trees.

- Return how many trees have to be planted, if you can't achieve a symmetrical layout then return `0`.

```
Example1:
width=3, length=3, gaps=1       o - o
we can plant 4 trees            -   -
sc(3,3,1)=4                     o - o

Example2:
width=3, length=3, gaps=3       o - -
we can plant 2 trees            -   -
sc(3,3,3)=2                     - - o

Example3:
width=3, length=3, gaps=2       o - -
if we plant 2 trees, some       x   o
gaps of two trees will >2       x x x
```

---

#### Test cases

```python
print(sc(3,3,1))
print(sc(3,3,3))
print(sc(3,3,2))
print(sc(7,7,3))
print(sc(3,3,0))
print(sc(3,3,10))
print(sc(2,2,1))
print(sc(2,2,0))
print(sc(200,2,1))
print(sc(2,200,1))
```

#### Output

```
4
2
0
6
8
0
2
4
200
200
```

---

#### Solution

```python
def sc(width, length, gaps):
    div, mod = divmod(2 * (width + length -2), gaps + 1)
    return 0 if mod else div
```

---

[Codewars link](https://www.codewars.com/kata/5710443187a36a9cee0005a1)
