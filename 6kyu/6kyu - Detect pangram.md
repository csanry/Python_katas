## Detect Pangram - 6kyu

**Instructions**

- A pangram is a sentence that contains every single letter of the alphabet at least once.

- For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram.

- Given a string, detect whether or not it is a pangram.

- Return True if it is, False if not.

- Ignore numbers and punctuation.

---

#### Test cases

```python
pangram = "The quick, brown fox jumps over the lazy dog!"
not_pangram = "This is not a pangram"
is_pangram(pangram)
is_pangram(not_pangram)
```

#### Output
```
True
False
```

---

#### Solution

```python
import string

# checks if A is subset of B
def is_pangram(st):
    return set(string.ascii_lowercase) <= set(st.lower())
```

---

[Codewars link](https://www.codewars.com/kata/545cedaa9943f7fe7b000048)
