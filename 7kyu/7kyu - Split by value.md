## Split By Value - 7kyu

**Instructions**

- For an integer `k` rearrange all the elements of the given array in such way, that:

    - All elements that are less than `k` are placed before elements that are not less than `k`.

    - All elements that are less than `k` remain in the same order with respect to each other.

    - All elements that are not less than `k` remain in the same order with respect to each other.

- For `k = 6` and `elements = [6, 4, 10, 10, 6]`, the output should be `split_by_value(k, elements) = [4, 6, 10, 10, 6]`.

- For `k = 5` and `elements = [1, 3, 5, 7, 6, 4, 2]`, the output should be `split_by_value(k, elements) = [1, 3, 4, 2, 5, 7, 6]`.

---

#### Test cases

```python
print(split_by_value(5, [1, 3, 5, 7, 6, 4, 2]))
print(split_by_value(0, [5, 2, 7, 3, 2]))
print(split_by_value(6, [6, 4, 10, 10, 6]))
```

#### Output

```
[1, 3, 4, 2, 5, 7, 6]
[5, 2, 7, 3, 2]
[4, 6, 10, 10, 6]
```

---

#### Solution

```python
def split_by_value(k, elements):
    return sorted(elements, key=lambda x: x >= k)
```

---

[Codewars link](https://www.codewars.com/kata/5a433c7a8f27f23bb00000dc)
