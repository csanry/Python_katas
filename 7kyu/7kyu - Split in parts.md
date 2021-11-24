## Split in Parts - 7kyu

**Instructions**

- Split a given string into different strings of equal size (note size of strings is passed to the method).

---

#### Test cases

```python
print(split_in_parts("supercalifragilisticexpialidocious", 3))
print(split_in_parts("HelloKata", 1))
print(split_in_parts("HelloKata", 9))
```

#### Output 

```
sup erc ali fra gil ist ice xpi ali doc iou s
H e l l o K a t a
HelloKata
```

---

#### Solution

```python
def split_in_parts(s, pl): 
    return ' '.join(s[i:i+pl] for i in range(0, len(s), pl))
```

---

[Codewars link](https://www.codewars.com/kata/5650ab06d11d675371000003)
