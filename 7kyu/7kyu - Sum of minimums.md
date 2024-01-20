## Sum of Minimums! - 7kyu

**Instructions**

- Given a 2D list of size `m * n`, find the sum of minimum value in each row.

**Example**

```
[
  [1, 2, 3, 4, 5],       # minimum value of row is 1
  [5, 6, 7, 8, 9],       # minimum value of row is 5
  [20, 21, 34, 56, 100]  # minimum value of row is 20
]
```

- So, the function should return `26` because sum of minimums is as `1 + 5 + 20 = 26`.

- You will be always given non-empty list containing positive values.

---

#### Test cases

```python
print(sum_of_minimums([[7, 9, 8, 6, 2], [6, 3, 5, 4, 3], [5, 8, 7, 4, 5]]))
print(sum_of_minimums([[11, 12, 14, 54], [67, 89, 90, 56], [7, 9, 4, 3], [9, 8, 6, 7]]))
```

#### Output

```
9
76
```

---

#### Solution

```python
def sum_of_minimums(numbers):
    return sum(map(min, numbers))
```

---

[Codewars link](https://www.codewars.com/kata/5d5ee4c35162d9001af7d699)
