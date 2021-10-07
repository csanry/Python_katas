## Hungarian vowel harmony - 7kyu

**Instructions**

- Given a valid Hungarian word, append the correct suffix to the word based on vowel harmony rules.

- When the last vowel in the word is:

    - A front vowel (e, é, i, í, ö, ő, ü, ű) the suffix is -nek.
    
    - A back vowel (a, á, o, ó, u, ú) the suffix is -nak.
    
    - The root word otherwise.
---

#### Test cases

```python
print(dative("ablak"))
print(dative("szék"))
print(dative("otthon"))
```

#### Output 
```
ablaknak
széknek
otthonnak
```

---

#### Solution

```python
def dative(word):
    for c in word[::-1]:
        if c in 'eéiíöőüű':
            return word + 'nek'
        elif c in 'aáoóuú':
            return word + 'nak'
    return word
```

---

[Codewars link](https://www.codewars.com/kata/57fd696e26b06857eb0011e7)
