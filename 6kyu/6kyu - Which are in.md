## Which are in? - 6kyu

**Instructions**

- Given two arrays of strings a1 and a2, return a sorted array r in lexicographical order of the strings of a1 which are substrings of strings of a2.

---

#### Test cases

```python
print(in_array(['cod', 'code', 'wars', 'ewar'], ['lively', 'alive', 'harp', 'sharp', 'armstrong', 'codewars']))
print(in_array(['ohio', 'code', '1346', '1028', 'art'], ['Carolina', 'Ohio', '4600', 'NY', 'California']))
print(in_array(['duplicates', 'duplicates'], ['duplicates', 'duplicates']))
```

#### Output 
```
['cod', 'code', 'ewar', 'wars']
[]
['duplicates']
```

---

#### Solution

```python
def in_array(arr1, arr2):
    return sorted({subst for subst in arr1 if any(subst in st for st in arr2)})
```

---

[Codewars link](https://www.codewars.com/kata/550554fd08b86f84fe000a58)
