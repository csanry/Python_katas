## Stem-and-leaf plot - 7kyu

**Instructions**

- A stem-and-leaf plot groups data points that have the same leading digit, resembling a histogram.

- For example, for the input [11, 35, 14, 9, 39, 23, 35], it might look something like this:

```
stem | leaf
-----------
  0  | 9
  1  | 1 4
  2  | 3
  3  | 5 5 9
```

- Any single-digit number, such as 9, has 0 as its stem.

- The leaves are presented in ascending order.

- Leaves can be repeated (as with the two 5's in the last row).

- Create a function called `stem_and_leaf` that, given a list of integers `i` as input (`0 <= i <= 99`), returns a dictionary containing a stem-and-leaf plot.

- Each key of the dictionary should be a stem and each value should be a list of leaves, following the format above.

- The output from the example above should be:

```
{0: [9], 1: [1, 4], 2: [3], 3: [5, 5, 9]}
```

---

#### Test cases

```python
data = [11, 35, 14, 9, 39, 23, 35]
print(stem_and_leaf(data))
```

#### Output

```
{0: [9], 1: [1, 4], 2: [3], 3: [5, 5, 9]}
```

---

#### Solution

```python
from collections import defaultdict
def stem_and_leaf(data):
    stemleaf = defaultdict(list)
    for i in sorted(data):
        stemleaf[i // 10].append(i % 10)
    return stemleaf
```

---

[Codewars link](https://www.codewars.com/kata/5cc80fbe701f0d001136e5eb)
