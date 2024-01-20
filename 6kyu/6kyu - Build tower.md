## Build tower - 6kyu

**Instructions**

- Build a tower by the following given argument:
    - `n_floors`(integer and always greater than 0).

- Tower block is represented as `*`

- Example of 3 story tower:

```
[  '  *  ',
   ' *** ',
   '*****'  ]
```

---

#### Test cases

```python
print(tower_builder(1))
print(tower_builder(2))
print(tower_builder(3))
print(tower_builder(5))
print(tower_builder(8))
```

#### Output
```
['*']
[' * ', '***']
['  *  ', ' *** ', '*****']
['    *    ', '   ***   ', '  *****  ', ' ******* ', '*********']
['       *       ', '      ***      ', '     *****     ', '    *******    ', '   *********   ', '  ***********  ', ' ************* ', '***************']
```

---

#### Solution

```python
def tower_builder(n_floors):
    res = []
    for i in range(1, n_floors + 1):
        stars = '*' * (2 * i - 1)
        space = ' ' * (n_floors - i)
        res.append(space + stars + space)
    return res
```

---

[Codewars link](https://www.codewars.com/kata/576757b1df89ecf5bd00073b)
