## Replace with Alphabet Position - 6kyu

**Instructions**

- Given a string, replace every letter with its position in the alphabet.

- Ignore anything in the text that isn't a letter.

- eg. alphabet_position("The") should return "20 8 5"

---

#### Test cases

```python
print(alphabet_position("The sunset sets at twelve o'clock."))
print(alphabet_position("A Test For Upperc@se #and non-letters%"))
```

#### Output 
```
20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11
1 20 5 19 20 6 15 18 21 16 16 5 18 3 19 5 1 14 4 14 15 14 12 5 20 20 5 18 19
```

---

#### Solution

```python
def alphabet_position(text):
    return ' '.join(str(ord(let) - 96) for let in text.lower() if let.isalpha())
```

---


[Codewars link](https://www.codewars.com/kata/546f922b54af40e1e90001da)
