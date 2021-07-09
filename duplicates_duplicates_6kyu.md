## Duplicates. Duplicates Everywhere. - 6kyu

**Instructions**

- You are given a table, in which every key is a number in `str` format, and corresponding values are an array of characters, e.g.

```
{
  "1": ["A", "B", "C"],
  "2": ["A", "B", "D", "A"],
}
```

- Create a function that returns a table with the same keys, but each character should appear only once among the value-arrays, e.g.

```
{
  "1": ["C"],
  "2": ["A", "B", "D"],
}
```

- Whenever two keys share the same character, they should be compared numerically, and the larger key will keep that character. 

- That's why in the example above the array under the key "2" contains "A" and "B", as 2 > 1.

- If duplicate characters are found in the same array, the first occurrence should be kept.



---

#### Test cases

```python
print(remove_duplicate_ids({
    "1": ["A"],
    "2": ["A"],
    "3": ["A"],
}))

print(remove_duplicate_ids({
    "1": ["C", "F", "G"],
    "2": ["A", "B", "C"],
    "3": ["A", "B", "D"],
}))
```

#### Output 
```
{
    "1": ["F", "G"],
    "2": ["C"],
    "3": ["A", "B", "D"]
}

{
    "1": [],
    "2": [],
    "3": ["A"]
}
```


---

#### Solution

```python
def remove_duplicate_ids(obj):
    res, seen = {}, set()
    for k, v in sorted(obj.items(), key = lambda x: -int(x[0])):
        res[k] = []
        for i in v: 
            if i not in seen: 
                seen.add(i)
                res[k].append(i)
    return res
```

---


[Codewars link](https://www.codewars.com/kata/5e8dd197c122f6001a8637ca)
