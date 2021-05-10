## n-back - 6kyu

**Instructions**

- Implement a function that counts the number of "targets" in a sequence of digits.

- Targets are stimuli that match the one from n steps earlier. 

- Your function will take 2 parameters:
    
    - `n`, a positive integer equal to the number of steps to look back to find a match.
    
    - `sequence` a sequence of digits contain 0 or more targets.

---

#### Test cases

```python
print(count_targets(1, [1, 1, 1, 1, 1]))
print(count_targets(2, [1, 1, 1, 1, 1]))
print(count_targets(1, [1, 2, 1, 2, 1]))
print(count_targets(2, [1, 2, 1, 2, 1]))
print(count_targets(9, [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]))
```

#### Output 
```
4
3
0
3
1
```

---

#### Solution

```python
def count_targets(n, sequence):
    return sum(sequence[i] == sequence[i-n] for i in range(n, len(sequence)))
```

---

[Codewars link](https://www.codewars.com/kata/599c7f81ca4fa35314000140)
