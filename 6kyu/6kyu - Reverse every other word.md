## Reverse every other word in the string - 6kyu

**Instructions**

- Reverse every other word in a given string, then return the string.

- Throw away any leading or trailing whitespace, while ensuring there is exactly one space between each word.

- Punctuation marks should be treated as if they are a part of the word in this kata.

---

#### Test cases

```python
print(reverse_alternate("I really hope it works this time..."))
print(reverse_alternate("Reverse this string, please!"))
print(reverse_alternate("Have a beer"))
```

#### Output
```
I yllaer hope ti works siht time...
Reverse siht string, !esaelp
Have a beer
```

---

#### Solution

```python
def reverse_alternate(string):
    return ' '.join(word[::-1] if i & 1 else word for i, word in enumerate(string.split()))
```

---


[Codewars link](https://www.codewars.com/kata/58d76854024c72c3e20000de)
