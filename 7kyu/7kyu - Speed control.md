## Speed control - 7kyu

**Instructions**

- In John's car the GPS records every `s` seconds the distance travelled from an origin (distances are measured in an arbitrary but consistent unit). 

- For example, below is part of a record with `s = 15`:

```
x = [0.0, 0.19, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25]
```

- The sections are:

```
0.0-0.19, 0.19-0.5, 0.5-0.75, 0.75-1.0, 1.0-1.25, 1.25-1.50, 1.5-1.75, 1.75-2.0, 2.0-2.25
```

- We can calculate John's average hourly speed on every section and we get:

```
[45.6, 74.4, 60.0, 60.0, 60.0, 60.0, 60.0, 60.0, 60.0]
```

- Given `s` and `x` the task is to return as an integer the floor of the maximum average speed per hour obtained on the sections of `x`. 

- If `x` length is less than or equal to 1 return `0` since the car didn't move.

---

#### Test cases

```python
print(gps(20, [0.0, 0.23, 0.46, 0.69, 0.92, 1.15, 1.38, 1.61]))
print(gps(12, [0.0, 0.11, 0.22, 0.33, 0.44, 0.65, 1.08, 1.26, 1.68, 1.89, 2.1, 2.31, 2.52, 3.25]))
print(gps(20, [0.0, 0.18, 0.36, 0.54, 0.72, 1.05, 1.26, 1.47, 1.92, 2.16, 2.4, 2.64, 2.88, 3.12, 3.36, 3.6, 3.84]))
```

#### Output 

```
41
219
80
```

---

#### Solution

```python
from math import floor  
def gps(s, x):
    return floor(3600 * max((j - i for i, j in zip(x, x[1:])), default=0) / s)
```

---

[Codewars link](https://www.codewars.com/kata/56484848ba95170a8000004d)
