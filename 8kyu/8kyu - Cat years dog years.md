## Cat years, Dog years - 8kyu

**Instructions**

- Given `human_years`, return a list of `[human_years, cat_years, dog_years]`.

- Cat years

    - 15 cat years for first year

    - +9 cat years for second year

    - +4 cat years for each year after that

- Dog Years

    - 15 dog years for first year

    - +9 dog years for second year

    - +5 dog years for each year after that

---

#### Test cases

```python
print(human_years_cat_years_dog_years(1))
print(human_years_cat_years_dog_years(2))
print(human_years_cat_years_dog_years(10))
```

#### Output 

```
[1, 15, 15]
[2, 24, 24]
[10, 56, 64]
```

---

#### Solution

```python
def human_years_cat_years_dog_years(hy):
    dog = 15 if hy == 1 else 24 if hy == 2 else (24 + 5 * (hy - 2))
    cat = 15 if hy == 1 else 24 if hy == 2 else (24 + 4 * (hy - 2))
    return [hy, cat, dog]
```

---

[Codewars link](https://www.codewars.com/kata/5a6663e9fd56cb5ab800008b)
