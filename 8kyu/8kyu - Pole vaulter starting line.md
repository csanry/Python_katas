## Pole Vaulter Starting Line - 8kyu

**Instructions**

- For a pole vaulter, it is very important to begin the approach run at the best possible starting mark. 

- There is a guideline that will help a beginning vaulter start at approximately the right location based on the vaulter's body height.

- You are given the following two guidelines to begin with:

    - A vaulter with a height of 1.52 meters should start at 9.45 meters on the runway.
    
    - A vaulter with a height of 1.83 meters should start at 10.67 meters on the runway.

- You will receive a vaulter's height in meters.

- The vaulter's height will always lie in a range between a minimum of 1.22 meters and a maximum of 2.13 meters.

- Return the best starting mark in meters, rounded to two decimal places.

- Assume there is a linear relationship between height of the vaulter and the start point.


---

#### Test cases

```python
starting_mark(1.75)
starting_mark(1.83)
starting_mark(1.88)
starting_mark(1.94)
starting_mark(1.98)
starting_mark(2.01)
```

#### Output 
```
10.36
10.67
10.87
11.10
11.26
11.38
```

---

#### Solution

```python
def starting_mark(height):
    m = (10.67 - 9.45) / (1.83 - 1.52)
    c = 10.67 - m * 1.83
    return round(m * height + c, 2)
```

---


[Codewars link](link here)
