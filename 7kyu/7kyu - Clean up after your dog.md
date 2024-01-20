## Clean up after your dog - 7kyu

**Instructions**

- You have stumbled across the divine pleasure that is owning a dog and a garden. Now time to pick up all the cr@p!

- Given a 2D array to represent your garden, you must find and collect all of the dog cr@p - represented by `@`.

- You will also be given the number of bags you have access to `bags`, and the capacity of a bag `cap`. If there are no bags then you can't pick anything up, so you can ignore `cap`.

- You need to find out if you have enough capacity to collect all the cr@p and make your garden clean again.

- If you do, return `Clean`, else return `Cr@p`.

- Watch out though - if your dog is out there `D`, he gets very touchy about being watched. If he is there you need to return `Dog!!`.

---

#### Test cases

```python
print(crap([['_', '_', '_', '_'], ['_', '_', '_', '@'], ['_', '_', '@', '_']], 2, 2))
print(crap([['_', '_', '_', '_'], ['_', '_', '_', '@'], ['_', '_', '@', '_']], 1, 1))
print(crap([['_', '_'], ['_', '@'], ['D', '_']], 2, 2))
print(crap([['_', '_', '_', '_'], ['_', '_', '_', '_'], ['_', '_', '_', '_']], 2, 2))
print(crap([['@', '@'], ['@', '@'], ['@', '@']], 3, 2))
```

#### Output

```
Clean
Cr@p
Dog!!
Clean
Clean
```

---

#### Solution

```python
def crap(garden, bags, cap):
    st = ''.join(ele for subarr in garden for ele in subarr)
    return 'Dog!!' if 'D' in st else 'Clean' if cap * bags >= st.count('@') else 'Cr@p'
```

---

[Codewars link](https://www.codewars.com/kata/57faa6ff9610ce181b000028)
