## Mexican Wave - 6kyu

**Instructions**

- In this simple Kata your task is to create a function that turns a string into a Mexican Wave.

- You will be passed a string and you must return that string in an array where an uppercase letter is a person standing up.

**Example**

```
Wave wAve waVe wavE
```

- The input string will always be lower case but maybe empty.

- If the character in the string is whitespace then pass over it as if it was an empty seat.

---

#### Test cases

```python
print(wave("two words"))
print(wave("codewars testing for multiple words"))
```

#### Output 
```
['Two words', 'tWo words', 'twO words', 'two Words', 'two wOrds', 'two woRds', 'two worDs', 'two wordS']
['Codewars testing for multiple words', 'cOdewars testing for multiple words', 'coDewars testing for multiple words', 'codEwars testing for multiple words', 'codeWars testing for multiple words', 'codewArs testing for multiple words', 'codewaRs testing for multiple words', 'codewarS testing for multiple words', 'codewars Testing for multiple words', 'codewars tEsting for multiple words', 'codewars teSting for multiple words', 'codewars tesTing for multiple words', 'codewars testIng for multiple words', 'codewars testiNg for multiple words', 'codewars testinG for multiple words', 'codewars testing For multiple words', 'codewars testing fOr multiple words', 'codewars testing foR multiple words', 'codewars testing for Multiple words', 'codewars testing for mUltiple words', 'codewars testing for muLtiple words', 'codewars testing for mulTiple words', 'codewars testing for multIple words', 'codewars testing for multiPle words', 'codewars testing for multipLe words', 'codewars testing for multiplE words', 'codewars testing for multiple Words', 'codewars testing for multiple wOrds', 'codewars testing for multiple woRds', 'codewars testing for multiple worDs', 'codewars testing for multiple wordS']
```

---

#### Solution

```python
def wave(people):
    return [people[:i] + c.upper() + people[i + 1:] for i, c in enumerate(people) if c.isalpha()]
```

---


[Codewars link](https://www.codewars.com/kata/58f5c63f1e26ecda7e000029)
