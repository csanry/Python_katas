## A gift well spent - 7kyu

**Instructions**

- You got a gift card for your local store. It has some credit you can use to buy things, but it may be used only for up to two items, and any credit you don't use is lost. 

- You want something for a friend and yourself. Therefore, you want to buy two items which add up the entire gift card value.

- Given the value of the gift card `c` and a finite list of item values, return a pair of indices that correspond to values that add up to c.

- The indices start at 0. The first index should always be smaller than the second index. 

- If there are multiple solutions, return the minimum (lexicographically).

```
buy(5, [1,2,3,4,5]) = [0,3] # the values at [1,2] also adds up to five, but [0,3] < [1,2]
```

---

#### Test cases

```python
print(buy(2, [1, 1]))
print(buy(3, [1, 1]))
print(buy(5, [5, 2, 3, 4, 5]))
print(buy(5, [1, 2, 3, 4, 5]))
print(buy(5, [0, 0, 0, 2, 3]))
```

#### Output 

```
[0, 1]
None
[1, 2]
[0, 3]
[3, 4]
```

---

#### Solution

```python
def buy(x,arr):        
    return next(iter([i, j] for i in range(len(arr) - 1) for j in range(i + 1, len(arr)) if arr[i] + arr[j] == x), None)
```

---

[Codewars link](https://www.codewars.com/kata/54554846126a002d5b000854)
