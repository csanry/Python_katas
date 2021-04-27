## Sum of parts - 6kyu

**Instructions**

- Given an array:

```python
# eg
ls = [0, 1, 3, 6, 10]
```

- It's corresponding parts are: 

```python
ls = [0, 1, 3, 6, 10]
ls = [1, 3, 6, 10]
ls = [3, 6, 10]
ls = [6, 10]
ls = [10]
ls = []
```

- Return the corresponding sums in a list:

```python
[20, 20, 19, 16, 10, 0]
```

---

#### Test cases

```python
print(part_sums([]))
print(part_sums([0, 1, 3, 6, 10]))
print(part_sums([1, 2, 3, 4, 5, 6]))
print(part_sums([744125, 935, 407, 454, 430, 90, 144, 6710213, 889, 810, 2579358]))
```

#### Output 
```
[0]
[20, 20, 19, 16, 10, 0]
[21, 20, 18, 15, 11, 6, 0]
[10037855, 9293730, 9292795, 9292388, 9291934, 9291504, 9291414, 9291270, 2581057, 2580168, 2579358, 0]
```

---

#### Solution

```python
def part_sums(lst):
    from itertools import accumulate
    return [*accumulate(lst[::-1])][::-1] + [0]
```

---

[Codewars link](https://www.codewars.com/kata/5ce399e0047a45001c853c2b)
