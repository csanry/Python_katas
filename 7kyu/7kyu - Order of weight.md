## Order of weight - 7kyu

**Instructions**

- Given an array of strings, sort the array into order of weight from light to heavy.

- Weight units are grams(G), kilo-grams(KG) and tonnes(T).

- Arrays will always contain correct and positive values as well as uppercase letters.

---

#### Test cases

```python
print(arrange(["200G", "300G", "150G", "100KG"]))
print(arrange(["400G", "100T", "150KG", "100G"]))
print(arrange(["4T", "300G", "450G", "900KG"]))
print(arrange(["400T", "100T", "1T", "100G"]))
print(arrange(["1G", "2KG", "3T", "100KG"]))
print(arrange(["100KG", "100G", "150T", "150KG"]))
print(arrange(["3T", "2900000G", "2950KG"]))
print(arrange(["3T", "3000001G", "2950KG"]))
print(arrange(["1T"]))
print(arrange([]))
```

#### Output 

```
['150G', '200G', '300G', '100KG']
['100G', '400G', '150KG', '100T']
['300G', '450G', '900KG', '4T']
['100G', '1T', '100T', '400T']
['1G', '2KG', '100KG', '3T']
['100G', '100KG', '150KG', '150T']
['2900000G', '2950KG', '3T']
['2950KG', '3T', '3000001G']
['1T']
[]
```

---

#### Solution

```python
import re
def arrange(arr):
    DENOMS = {'T': '000000', 'KG': '000', 'G': ''}
    return sorted(arr, key = lambda s: int(re.sub(r'T|G|KG', lambda m: DENOMS[m.group(0)], s)))
```

---

[Codewars link](https://www.codewars.com/kata/59ff4709ba2a14501500003a/)
