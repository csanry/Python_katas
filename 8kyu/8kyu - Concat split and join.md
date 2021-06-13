## Concat split and join - 8kyu

**Instructions**

- Implement a function which accepts 2 arguments: `st` and `separator`.

- Split the string into words by spaces, split each word into separate characters and join them back with the specified separator.

- Join all the resulting "words" back into a sentence with spaces.

---

#### Test cases

```python
print(split_and_merge("My name is John", " "))
print(split_and_merge("My name is John", "-"))
print(split_and_merge("Hello World!", "."))
print(split_and_merge("Hello World!", ","))
```

#### Output 

```
M y n a m e i s J o h n
M-y n-a-m-e i-s J-o-h-n
H.e.l.l.o W.o.r.l.d.!
H,e,l,l,o W,o,r,l,d,!
```

---

#### Solution

```python
def split_and_merge(st, separator):
    return ' '.join(separator.join(word) for word in st.split())
```

---

[Codewars link](https://www.codewars.com/kata/57280481e8118511f7000ffa)
