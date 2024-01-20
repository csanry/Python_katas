## Filter Long Words - 7kyu

**Instructions**

- Write a function `filter_long_words` that takes a string `sentence` and an integer `n`.

- Return a list of all words that are longer than `n`.

---

#### Test cases

```python
filter_long_words("The quick brown fox jumps over the lazy dog", 4)
```

#### Output

```
['quick', 'brown', 'jumps']
```

---

#### Solution

```python
def filter_long_words(sentence, n):
    return [*filter(lambda x: len(x) > n, sentence.split())]
```

---

[Codewars link](https://www.codewars.com/kata/5697fb83f41965761f000052)
