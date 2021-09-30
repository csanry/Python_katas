## Count of positives / sum of negatives - 7kyu

**Instructions**

- Given an array, return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers.

- Return an empty array if the input array is empty or null.

---

#### Test cases

```python
print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))
print(count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]))
print(count_positives_sum_negatives([1]))
print(count_positives_sum_negatives([-1]))
print(count_positives_sum_negatives([0,0,0,0,0,0,0,0,0]))
print(count_positives_sum_negatives([]))
```

#### Output 
```
[10, -65]
[8, -50]
[1, 0]
[0, -1]
[0, 0]
[]
```

---

#### Solution

```python
def count_positives_sum_negatives(arr):
    return [sum(x > 0 for x in arr), sum(x for x in arr if x < 0)] if arr else []
```

---

[Codewars link](https://www.codewars.com/kata/576bb71bbbcf0951d5000044)
