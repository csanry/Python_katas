## Sort array by string length - 7kyu

**Instructions**

- Write a function that takes an array of strings as an argument and returns a sorted array containing the same strings, ordered from shortest to longest.

- For example, if this array were passed as an argument:

```
["Telescopes", "Glasses", "Eyes", "Monocles"]
```

- Return the following array:

```
["Eyes", "Glasses", "Monocles", "Telescopes"]
```

- All of the strings in the array passed to your function will be different lengths.

---

#### Test cases

```python
print(sort_by_length(["i", "to", "beg", "life"]))
print(sort_by_length(["", "pizza", "brains", "moderately"]))
print(sort_by_length(["short", "longer", "longest"]))
print(sort_by_length(["a", "of", "dog", "food"]))
```

#### Output
```
['i', 'to', 'beg', 'life']
['', 'pizza', 'brains', 'moderately']
['short', 'longer', 'longest']
['a', 'of', 'dog', 'food']
```

---

#### Solution

```python
def sort_by_length(arr):
    return sorted(arr, key = len)
```

---

[Codewars link](https://www.codewars.com/kata/57ea5b0b75ae11d1e800006c)
