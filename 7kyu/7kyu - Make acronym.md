## Make acronym - 7kyu

**Instructions**

- Implement a function called make_acronym that returns the first letters of each word in a string.

- Make sure the letters returned are uppercase.

- If the value passed in is not a string return `Not a string`.

- If the value passed in is a string which contains characters other than spaces and alphabet letters, return `Not letters`.

- If the string is empty, just return the string itself: `""`.

---

#### Test cases

```python
print(make_acronym([1, 2, 3]))
print(make_acronym('123'))
print(make_acronym('My aunt sally'))
print(make_acronym('Please excuse my dear aunt Sally'))
print(make_acronym('How much wood would a woodchuck chuck if a woodchuck could chuck wood'))
```

#### Output 

```
Not a string
Not letters
MAS
PEMDAS
HMWWAWCIAWCCW
```

---

#### Solution

```python
def make_acronym(phrase):
    if not isinstance(phrase, str):
        return 'Not a string'
    arr = phrase.split()
    return ''.join(w[0].upper() for w in arr) if all(map(str.isalpha, arr)) else 'Not letters'
```

---

[Codewars link](https://www.codewars.com/kata/557efeb04effce569d000022)
