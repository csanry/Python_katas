## Array Appender - 7kyu

**Instructions**

- Write a function that appends the items from sequence 2 onto sequence 1, returning the newly formed sequence. 

- Your function should also be able to handle nested sequences.

---

#### Test cases

```python
print(append_arrays([1, 2], [2, 4]))
print(append_arrays([1, 2], [3, 4]))
print(append_arrays(['this'], ['that']))
print(append_arrays(['a', 'B'], ['c', 'D']))
print(append_arrays([1, 2], [1]))
```

#### Output 

```
[1, 2, 2, 4]
[1, 2, 3, 4]
['this', 'that']
['a', 'B', 'c', 'D']
[1, 2, 1]
```

---

#### Solution

```python
def append_arrays(seq1, seq2): 
    seq1.extend(seq2)
    return seq1
```

---

[Codewars link](https://www.codewars.com/kata/53a8a476947277a3020001cc)
