## Start with a Vowel - 7kyu

**Instructions**

- Create a function that takes any sentence and redistributes the spaces (and adds additional spaces if needed) so that each word starts with a vowel. 

- The letters should all be in the same order but every vowel in the sentence should be the start of a new word. 

- The first word in the new sentence may start without a vowel. 

- It should return a string in all lowercase with no punctuation (only alphanumeric characters).

- `It is beautiful weather today!` becomes `it isb e a ut if ulw e ath ert od ay`. 

- `Coding is great` becomes `c od ing isgr e at`.

---

#### Test cases

```python
print(vowel_start('It is beautiful weather today!'))
print(vowel_start('Coding is great'))
print(vowel_start('my number is 0208-533-2325'))
print(vowel_start('oranges, apples, melon, pineapple'))
print(vowel_start('under_score'))
```

#### Output 

```
it isb e a ut if ulw e ath ert od ay
c od ing isgr e at
myn umb er is02085332325
or ang es appl esm el onp in e appl e
und ersc or e
```

---

#### Solution

```python
import re 
def vowel_start(st): 
    res = re.sub(r'[^0-9a-z]', '', st.lower())
    return re.sub(r'\B([aeiou])', r' \1', res)
```

---

[Codewars link](https://www.codewars.com/kata/5a02e9c19f8e2dbd50000167)
