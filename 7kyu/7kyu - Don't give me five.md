## Don't give me five! - 7kyu

**Instructions**

- Given the start number and the end number of a region, return the count of all numbers except numbers with a 5 in it.

- The start and the end number are both inclusive.

- The start number will always be smaller than the end number. Both numbers can be negative.

---

#### Test cases

```python
print(dont_give_me_five(1, 9))
print(dont_give_me_five(4, 17))
print(dont_give_me_five(50, 59))
print(dont_give_me_five(-10, 10))
print(dont_give_me_five(-50, -5))
```

#### Output

```
8
12
0
19
40
```

---

#### Solution

```python
def dont_give_me_five(start, end):
    return sum('5' not in str(i) for i in range(start, end + 1))
```

---

[Codewars link](https://www.codewars.com/kata/5813d19765d81c592200001a)
