## Alternate capitalization - 7kyu

**Instructions**

- Given a string, capitalize the letters that occupy even indexes and odd indexes separately, and return as shown below.

- For example, capitalize("abcdef") = ['AbCdEf', 'aBcDeF'].

- The input will be a lowercase string with no spaces.

---

#### Test cases

```python
print(capitalize("abcdef"))
print(capitalize("codewars"))
print(capitalize("abracadabra"))
print(capitalize("codewarriors"))
```

#### Output
```
['AbCdEf', 'aBcDeF']
['CoDeWaRs', 'cOdEwArS']
['AbRaCaDaBrA', 'aBrAcAdAbRa']
['CoDeWaRrIoRs', 'cOdEwArRiOrS']
```

---

#### Solution

```python
def capitalize(s):
    return [''.join(c.upper() if not i & 1 else c for i, c in enumerate(s)),
            ''.join(c.upper() if i & 1 else c for i, c in enumerate(s))]
```

---

[Codewars link](https://www.codewars.com/kata/59cfc000aeb2844d16000075)
