## CSV representation of array - 8kyu

**Instructions**

- Create a function that returns the CSV representation of a two-dimensional numeric array.

---

#### Test cases

```python
print(to_csv_text([
      [-25, 21, 2, -33, 48],
      [30, 31, -32, 33, -34]]))
```

#### Output 

```
-25,21,2,-33,48\n30,31,-32,33,-34
```

---

#### Solution

```python
def to_csv_text(array):
    return '\n'.join(','.join(map(str, subarr)) for subarr in array)
```

---

[Codewars link](https://www.codewars.com/kata/5a34af40e1ce0eb1f5000036)
