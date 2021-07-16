## Where my anagrams at? - 5kyu

**Instructions**

- Two words are anagrams if they both contain the same letters.

```
'abba' & 'baab' == true
'abba' & 'bbaa' == true
'abba' & 'abbba' == false
'abba' & 'abca' == false
```

- Write a function that will find all the anagrams of a word from a list. You will be given two inputs: a word and an array with words. 

- Return an array of all the anagrams of the word, or an empty array if there are none. 

---

#### Test cases

```python
print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))
```

#### Output 
```
['aabb', 'bbaa']
['carer', 'racer']
```

---

#### Solution

```python
from collections import Counter

def anagrams(word, words): 
    base = Counter(word)
    return [w for w in words if base == Counter(w)]
```

---

[Codewars link](https://www.codewars.com/kata/523a86aa4230ebb5420001e1)
