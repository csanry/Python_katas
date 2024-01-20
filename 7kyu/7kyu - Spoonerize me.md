## Spoonerize me - 7kyu

**Instructions**

- A spoonerism is a spoken phrase in which the first letters of two of the words are swapped around, often with amusing results.

- In its most basic form a spoonerism is a two word phrase in which only the first letters of each word are swapped: `not picking` > `pot nicking`

- Create a function that takes a string of two words, separated by a space: words and returns a spoonerism of those words in a string, as in the above example.

---

#### Test cases

```python
print(spoonerize("nit picking"))
print(spoonerize("wedding bells"))
print(spoonerize("jelly beans"))
print(spoonerize("pop corn"))
```

#### Output

```
pit nicking
bedding wells
belly jeans
cop porn
```

---

#### Solution

```python
def spoonerize(words):
    w1, w2 = words.split()
    return f"{w2[0]}{w1[1:]} {w1[0]}{w2[1:]}"
```

---

[Codewars link](https://www.codewars.com/kata/56b8903933dbe5831e000c76/)
