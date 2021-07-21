## Find the vowels - 7kyu

**Instructions**

- We want to know the index of the vowels in a given word, for example, there are two vowels in the word super (the second and fourth letters).

- Eg. given a string "super", we should return a list of [2, 4].

- Vowels in this context refers to: `a e i o u y` (including upper case)

- This is indexed from `[1..n]` (not zero indexed!)
---

#### Test cases

```python
print(vowel_indices('SUPERapple'))
print(vowel_indices('iutnms0wuQ'))
print(vowel_indices('YmvM3oxbpK07vCV'))
print(vowel_indices('E6q7yb7C4aPfuWFdelFbl'))
```

#### Output 
```
[2, 4, 6, 10]
[1, 2, 9]
[1, 6]
[1, 5, 10, 13, 17]
```

---

#### Solution

```python
def vowel_indices(word):
    return [i for i, v in enumerate(word, 1) if v in 'aeiouyAEIOUY']
```

---

[Codewars link](https://www.codewars.com/kata/5680781b6b7c2be860000036)
