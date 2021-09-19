## Poem formatter - 7kyu

**Instructions**

- Write a function, format_poem() that takes a one line string as an argument.
 
- Return a new string that is formatted across multiple lines with each new sentence starting on a new line when you print it out.

---

#### Test cases

```python
print(format_poem('Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated.'))
```

#### Output 
```
'Beautiful is better than ugly.\nExplicit is better than implicit.\nSimple is better than complex.\nComplex is better than complicated.'
```

---

#### Solution

```python
def format_poem(poem):
    # return '.\n'.join(poem.split('. '))

    return poem.replace('. ', '.\n')
```

---

[Codewars link](https://www.codewars.com/kata/585af8f645376cda59000200)
