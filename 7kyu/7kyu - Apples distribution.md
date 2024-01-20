## Apples distribution - 7kyu

**Instructions**

- There are some apples that you want to give out as a present.

- You are going to distribute them between some gift boxes in such a way that all the boxes will contain an equal number of apples.

- You can leave out some of the apples, but no more than `max_left`.

- You also don't want to leave out more apples than necessary; that is, if each box contains N apples, the number of left out apples should be less than N.

- Assume that you have an infinite number of gift boxes, and that all of them have the capacity of capacity.

- In how many ways can you distribute the apples satisfying all of the above conditions?

---

#### Test cases

```python
print(apples_distribution(7, 4, 1))
print(apples_distribution(10, 5, 1))
```

#### Output
```
3
4
```

---

#### Solution

```python
def apples_distribution(apples, capacity, max_left):
    cnt = 0
    for n in range(1, capacity + 1):
        if apples % n <= max_left:
            cnt += 1
    return cnt
```

---

[Codewars link](https://www.codewars.com/kata/590fca79b5f8a69285000465)
