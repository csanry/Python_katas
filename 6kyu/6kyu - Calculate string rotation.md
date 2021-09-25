## Calculate String Rotation - 6kyu

**Instructions**

- Write a function that receives two strings and returns n. 

- n is equal to the number of characters we should shift the first string forward to match the second. 

- The check should be case sensitive.

- For instance, take the strings `"fatigue"` and `"tiguefa"`. In this case, the first string has been rotated 5 characters forward to produce the second string, so 5 would be returned.

- If the second string isn't a valid rotation of the first string, the method returns `-1`.

---

#### Test cases

```python
print(shifted_diff("coffee", "eecoff"))
print(shifted_diff("eecoff", "coffee"))
print(shifted_diff("moose", "Moose"))
print(shifted_diff("dog", "god"))
```

#### Output 
```
2
4
-1
-1
```

---

#### Solution

```python
def shifted_diff(first, second):
    for i in range(len(first)): 
        if first == second: 
            return i
        first = first[-1] + first[:-1]
    return -1
```

---


[Codewars link](https://www.codewars.com/kata/5596f6e9529e9ab6fb000014)
