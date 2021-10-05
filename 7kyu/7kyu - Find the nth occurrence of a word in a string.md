## Find the nth occurrence of a word in a string! - 7kyu

**Instructions**

- Implement a function `find_nth_occurrence` that returns the index of the nth occurrence of a substring within a string. 

- Considering that those substring could overlap each others. 

- If there are less than n occurrences of the substring, return -1.

```python
string = "This is an example. Return the nth occurrence of example in this example string."
find_nth_occurrence("example", string, 1) == 11
find_nth_occurrence("example", string, 2) == 49
find_nth_occurrence("example", string, 3) == 65
find_nth_occurrence("example", string, 4) == -1
```

---

#### Test cases

```python
string = "This is an example. Return the nth occurrence of example in this example string."
print(find_nth_occurrence("example", string, 1))
print(find_nth_occurrence("example", string, 2))
print(find_nth_occurrence("example", string, 3))
print(find_nth_occurrence("example", string, 4))
```

#### Output 

```
11
49
65
-1
```

---

#### Solution

```python
def find_nth_occurrence(substring, string, occurrence=1):
    idx = -1
    for _ in range(occurrence): 
        idx = string.find(substring, idx+1)
    return idx
```

---

[Codewars link](https://www.codewars.com/kata/5b1d1812b6989d61bd00004f)
