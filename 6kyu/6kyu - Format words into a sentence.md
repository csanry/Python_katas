## Format words into a sentence - 6kyu

**Instructions**

- Complete the method so that it formats the words into a single comma separated value.

- The last word should be separated by the word 'and' instead of a comma.

- The method takes in an array of strings and returns a single formatted string.

- Empty string values should be ignored.

- Empty arrays or `null` values being passed into the method should result in an empty string being returned.

---

#### Test cases

```python
print(format_words(['one', 'two', 'three', 'four']))
print(format_words(['one']))
print(format_words(['one', '', 'three']))
print(format_words(['', '', 'three']))
print(format_words(['one', 'two', '']))
print(format_words([]))
print(format_words(None))
print(format_words(['']))
```

#### Output

```
one, two, three and four
one
one and three
three
one and two
""
""
""
```

---

#### Solution

```python
def format_words(words):
    if not words or words == ['']:
        return ''
    words = [w for w in words if w]
    if len(words) == 1:
        return words[0]
    return ', '.join(words[:-1]) + ' and ' + words[-1]
```

---

[Codewars link](https://www.codewars.com/kata/51689e27fe9a00b126000004)
