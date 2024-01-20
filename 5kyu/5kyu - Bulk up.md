## Bulk up! - 5kyu

**Instructions**

- Given an array of meals where each element is a string in the form `300g turkey, 300g potatoes, 100g cucumber` find out how many proteins and calories you consumed.

- You like to keep things simple so all values will be expressed in grams.

- Every gram of protein and carbohydrate has 4 calories, while 1 gram of fat provides 9 calories.

- An object `food` is preloaded for you that contains the information about the given food per 100 grams.

- Round your results to 2 decimal places and return a string in the form `Total proteins: n grams, Total calories: n`.

- Delete all trailing zeros on every float and remove trailing point if the result is an integer.

---

#### Test cases

```python
a = ["175g pork, 100g eggs, 25g chocolate", "175g goose, 200g cheddar, 250g milk, 300g kiwi", "100g catfish, 125g parmesan, 75g chocolate, 125g watermelon", "125g chicken, 25g beans, 50g lemons"]
b = ["150g elk, 325g tofu, 150g watermelon", "75g pork, 50g mushrooms, 75g kiwi", "275g rabbit, 325g broccoli, 100g cherries", "225g duck, 200g potatoes, 175g parmesan, 25g wine", "225g rabbit, 125g broccoli"]
c = ["350g goose, 75g mozzarella", "325g beef, 175g tofu, 75g juice", "125g goose, 350g rice", "175g beef, 50g mushrooms", "325g pork, 50g mushrooms", "325g rabbit, 175g cheddar"]
d = ["325g duck, 175g potatoes, 325g bananas", "75g elk, 225g rice", "100g chicken, 50g broccoli", "300g turkey, 325g corn, 175g milk, 50g wine", "150g bass, 75g tomatoes, 275g wine", "200g buffalo, 150g potatoes"]

print(bulk([]))
print(bulk(["200g pork"]))
print(bulk(a))
print(bulk(b))
print(bulk(c))
print(bulk(d))
```

#### Output

```
Total proteins: 0 grams, Total calories: 0
Total proteins: 40 grams, Total calories: 358
Total proteins: 242.75 grams, Total calories: 3079.5
Total proteins: 354.25 grams, Total calories: 2972.5
Total proteins: 505.25 grams, Total calories: 4888
Total proteins: 327.5 grams, Total calories: 2959
```

---

#### Solution

```python
food = {'beef': [26, 0, 18], 'buffalo': [27, 0, 2], 'elk': [30, 0, 2], 'lamb': [23, 0, 19], 'pork': [20, 0, 11], 'rabbit': [29, 0, 8],
        'chicken': [24, 0, 5], 'duck': [23, 0, 9], 'goose': [28, 0, 10], 'turkey': [26, 0, 2], 'bass': [24, 0, 5], 'catfish': [18, 0, 3],
        'crab': [19, 0, 2], 'lobster': [21, 1, 1], 'salmon': [27, 0, 10], 'beans': [8, 25, 0], 'tofu': [7, 3, 3], 'cheddar': [21, 0, 28],
        'eggs': [10, 2, 10], 'mozzarella': [18, 3, 18], 'parmesan': [30, 4, 22], 'beer': [0, 5, 0], 'wine': [0, 3, 0], 'juice': [0, 10, 0],
        'milk': [3, 4, 2], 'cabbage': [1, 6, 0], 'broccoli': [3, 7, 0], 'corn': [3, 20, 1], 'mushrooms': [3, 3, 0], 'tomatoes': [1, 3, 0],
        'potatoes': [2, 16, 0], 'olives': [1, 6, 11], 'cucumber': [1, 4, 0], 'apples': [0, 14, 0], 'bananas': [1, 23, 0], 'blackberries': [1, 10, 0],
        'cherries': [1, 12, 0], 'lemons': [1, 9, 0], 'kiwi': [1, 15, 1], 'watermelon': [1, 8, 0], 'oat': [12, 50, 5], 'quinoa': [14, 60, 5],
        'rice': [5, 28, 0], 'chocolate': [7, 45, 30], 'mayonnaise': [0, 0, 12]}

def bulk(arr):
    protein, calories = 0, 0
    if arr:
        for i in range(len(arr)):
            items = arr[i].split(',')
            for i in range(len(items)):
                weight, type = items[i].split('g ')
                unit = int(weight) / 100
                pro = food[type][0] * unit
                car = food[type][1] * unit
                fat = food[type][2] * unit
                protein += pro
                calories += 4 * (pro + car) + 9 * fat
            if protein % 1 == 0:
                protein = int(protein)
            if calories % 1 == 0:
                calories = int(calories)
    return f'Total proteins: {protein} grams, Total calories: {calories}'
```

---

[Codewars link](https://www.codewars.com/kata/5863f1c8b359c4dd4e000001)
