## Simple Pig Latin - 5kyu

**Instructions**

- Move the first letter of each word to the end of it, then add "ay" to the end of the word.

- Leave punctuation marks untouched.

---

#### Test cases

```python
print(pig_it('Pig latin is cool'))
print(pig_it('This is my string'))
```

#### Output

```
igPay atinlay siay oolcay
hisTay siay ymay tringsay
```

---

#### Solution

```python
def pig_it(text):
    return ' '.join(word[1:] + word[0] + 'ay' if word.isalpha() else word for word in text.split())
```

---

[Codewars link](https://www.codewars.com/kata/520b9d2ad5c005041100000f)
