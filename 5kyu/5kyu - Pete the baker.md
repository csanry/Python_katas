## Pete, the baker - 5kyu

**Instructions**

- Pete likes to bake some cakes. He has some recipes and ingredients.

- Help him to find out how many cakes he could bake considering his recipes.

- Write a function which takes `recipe` and the `available` ingredients and returns the maximum number of cakes Pete can bake as an integer.

- For simplicity there are no units for the amounts (e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200).

- Ingredients that are not present in the objects, can be considered as 0.

---

#### Test cases

```python
recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
print(cakes(recipe, available))

recipe_two = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
available_two = {"sugar": 500, "flour": 2000, "milk": 2000}
print(cakes(recipe_two, available_two))
```

#### Output

```
2
0
```

---

#### Solution

```python
def cakes(recipe, available):
    return min(available.get(i, 0) // a for i, a in recipe.items())
```

---

[Codewars link](https://www.codewars.com/kata/525c65e51bf619685c000059)
