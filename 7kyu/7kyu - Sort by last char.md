## Sort by last char - 7kyu

**Instructions**

- Given a string of words (x), you need to return an array of the words, sorted alphabetically by the final character in each.

- If two words have the same last letter, the returned array should show them in the order they appeared in the given string.

---

#### Test cases

```python
print(last("man i need a taxi up to ubud"))
print(last("what time are we climbing up the volcano"))
print(last("take me to semynak"))
print(last("massage yes massage yes massage"))
print(last("take bintang and a dance please"))
```

#### Output

```
['a', 'need', 'ubud', 'i', 'taxi', 'man', 'to', 'up']
['time', 'are', 'we', 'the', 'climbing', 'volcano', 'up', 'what']
['take', 'me', 'semynak', 'to']
['massage', 'massage', 'massage', 'yes', 'yes']
['a', 'and', 'take', 'dance', 'please', 'bintang']
```

---

#### Solution

```python
def last(s):
    return sorted(s.split(), key=lambda x: x[-1])
```

---

[Codewars link](https://www.codewars.com/kata/57eba158e8ca2c8aba0002a0)
