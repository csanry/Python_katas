## Mispelled word - 7kyu

**Instructions**

- Create a function `mispelled(word1, word2)`:

```python
mispelled('versed', 'xersed') # returns True
mispelled('versed', 'applb') # returns False
mispelled('versed', 'v5rsed') # returns True
mispelled('1versed', 'versed') # returns True
```

- It checks if `word2` differs from `word1` by only one character.

- This can include an extra char at the end or the beginning of either of words.

- In the tests that expect true, the mispelled word will always differ only by one character.

---

#### Test cases

```python
print(mispelled('versed','xersed'))
print(mispelled('versed','applb'))
print(mispelled('versed','v5rsed'))
print(mispelled('1versed','versed'))
print(mispelled('versed','versed'))
```

#### Output 

```
True
False
True
True
True
```

---

#### Solution

```python
import difflib
def mispelled(word1, word2):
    return len([i for i in difflib.ndiff(word1, word2) if i[0] != ' ']) <= 2
```

---

[Codewars link](https://www.codewars.com/kata/5892595f190ca40ad0000095)
