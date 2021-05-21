## Stop gninnipS My sdroW! - 6kyu

**Instructions**

- Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (like the name of this kata).

- Strings passed in will consist of only letters and spaces.

- Spaces will be included only when more than one word is present.

---

#### Test cases

```python
print(spin_words("Hey fellow warriors"))
print(spin_words("This is a test"))
print(spin_words("This is another test"))
```

#### Output 
```
Hey wollef sroirraw
This is a test
This is rehtona test
```

---

#### Solution

```python
def spin_words(sentence):
    return ' '.join(word[::-1] if len(word) >= 5 else word for word in sentence.split())
```

---

[Codewars link](https://www.codewars.com/kata/5264d2b162488dc400000001)
