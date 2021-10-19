## Some stereometry - 7kyu

**Instructions**

- You will be given a sphere with radius `r`. 

- Imagine that sphere gets cut with flat surface, in this case the figure that is made with this cut is circle. 

- You will also be given distance `h` between centres of sphere and circle.

- Your task is to return: 

    - The area of the original sphere.
    
    - Area of circle and perimeter of circle.
    
    - All of them rounded to 3 decimal places.

---

#### Test cases

```python
print(stereometry(2, 1))
print(stereometry(3, 2))
print(stereometry(4, 3))
print(stereometry(5, 4))
print(stereometry(2.98, 1))
```

#### Output 

```
(50.265, 9.425, 10.883)
(113.097, 15.708, 14.05)
(201.062, 21.991, 16.624)
(314.159, 28.274, 18.85)
(111.594, 24.757, 17.638)
```

---

#### Solution

```python
from math import pi 
def stereometry(r, h):
    area_of_sphere = round(4 * pi * r ** 2, 3)
    area_of_circle = round(pi * (r**2 - h**2), 3)
    perimeter_of_circle = round(2 * pi * (r**2 - h**2)**0.5, 3)
    return area_of_sphere, area_of_circle, perimeter_of_circle
```

---

[Codewars link](https://www.codewars.com/kata/5970915e54c27bd71000007b)
