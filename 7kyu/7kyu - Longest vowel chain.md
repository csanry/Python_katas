## Longest vowel chain - 7kyu

**Instructions**

- The vowel substrings in the word `codewarriors` are `o, e, a, io`.

- The longest of these has a length of 2.

- Given a lowercase string that has alphabetic characters only (both vowels and consonants) and no spaces, return the length of the longest vowel substring.

- Vowels are any of aeiou.

---

#### Test cases

```python
print(solve("codewarriors"))
print(solve("suoidea"))
print(solve("ultrarevolutionariees"))
print(solve("strengthlessnesses"))
print(solve("cuboideonavicuare"))
print(solve("chrononhotonthuooaos"))
print(solve("iiihoovaeaaaoougjyaw"))
```

#### Output
```
2
3
3
1
2
5
8
```

---

#### Solution

```python
def solve(s):
    return max(map(len, ''.join(c if c in 'aeiou' else ' ' for c in s).split()))
```

---

[Codewars link](https://www.codewars.com/kata/59c5f4e9d751df43cf000035)
