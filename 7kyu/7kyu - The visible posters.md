## The Visible Posters - 7kyu

**Instructions**

- The citizens of Bytetown, could not stand that the candidates in the mayoral election campaign have been placing their electoral posters at all places at their whim. 

- The city council has finally decided to build an electoral wall for placing the posters and introduce the following rules:

```
Every candidate can place exactly one poster on the wall. 
All posters are of the same height equal to the height of the wall;
the width of a poster can be any integer number of bytes
(byte is the unit of length in Bytetown). 
The wall is divided into segments and the width of each segment is one byte. 
Each poster must completely cover a contiguous number of wall segments.
```

- They have built a wall 1000 bytes long (such that there is enough place for all candidates). 

- When the electoral campaign was restarted, the candidates were placing their posters on the wall and their posters differed widely in width. 

- Moreover, the candidates started placing their posters on wall segments already occupied by other posters.

- Everyone in Bytetown was curious whose posters will be visible (entirely or in part) on the last day before elections.

- Given a 2D integer array posters. Each subarray is a 2-elements array. i.e. [1,10]. It represents a poster, 1 and 10 represent the starting position and ending position of a poster.

- Your task is to return the number of visible posters when all the posters are placed given the information about posters' size, their place and order of placement on the electoral wall.

- You can assume that the poster's pasting order is in accordance with the index order of the array.

---

#### Test cases

```python
print(count_visible([(1, 4), (2, 6), (8, 10), (3, 4), (7, 10)]))
print(count_visible([(1, 2), (3, 4), (5, 6), (7, 8), (9, 10), (1, 10)]))
print(count_visible([(1, 10), (1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]))
print(count_visible([(1, 2), (1, 3), (1, 4), (1, 6), (1, 8), (1, 10)]))
print(count_visible([(1, 3), (2, 4), (3, 5), (4, 6), (5, 7), (6, 8)]))
print(count_visible([(1, 1000), (1, 2), (3, 999)]))
```

#### Output 

```
4
1
5
1
6
3
```

---

#### Solution

```python
def count_visible(posters):
    wall = [0] * 1000
    for candidate, (start, end) in enumerate(posters, 1):
        wall[start-1:end] = [candidate] * (end-start+1)
    return len(set(wall) - {0})
```

---

[Codewars link](https://www.codewars.com/kata/5a028001ba2a14346b0000d4)
