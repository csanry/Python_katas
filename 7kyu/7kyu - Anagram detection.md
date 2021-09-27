## Anagram detection - 7kyu

**Instructions**

- An anagram is the result of rearranging the letters of a word to produce a new word.

- Return True if two argument given are anagrams of each other.

---

#### Test cases

```python
print(is_anagram("foefet", "toffee"))
print(is_anagram("Buckethead", "DeathCubeK"))
print(is_anagram("Twoo", "WooT"))
print(is_anagram("dumble", "bumble"))
print(is_anagram("ound", "round"))
print(is_anagram("apple", "pale"))
```

#### Output 
```
True
True
True
False
False
False
```

---

#### Solution

```python
def is_anagram(test, original):
    return sorted(test.lower()) == sorted(original.lower())
```

---

[Codewars link](https://www.codewars.com/kata/529eef7a9194e0cbc1000255)
