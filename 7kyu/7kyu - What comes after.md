## What comes after? - 7kyu

**Instructions**

- You will be given two inputs: a string of words and a letter.

- For each string, return the alphabetic character after every instance of letter(case insensitive).

- If there is a number, punctuation or underscore following the letter, it should not be returned.

- Return an empty string if there are no instances of letter in the given string.

---

#### Test cases

```python
print(comes_after("Pirates say arrrrrrrrr.", 'r'))
print(comes_after("Free coffee for all office workers!", 'F'))
print(comes_after("king kUnta is the sickest rap song ever kNown k!", 'k'))
print(comes_after("p8tice makes pottery p0rfect!", 'p'))
print(comes_after("nothing to be found here", 'z'))
```

#### Output

```
arrrrrrrr
rfeofi
iUeN
o
''
```

---

#### Solution

```python
def comes_after(st, l):
    return ''.join(b for (a, b) in zip(st, st[1:]) if a.lower() == l.lower() and b.isalpha())
```

---

[Codewars link](https://www.codewars.com/kata/590f5b4a7bbb3e246000007d)
