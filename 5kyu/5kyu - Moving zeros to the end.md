## Moving Zeros To The End - 5kyu

**Instructions**

- Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.


---

#### Test cases

```python
print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))
print(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))
```

#### Output

```
[1, 2, 1, 1, 3, 1, 0, 0, 0, 0]
[9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
```

---

#### Solution

```python
def move_zeros(array):
    lst = [i for i in array if i != 0]
    return lst + [0] * (len(array) - len(lst))

    # sorting alternative
    # return sorted(array, key=lambda x: x == 0)
```

---


[Codewars link](https://www.codewars.com/kata/52597aa56021e91c93000cb0)
