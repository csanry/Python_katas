## Character Frequency - 6kyu

**Instructions**

- Write a function that takes a piece of text in the form of a string and returns the letter frequency count for the text. 

- This count excludes numbers, spaces and all punctuation marks. 

- Upper and lower case versions of a character are equivalent and the result should all be in lowercase.

- The function should return a list of tuples sorted by the most frequent letters first. 


---

#### Test cases

```python
print(letter_frequency('Punctuation and Capital Letters Test...'))
print(letter_frequency('wklv lv d vhfuhw phvvdjh'))
```

#### Output 
```
[('t', 7), ('a', 4), ('e', 3), ('n', 3), ('c', 2), ('i', 2), ('l', 2), ('p', 2), ('s', 2), ('u', 2), ('d', 1), ('o', 1), ('r', 1)]
[('v', 5), ('h', 4), ('d', 2), ('l', 2), ('w', 2), ('f', 1), ('j', 1), ('k', 1), ('p', 1), ('u', 1)]
```

---

#### Solution

```python
from collections import Counter
def letter_frequency(text): 
    return sorted(Counter(filter(str.isalpha, text.lower())).items(), 
                  key=lambda x: (-x[1], x[0]))
```

---


[Codewars link](https://www.codewars.com/kata/53e895e28f9e66a56900011a)
