## Sort the odd - 6kyu

**Instructions**

- Given an array of numbers, sort the odd numbers in ascending order while leaving the even numbers at their original positions.

---

#### Test cases

```python
print(sort_array([5, 3, 2, 8, 1, 4]))
print(sort_array([5, 3, 1, 8, 0]))
print(sort_array([]))
```

#### Output 

```
[1, 3, 2, 8, 5, 4]
[1, 3, 5, 8, 0]
[]
```

---

#### Solution

```python
# generate an iterator that consists of sorted odd numbers
# using list comprehension to replace any odd number with the sorted equivalent
def sort_array(array):
    odds = iter(sorted(x for x in array if x & 1))
    return [next(odds) if i & 1 else i for i in array]
```

---

[Codewars link](https://www.codewars.com/kata/578aa45ee9fd15ff4600090d)
