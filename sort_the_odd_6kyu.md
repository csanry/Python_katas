## Sort the Odd - 6kyu

**Instructions**

Given an array of numbers, sort the odd numbers in ascending order while leaving the even numbers
at their original positions.

---

#### Test cases

```python
sort_array([7, 1])
sort_array([5, 3, 2, 8, 1, 4])
sort_array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
```

#### Output 
```
[1, 7]
[1, 3, 2, 8, 5, 4]
[1, 8, 3, 6, 5, 4, 7, 2, 9, 0]
```

---

#### Solution

```python
def sort_array(input_arr):
    odds = sorted(x for x in input_arr if x & 1)
    return [odds.pop(0) if n & 1 else n for n in input_arr]
```

---

[Codewars link](https://www.codewars.com/kata/578aa45ee9fd15ff4600090d)
