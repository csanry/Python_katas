## Sequence classifier - 6kyu

**Instructions**

- Write a function to return a code according to the type of sequence of the input.

```
0 - unordered - [3,5,8,1,14,3]
1 - strictly increasing - [3,5,8,9,14,23]
2 - not decreasing - [3,5,8,8,14,14]
3 - strictly decreasing - [14,9,8,5,3,1]
4 - not increasing - [14,14,8,8,5,3]
5 - constant - [8,8,8,8,8,8]
```

- You can expect all the inputs to be non-empty and numerical arrays.

---

#### Test cases

```python
print(sequence_classifier([3,5,8,1,14,3]))
print(sequence_classifier([3,5,8,9,14,23]))
print(sequence_classifier([3,5,8,8,14,14]))
print(sequence_classifier([14,9,8,5,3,1]))
print(sequence_classifier([14,14,8,8,5,3]))
print(sequence_classifier([8,8,8,8,8,8]))
print(sequence_classifier([8,9]))
print(sequence_classifier([8,8,8,8,8,9]))
print(sequence_classifier([9,8]))
print(sequence_classifier([9,9,9,8,8,8]))
```

#### Output 
```
0
1
2
3
4
5
1
2
3
4
```

---

#### Solution

```python
def sequence_classifier(arr):
    if len(arr) == len(set(arr)): 
        return 1 if arr == sorted(arr) else 3 if arr == sorted(arr, reverse=True) else 0
    else: 
        return 5 if len(set(arr)) == 1 else 2 if arr == sorted(arr) else 4 if arr == sorted(arr, reverse=True) else 0
```

---

[Codewars link](https://www.codewars.com/kata/5921c0bc6b8f072e840000c0)
