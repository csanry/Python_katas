## Club doorman - 7kyu

**Instructions**

- The Club Doorman will give you a word.

- To enter the Club you need to provide the right number according to provided the word.

- Every given word has a doubled letter, like 'tt' in lettuce.

- To answer the right number you need to find the doubled letter's position of the given word in the alphabet and multiply this number per 3.

- You will be given only words with one doubled letter.

---

#### Test cases

```python
print(pass_the_door_man("lettuce"))
print(pass_the_door_man("hill"))
print(pass_the_door_man("apple"))
```

#### Output

```
60
36
48
```

---

#### Solution

```python
import re
def pass_the_door_man(word):
    let = re.search(r'(\w)\1', word).group(1)
    return 3 * (ord(let)-96)
```

---

[Codewars link](https://www.codewars.com/kata/5c563cb78dac1951c2d60f01)
