## Find Missing Letter - 6kyu

**Instructions**

- Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.

- You will always get an valid array.

- And it will be always exactly one letter be missing.

- The length of the array will always be at least 2.

- The array will always contain letters in only one case.

---

#### Test cases

```python
print(find_missing_letter(['a','b','c','d','f']))
print(find_missing_letter(['O','Q','R','S']))
```

#### Output 

```
e
P
```

---

#### Solution

```python
def find_missing_letter(chars):
    curr = ord(chars[0]) + 1
    for c in chars[1:]:
        if ord(c) != curr:
            return chr(curr)
        curr += 1
```

---

[Codewars link](https://www.codewars.com/kata/5839edaa6754d6fec10000a2)
