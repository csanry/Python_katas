## Are they the "same"? - 6kyu

**Instructions**

- Given two arrays a and b write a function that checks whether the two arrays have the "same" elements, with the same multiplicities (the multiplicity of a member is the number of times it appears).

- "Same" means, here, that the elements in `b` are the elements in `a` squared, regardless of the order.

---

#### Test cases

```python
a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11 * 11, 121 * 121, 144 * 144, 19 * 19, 161 * 161, 19 * 19, 144 * 144, 19 * 19]
a3 = [121, 144, 19, 161, 19, 144, 19, 11]
a4 = [11 * 21, 121 * 121, 144 * 144, 19 * 19, 161 * 161, 19 * 19, 144 * 144, 19 * 19]
a5 = [121, 144, 19, 161, 19, 144, 19, 11]
a6 = [11 * 11, 121 * 121, 144 * 144, 190 * 190, 161 * 161, 19 * 19, 144 * 144, 19 * 19]

print(comp(a1, a2))
print(comp(a3, a4))
print(comp(a5, a6))
```

#### Output

```
True
False
False
```

---

#### Solution

```python
def comp(arr1, arr2):
    if not arr1 or not arr2:
        return False
    return sorted(i ** 2 for i in arr1) == sorted(arr2)
```

---

[Codewars link](https://www.codewars.com/kata/550498447451fbbd7600041c)
