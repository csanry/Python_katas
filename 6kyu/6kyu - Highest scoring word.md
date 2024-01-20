## Highest Scoring Word - 6kyu

**Instructions**

- Given a string of words, you need to find the highest scoring word.

- Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

- You need to return the highest scoring word as a string.

- If two words score the same, return the word that appears earliest in the original string.

- All letters will be lowercase and all inputs will be valid.

---

#### Test cases

```python
print(high('man i need a taxi up to ubud'))
print(high('what time are we climbing up the volcano'))
print(high('take me to semynak'))
```

#### Output
```
taxi
volcano
semynak
```

---

#### Solution

```python
def high(x):
    words = x.split()
    n = [sum(ord(c) - 96 for c in w) for w in words]
    return words[n.index(max(n))]

# one-liner
def high(x):
    return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))
```

---


[Codewars link](https://www.codewars.com/kata/57eb8fcdf670e99d9b000272)
