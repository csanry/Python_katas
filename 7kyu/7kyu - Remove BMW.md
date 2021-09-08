## Remove BMW - 7kyu

**Instructions**

- Write a function that takes one parameter str that MUST be a string and removes all capital and small letters B, M and W.

- If data of the wrong data type was sent as a parameter the function must throw an error with the following specific message:

```python
TypeError("This program only works for text.")
```


---

#### Test cases

```python
print(remove_bmw("bmwvolvoBMW"))
print(remove_bmw("blablahblah"))
print(remove_bmw(424))
```

#### Output 
```
volvo
lalahlah
This program only works for text.
```

---

#### Solution

```python
def remove_bmw(string):
    import re
    try:
        return re.sub(r'[bmw]', '', string, flags = re.I)
    except TypeError:
        return 'This program only works for text.'
```

---

[Codewars link](https://www.codewars.com/kata/59de795c289ef9197f000c48)
